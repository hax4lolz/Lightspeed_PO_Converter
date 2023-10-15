# Halcyon PO Converter 

This program is intended to take a purchase order exported from LightSpeed POS and convert it into the correct format 
to send to Halcyon, a vendor of Extreme-Exposure.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements for Analysis Sticker.

```bash
pip install reportlab
pip install pyfiglet
```

## Usage

```python
python main.py --input-csv "file-path.csv"
```


## Roadmap
- Turn into a standalone windows program that runs in a window where the user can select which file to convert.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
