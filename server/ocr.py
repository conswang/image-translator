try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

print(pytesseract.image_to_string(Image.open('english.jpg'), lang='eng'))
print(pytesseract.image_to_string(Image.open('arabic.png'), lang='ara'))
print(pytesseract.image_to_string(Image.open('mandarin.jpg'), lang='chi_sim'))
