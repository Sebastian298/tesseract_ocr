import pytesseract
from PIL import Image
import pdf2image


def main():
    pages = pdf2image.convert_from_path('pdf/sample-pdf-file.pdf', 500)
    for page_number,image in enumerate(pages):
        image.save(f'images/page_{page_number}.png', 'PNG')
        img = Image.open(f'images/page_{page_number}.png')
        text = pytesseract.image_to_string(img)
        print(text)
    

if __name__ == '__main__':
    main()