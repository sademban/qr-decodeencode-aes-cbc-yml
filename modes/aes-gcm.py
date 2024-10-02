from Crypto.Cipher import AES
import base64

# 16-byte key
key = "xxxxxxxxxxx".encode("utf-8")
# 16-byte IV (GCM also requires an IV)
iv = "xxxxxxxxxxx".encode("utf-8")

# Encrypted Base64 string
encrypted_base64 = "xxxxxxxxxxxxx==" 
encrypted_data = base64.b64decode(encrypted_base64)

# Initialize AES cipher in GCM mode
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

try:
    # Decrypt the data (without tag verification in this example)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_text = decrypted_data.decode('utf-8')
    print("Decrypted (GCM mode) data:", decrypted_text)
except ValueError as e:
    print(f"Decryption error (GCM mode): {e}")
