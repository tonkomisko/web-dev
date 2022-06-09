from PIL import Image
from pytesseract import pytesseract


path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
folder_path = r"C:\Users\antonsuslik\OneDrive\Desktop\Zaklady Programovania a BlbstckY\Programming\Python" \
              r"\pyteserract_images_to_process"


for _ in range(2):
    print("found an image...")
    image_path = folder_path + r"\2" + ".jpg"
    print(image_path)
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img)

    print(text[:-1])

# comment

