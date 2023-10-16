import argparse
import csv
import pyfiglet  # Import module for startup banner
import re  # Import the regular expression module
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

import address


# Function to strip HTML tags from a string
def strip_tags(text):
    return re.sub(r'<.*?>', '', text)


# Function to read data from a CSV file
def read_csv(file_path):
    print("\nReading .csv file")
    data = []
    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


# Function to generate a PDF with header and CSV data
def create_pdf(output_pdf_path, csv_data):
    print("\nGenerating PDF")
    doc = SimpleDocTemplate(output_pdf_path, pagesize=landscape(letter))
    styles = getSampleStyleSheet()

    # Define which columns need special handling e.g. removed or adjusted
    columns_to_exclude = [0, 3, 5, 6, 8, 12, 11]  # Example: Remove columns 2 and 4

    # Modify the CSV data by excluding specified columns
    modified_data = []
    for row in csv_data:
        modified_row = [cell for index, cell in enumerate(row) if index not in columns_to_exclude]
        modified_data.append(modified_row)

    # Create a list of flowable elements for the PDF
    elements = []

    vendor_address = """
        Vendor Information <br />
        Halcyon Manufacturing <br />
        24587 NW 178th Place <br />
        High Springs, FL 32643 <br />
        386.454.0811 <br />
        386.454.0815
    """

    dealer_address = """
        Dealer Information <br />
        Extreme Exposure <br />
        Dealer Number 1158 <br />
        18481 High Spring Main Street <br />
        High Springs, FL 32643 <br />
        386.454.8158
    """

    # Define the style for the addresses
    styles = getSampleStyleSheet()
    address_style = styles["Normal"]
    address_style.fontName = "Helvetica"  # Set the font to Helvetica
    address_style.fontSize = 12  # Set the font size

    # Create a two-column table for the header information
    header_table_data = [
        [Paragraph(vendor_address, address_style), Paragraph(dealer_address, address_style)]
    ]

    header_table = Table(header_table_data, colWidths=[400, 200])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (0, 0), (1, -1), 'RIGHT'),
    ]))

    elements.append(header_table)

    elements.append(Spacer(1, 12))

    # Add the CSV data with HTML tags stripped
    cleaned_data = [[strip_tags(cell) for cell in row] for row in modified_data]

    # Create a table for the CSV data
    table = Table(cleaned_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # Build the PDF document
    doc.build(elements)


def main():
    # Startup banner
    ascii_banner = pyfiglet.figlet_format("Halcyon PO Generator")
    print(ascii_banner)

    # Code starts
    parser = argparse.ArgumentParser(description='''
    
    A Simple Python script to take a PO output from Lightspeed and convert it to a PDF for Halcyon.
    ''')
    parser.add_argument("--input-csv", required=True, help='Path to the input CSV file. Ex. --input-csv "file.csv"')
    parser.add_argument("--vendor", required=True, help='Vendor name for PO. Must match address book. Ex. --vendor "Halcyon"')
    args = parser.parse_args()

    output_pdf_file = 'order.pdf'  # Replace with the desired output PDF file
    input_csv_file = args.input_csv
    vendor_address = args.vendor

    csv_data = read_csv(input_csv_file)
    create_pdf(output_pdf_file, csv_data)
    print("\nComplete. PDF file saved to: " + output_pdf_file)


if __name__ == '__main__':
    main()
