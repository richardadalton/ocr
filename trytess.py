from PIL import Image
import pytesseract

image = Image.open("sample.png")
print(pytesseract.image_to_string(image))

