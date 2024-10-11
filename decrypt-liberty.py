import yaml # type: ignore
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Load the config.yml file
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Get the secret key and IV from the config
key = config['qrcode']['secretKey'].encode('utf-8')
iv = config['qrcode']['iv'].encode('utf-8')

# Encrypted Base64 string (replace this with the actual encrypted string)
encrypted_base64 = "-8YXcAWvCPY1WmVQnK1v_g=="  # Example from your previous output 
# Decode the Base64 string to get the encrypted bytes
encrypted_data = base64.b64decode(encrypted_base64)

# Initialize the AES cipher in CBC mode with PKCS5Padding
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the data
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

# Decode the decrypted bytes to a string
decrypted_text = decrypted_data.decode('utf-8')
print("Decrypted data: " + decrypted_text)
