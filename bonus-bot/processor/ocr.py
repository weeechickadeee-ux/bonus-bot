import cv2
import pytesseract

def extract_text_from_image(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    print("OCR OUTPUT:", text)

    import re
    match = re.search(r"[A-Z0-9]{5,}", text)

    if match:
        return match.group(0)

    return None