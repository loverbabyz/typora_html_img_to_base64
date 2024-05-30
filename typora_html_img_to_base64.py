import os
import base64
import logging
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_img_to_base64(html_file_path):
    with open(html_file_path, 'r') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')

    base_dir = os.path.dirname(html_file_path)
    assets_dir = os.path.join(base_dir, 'assets')

    for img in soup.find_all('img'):
        img_file_path_assets = os.path.join(assets_dir, img['src'])
        img_file_path_base = os.path.join(base_dir, img['src'])

        if os.path.isfile(img_file_path_assets):
            img_file_path = img_file_path_assets
        elif os.path.isfile(img_file_path_base):
            img_file_path = img_file_path_base
        else:
            logging.warning(f"Image file not found: {img['src']}")
            continue

        logging.info(f"Processing image file: {img_file_path}")

        with Image.open(img_file_path) as img_file:
            buffered = BytesIO()
            img_file.save(buffered, format=img_file.format)
            img_b64 = base64.b64encode(buffered.getvalue()).decode()

            img['src'] = f'data:image/{img_file.format};base64,{img_b64}'

    with open(html_file_path, 'w') as file:
        file.write(str(soup))

if __name__ == '__main__':
    import sys
    convert_img_to_base64(sys.argv[1])
