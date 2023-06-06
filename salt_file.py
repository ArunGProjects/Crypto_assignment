import random
import string
import hashlib
import os
password_file = "passwords.txt"
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
with open(password_file, 'w') as file:
    for _ in range(10):
        password = generate_password()
        file.write(password + '\n')
print("Password file created:", password_file)
hashed_password_file = "hashed_passwords.txt"
def compute_hash(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()
with open(password_file, 'r') as input_file, open(hashed_password_file, 'w') as output_file:
    for line in input_file:
        password = line.strip()
        hashed_password = compute_hash(password)
        output_file.write(hashed_password + '\n')
print("Hashed password file created:", hashed_password_file)
salt_file = "salt.txt"
hashed_password_file = "hashed_passwords.txt"
def generate_salt(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    salt = ''.join(random.choice(characters) for _ in range(length))
    return salt
def compute_hash1(password, salt):
    salted_password = salt + password
    hash_object = hashlib.sha256()
    hash_object.update(salted_password.encode('utf-8'))
    return hash_object.hexdigest()
salt = generate_salt()
with open(salt_file, 'w') as file:
    file.write(salt)
with open(password_file, 'r') as input_file, open(hashed_password_file, 'w') as output_file:
    for line in input_file:
        password = line.strip()
        hashed_password = compute_hash1(password, salt)
        output_file.write(hashed_password + '\n')
print("Salt file created:", salt_file)
print("Hashed password file with salt created:", hashed_password_file)


