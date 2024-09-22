import pytesseract
from PIL import Image


def img_to_text(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(img_path), lang='rus')
    return text