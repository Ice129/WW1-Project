#
# Function to change adminstrator account password

import hashlib
import os
import logging

# Basic logging, displaying timestamp of the log, severity level and the log message itself
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Generates a random salt with a length of 16 integers
def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)

# Hashes the password using SHA256, then returns the hex
def hash_password_sha256(password: str, salt: bytes, iterations: int = 100000) -> str:
    try:
        password_bytes = password.encode('utf-8')
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',
            password_bytes,
            salt,
            iterations
        )
        return hashed_password.hex()
    except Exception as e:
        logging.error(f"An error occurred while hashing the password: {e}")
        raise
    
def save_to_file(filename: str, hashed_password: str, salt: str):
    try:
        with open (filename, 'w') as file:
            file.write(f"Hashed Password: {hashed_password}\n")
            file.write(f"Salt: {salt}\n")
        logging.info(f"Password and salt saved to {filename}.")
    except Exception as e:
        logging.error(f"An error occurred while saving to file: {e}")
        raise
    
