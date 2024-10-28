from PIL import Image
import pyzbar.pyzbar as pyzbar
import yaml  # type: ignore
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Load the config.yml file for AES decryption details
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Get the secret key and IV from the config
key = config['qrcode']['secretKey'].encode('utf-8')
iv = config['qrcode']['iv'].encode('utf-8')

# Load the image with the QR code
img = Image.open(r'media/test.png')  # Replace with the correct path to your QR code image

# Decode the QR code
decoded_objects = pyzbar.decode(img)

# Check if any QR codes were found
if decoded_objects:
    # Extract the encrypted Base64 data from the first QR code (assuming only one)
    encrypted_base64 = decoded_objects[0].data.decode('utf-8')
    
    # Replace '-' with '+' and '_' with '/' in the Base64 string (if necessary)
    encrypted_base64 = encrypted_base64.replace('-', '+').replace('_', '/')
    
    # Decode the Base64 string to get the encrypted bytes
    encrypted_data = base64.b64decode(encrypted_base64)
    
    # Initialize the AES cipher in CBC mode with PKCS5Padding
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    # Decode the decrypted bytes to a string
    decrypted_text = decrypted_data.decode('utf-8')
    
    # Print the decrypted data
    print("Decrypted data from QR code:", decrypted_text)
else:
    print("No QR code detected in the image.")
