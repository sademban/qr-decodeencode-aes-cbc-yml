from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# 16-byte key
key = "xxxxxxxxx".encode("utf-8")
# 16-byte IV
iv = "xxxxxxxxxxx".encode("utf-8")

# Encrypted Base64 string
encrypted_base64 = "xxxxxxxxxxxxx==" 
encrypted_data = base64.b64decode(encrypted_base64)

# Initialize AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

try:
    # Decrypt the data and unpad
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    decrypted_text = decrypted_data.decode('utf-8')
    print("Decrypted (CBC mode) data:", decrypted_text)
except ValueError as e:
    print(f"Decryption error (CBC mode): {e}")
