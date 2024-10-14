import easyocr

def extract_text_with_easyocr(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    text = ' '.join([item[1] for item in result])
    return text

# Example usage
print(extract_text_with_easyocr('C://Users/HP/Desktop/pic.png'))
