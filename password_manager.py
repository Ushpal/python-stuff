from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, key_file="key.key", data_file="passwords.json"):
        self.key_file = key_file
        self.data_file = data_file
        self.load_or_generate_key()

    def load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                self.key = key_file.read()
        else:
            self.key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(self.key)

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password

    def save_password(self, service, username, password):
        encrypted_password = self.encrypt_password(password)
        data = self.load_data()
        data[service] = {"username": username, "password": encrypted_password}
        self.save_data(data)

    def get_password(self, service):
        data = self.load_data()
        if service in data:
            encrypted_password = data[service]["password"]
            decrypted_password = self.decrypt_password(encrypted_password)
            return decrypted_password
        else:
            return None

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
            return data
        else:
            return {}

    def save_data(self, data):
        with open(self.data_file, "w") as file:
            json.dump(data, file)


password_manager = PasswordManager()


password_manager.save_password("Take password", "Comic", "1234567890")


retrieved_password = password_manager.get_password("Take Password")
if retrieved_password:
    print("Retrieved Password:", retrieved_password)
else:
    print("Service not found.")
