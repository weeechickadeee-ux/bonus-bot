import re

def process_text(text):

    if not text:
        return None

    # simple cleanup for codes
    match = re.search(r"[A-Z0-9]{5,}", text)

    if match:
        return match.group(0)

    return None