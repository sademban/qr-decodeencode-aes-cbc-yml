import yaml # type: ignore
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Load the config.yml file
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Get the secret key and IV from the config
key = config['qrcode']['secretKey'].encode('utf-8')
iv = config['qrcode']['iv'].encode('utf-8')

# Input string to encrypt
input_data = "xxxxxxxxxxx".encode("utf-8")

# Initialize the AES cipher in CBC mode with PKCS5Padding
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the input string using PKCS5 padding
encrypted_data = cipher.encrypt(pad(input_data, AES.block_size))

# Convert the encrypted bytes to Base64 for easy storage/display
encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')
print("Encrypted Base64 data: " + encrypted_base64)
