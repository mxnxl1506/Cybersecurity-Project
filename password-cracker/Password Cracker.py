#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib

def crack_password(hash_value, password_list):
    for password in password_list:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == hash_value:
            return password
    return None

# Example usage:
hash_to_crack = "2bb80d839158409aabadb9ed93fcb12e15870f66cf44144d3625a8c85c23c716"  # SHA-256 hash
common_passwords = ["password", "123456", "letmein", "qwerty"]

cracked_password = crack_password(hash_to_crack, common_passwords)
if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found in the list.")

