# Example 1: Nested Loop for a 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Example 1:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Example 2: Nested Loop for Multiplication Table
print("\nExample 2:")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)

        return text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
image_path = 'c:/Users/HP/Desktop/pic.png'
extracted_text = extract_text_from_image(image_path)

if extracted_text:
    print("Text extracted from the image:")
    print(extracted_text)
else:
    print("Failed to extract text from the image.")
