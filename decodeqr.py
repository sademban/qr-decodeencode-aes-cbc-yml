from PIL import Image
import pyzbar.pyzbar as pyzbar

# Load the image with the QR code
# img = Image.open(r'test\1.png')  # Replace with the path to your QR code image
img = Image.open(r'media/test.png')  # [hospital code : 0153] [clinic code:0001]  [customer code:000013]

# Decode the QR code
decoded_objects = pyzbar.decode(img)

# Extract and print the data from the decoded QR code
for obj in decoded_objects:
    print("Decoded QR code data:", obj.data.decode('utf-8'))
