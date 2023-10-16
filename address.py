import json


def load_address_book(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_address_book(address_book, filename):
    with open(filename, 'w') as file:
        json.dump(address_book, file, indent=4)  # Indent for pretty formatting


def print_address(name, address_book):
    if name in address_book:
        person_info = address_book[name]
        print(f"Name: {name}")
        print(f"Display Name: {person_info['full_name']}")
        print(f"Street Address: {person_info['street_address']}")
        print(f"City: {person_info['city']}")
        print(f"Phone Number: {person_info['phone_number']}")
        print(f"Dealer Number: {person_info['dealer_number']}")
    else:
        print("Address not found in the address book.")


def add_address(name, full_name, street_address, city, phone_number, dealer_number, address_book, filename):
    address_book[name] = {
        "full_name": full_name,
        "street_address": street_address,
        "city": city,
        "phone_number": phone_number,
        "dealer_number": dealer_number
    }
    save_address_book(address_book, filename)
    print(f"Address for {name} added to the address book.")


def edit_address(name, full_name, street_address, city, phone_number, dealer_number, address_book, filename):
    if name in address_book:
        address_book[name]["full_name"] = full_name
        address_book[name]["street_address"] = street_address
        address_book[name]["city"] = city
        address_book[name]["phone_number"] = phone_number
        address_book[name]["dealer_number"] = dealer_number
        save_address_book(address_book, filename)
        print(f"Address for {name} updated in the address book.")
    else:
        print("Address not found in the address book.")


def main():
    filename = "address.json"

    address_book = load_address_book(filename)

    while True:
        print("\nAddress Book Menu:")
        print("1. View Address")
        print("2. Add Address")
        print("3. Edit Address")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name to view the address: ")
            print_address(name, address_book)
        elif choice == "2":
            name = input("Enter the short name to add to the address book: ")
            full_name = input("Enter the full name to be shown: ")
            street_address = input("Enter the street address: ")
            city = input("Enter the City, State Zip: ")
            phone_number = input("Enter the phone number: ")
            dealer_number = input("Enter the Dealer Number or Dealer Contact: ")
            add_address(name, full_name, street_address, city, phone_number, dealer_number, address_book, filename)
        elif choice == "3":
            name = input("Enter the short name to edit in the address book: ")
            full_name = input("Enter the full name to be shown: ")
            street_address = input("Enter the updated street address: ")
            city = input("Enter the updated City, State Zip: ")
            phone_number = input("Enter the updated phone number: ")
            dealer_number = input("Enter the Dealer Number or Dealer Contact: ")
            edit_address(name, full_name, street_address, city, phone_number, dealer_number, address_book, filename)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
