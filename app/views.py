import exifread
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
import folium
import os
from django.urls import reverse
from django.shortcuts import redirect
from fractions import Fraction
import exifread

def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def imageinfo(request):
    if request.method == "POST":
        image = request.FILES.get('image')

        if image is not None:
            img = Image.open(image)
            exif_data = exifread.process_file(image)

            # Get image dimensions and other basic info
            dimensions = img.size
            size = image.size
            pixels = dimensions[0] * dimensions[1]

            # Extract additional EXIF information
            make = exif_data.get('Image Make', 'Unknown')
            model = exif_data.get('Image Model', 'Unknown')
            datetime_taken = exif_data.get('EXIF DateTimeOriginal', 'Unknown')

            latitude = None
            longitude = None

            if 'GPS GPSLatitude' in exif_data and 'GPS GPSLongitude' in exif_data:
                lat_values = exif_data['GPS GPSLatitude'].values
                lat_ref = exif_data['GPS GPSLatitudeRef'].values
                lon_values = exif_data['GPS GPSLongitude'].values
                lon_ref = exif_data['GPS GPSLongitudeRef'].values

                latitude = dms_to_decimal(float(lat_values[0]), float(lat_values[1]), float(lat_values[2]), lat_ref)
                longitude = dms_to_decimal(float(lon_values[0]), float(lon_values[1]), float(lon_values[2]), lon_ref)

            getinfo = {
                'file_name': image.name,
                'dimensions': dimensions,
                'size': size,
                'pixels': pixels,
                'latitude': latitude,
                'longitude': longitude,
                'make': make,
                'model': model,
                'datetime_taken': datetime_taken
            }

            return render(request, "home.html", {'getinfo': getinfo})

        else:
            return HttpResponse("No image uploaded.")

    return render(request, "home.html")


import folium

def imap(request, latitude, longitude):
    map_file_path = "map.html"  # Adjust the path as needed

    try:
        lat = float(latitude)
        lon = float(longitude)

        # Create a map centered on the location
        mymap = folium.Map(location=[lat, lon], zoom_start=14)

        # Add a marker for the main location
        folium.Marker(location=[lat, lon], popup="Location", icon=folium.Icon(color='blue')).add_to(mymap)

        # Example data for temples and shops
        temples = [
            {"name": "Temple A", "location": [lat + 0.002, lon + 0.002]},
            {"name": "Temple B", "location": [lat + 0.005, lon - 0.005]},
        ]

        shops = [
            {"name": "Shop A", "location": [lat - 0.002, lon - 0.002]},
            {"name": "Shop B", "location": [lat - 0.003, lon + 0.003]},
        ]

        # Add temple markers to the map
        for temple in temples:
            folium.Marker(
                location=temple["location"],
                popup=temple["name"],
                icon=folium.Icon(color='orange')
            ).add_to(mymap)

        # Add shop markers to the map
        for shop in shops:
            folium.Marker(
                location=shop["location"],
                popup=shop["name"],
                icon=folium.Icon(color='green')
            ).add_to(mymap)

        # Save the map to an HTML file
        mymap.save(map_file_path)

        # Render the map in the template
        with open(map_file_path, 'r') as f:
            map_html = f.read()

        return render(request, "map.html", {'map': map_html})

    except (ValueError, TypeError):
        return render(request, "map.html", {'error': "No Location details available for this photo."})


from django.shortcuts import render
import easyocr
import numpy as np
from PIL import Image
import io

def extract_text_with_easyocr(request):
    text = ""
    if request.method == "POST":
        if 'image' not in request.FILES:
            return render(request, 'read_img.html', {'error': 'No image uploaded.'})

        image_file = request.FILES['image']
        
        # Read the image file and convert it to a format EasyOCR can process
        image = Image.open(image_file)
        image = np.array(image)  # Convert the PIL image to a NumPy array
        
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)
        text = ' '.join([item[1] for item in result])

    return render(request, 'read_img.html', {'text': text})
