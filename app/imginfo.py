
image_path = 'D:\\Photos\\2024\\FullSizeRender 6.JPG'

from PIL import Image
from PIL.ExifTags import TAGS
import os

def get_image_details(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Get basic image details
        image_info = {
            'file_name': os.path.basename(image_path),
            'size_bytes': os.path.getsize(image_path),
            'dimensions': img.size,
            'pixels': img.size[0] * img.size[1],
        }

        # Get Exif data
        exif_data = img._getexif()

        if exif_data is not None:
            for tag, value in exif_data.items():
                # Skip MakerNote section (tag 37500)
                if tag == 37500:
                    continue

                tag_name = TAGS.get(tag, tag)
                image_info[tag_name] = value

        return image_info

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage

image_details = get_image_details(image_path)

if image_details:
    print("Image Details:")
    for key, value in image_details.items():
        print(f"{key}: {value}")
else:
    print("Failed to get image details.")
