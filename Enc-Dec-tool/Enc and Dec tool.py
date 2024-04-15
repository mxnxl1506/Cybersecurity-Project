#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage:
key = generate_key()
message = "Hello, world!"
encrypted = encrypt_message(message, key)
decrypted = decrypt_message(encrypted, key)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")

