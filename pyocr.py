import argparse
from PIL import Image
import pytesseract

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="testimage.png",
                        help="Path to image file containing text")

    args = parser.parse_args()
    return args

def get_text(filename):
    image = Image.open(filename)
    return pytesseract.image_to_string(image)

def main():
    args = get_arguments()
    text = get_text(args.file)
    print(text)

main()