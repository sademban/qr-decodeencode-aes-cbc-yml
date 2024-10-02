from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64

# 16-byte key
key = "xxxxxxxxxxxx".encode("utf-8")
# IV to create a counter (CTR mode uses a counter, not directly IV)
iv = "xxxxxxxxxxxxx".encode("utf-8")

# Encrypted Base64 string
encrypted_base64 = "xxxxxxxxxxxxx==" 
encrypted_data = base64.b64decode(encrypted_base64)

# Create counter from IV
ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))

# Initialize AES cipher in CTR mode
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

try:
    # Decrypt the data (CTR doesn't require unpadding)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_text = decrypted_data.decode('utf-8')
    print("Decrypted (CTR mode) data:", decrypted_text)
except ValueError as e:
    print(f"Decryption error (CTR mode): {e}")
