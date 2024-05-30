# HTML Image to Base64 Converter

This Python script converts all images in an HTML file to base64 format. This is useful for embedding images directly into the HTML, reducing the number of HTTP requests.

## Requirements

- Python 3.6+
- BeautifulSoup4
- Pillow

You can install the Python dependencies with pip:

```bash
pip install beautifulsoup4 pillow
```

## Usage

To use the script, pass the path of the HTML file as a command-line argument:

```bash
python typora_html_img_to_base64.py your_file.html
```

The script will modify the HTML file in-place, replacing all src attributes of img tags with the base64-encoded image data.

## Logging

The script uses Python's built-in logging module to output information about its progress. By default, it logs warnings and errors. You can change the log level by modifying the logging.basicConfig(level=logging.INFO) line at the top of the script.

## Limitations

The script assumes that all images are located either in the same directory as the HTML file or in a subdirectory named 'assets'. If your images are located elsewhere, you will need to modify the script accordingly.
