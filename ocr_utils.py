# ocr_utils.py
import easyocr

reader = easyocr.Reader(['en'])

def extract_plate_text(image):
    results = reader.readtext(image)
    for (_, text, prob) in results:
        if prob > 0.4 and len(text) >= 4:
            return text.upper()
    return None
