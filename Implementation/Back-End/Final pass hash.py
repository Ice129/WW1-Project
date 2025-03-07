


import hashlib
import os
import logging
from getpass import getpass

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)

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

def verify_password_sha256(plain_password: str, hashed_password: str, salt: bytes, iterations: int = 100000) -> bool:
    try:
        new_hashed_password = hash_password_sha256(plain_password, salt, iterations)

        return new_hashed_password == hashed_password

    except Exception as e:
        logging.error(f"An error occurred while verifying the password: {e}")
        raise

def validate_password(password: str) -> bool:
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    return True

def save_to_file(filename: str, hashed_password: str, salt: str):
    try:
        with open(filename, 'w') as file:
            file.write(f"Hashed Password: {hashed_password}\n")
            file.write(f"Salt: {salt}\n")
        logging.info(f"Data saved to {filename}.")
    except Exception as e:
        logging.error(f"An error occurred while saving to file: {e}")
        raise

def load_from_file(filename: str) -> tuple:

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            hashed_password = lines[0].split(": ")[1].strip()
            salt = lines[1].split(": ")[1].strip()
        logging.info(f"Data loaded from {filename}.")
        return hashed_password, salt
    except Exception as e:
        logging.error(f"An error occurred while loading from file: {e}")
        raise

if __name__ == "__main__":
    try:
        while True:
            password = getpass("Enter your password: ").strip()
            if validate_password(password):
                break
            print("Please try again.")

        salt = generate_salt()
        salt_hex = salt.hex()
        print(f"Salt (hex): {salt_hex}")

        hashed_password = hash_password_sha256(password, salt)
        print(f"Hashed Password: {hashed_password}")

        save_to_file("password.txt", hashed_password, salt_hex)

        loaded_hashed_password, loaded_salt = load_from_file("password.txt")

        verify_password = getpass("Enter your password again to verify: ").strip()
        is_valid = verify_password_sha256(verify_password, loaded_hashed_password, bytes.fromhex(loaded_salt))
        print(f"Password is valid: {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")