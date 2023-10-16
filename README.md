# Lightspeed PO Converter 

This program is intended to take a purchase order exported from LightSpeed POS and convert it into a pdf with a nice template that includes addresses.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements for PO Converter.

```bash
pip install reportlab
pip install pyfiglet
```

## Usage

```python
python main.py --input-csv "file-path.csv" --vendor Vendor
```

## Files
- main.py Main program
- address.py Contains functions specific to address lookup and maintenance.
- address.json Contains addresses to be used for the PO conversion.

## Roadmap
- Turn into a standalone windows program that runs in a window where the user can select which file to convert.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
