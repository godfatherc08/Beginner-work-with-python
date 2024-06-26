
from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)
d = input("Enter: ").encode()

encrypted_data = f.encrypt(d)
print(encrypted_data)
decrypted_data = f.decrypt(encrypted_data)
print(decrypted_data.decode())