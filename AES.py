from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from Crypto.Util.Padding import pad, unpad

# AES requires the key to be 16, 24, or 32 bytes long
key = get_random_bytes(16)  # Generate a random 128-bit key
iv = get_random_bytes(16)   # AES requires an initialization vector (IV)

#AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Sample message
message = "This is a secret message!"
message_bytes = message.encode('utf-8')

# Padding the message to make it a multiple of block size (16 bytes)
padded_message = pad(message_bytes, AES.block_size)

# Encrypt 
encrypted_message = cipher.encrypt(padded_message)

# Decrypting
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_message = unpad(decipher.decrypt(encrypted_message), AES.block_size)

# Convert bytes back to string
decrypted_message = decrypted_message.decode('utf-8')

# Show results
print("Original Message: ", message)
print("Encrypted Message (base64): ", base64.b64encode(encrypted_message).decode())
print("Decrypted Message: ", decrypted_message)