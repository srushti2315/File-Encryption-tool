import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

from cryptography import fernet
from cryptography.fernet import Fernet
import sqlite3
from cryptography.fernet import InvalidToken
from tkinter import ttk


class FileEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        self.root.title("File Encryption Tool")

        self.label = ctk.CTkLabel(root, text="Select a file to encrypt:")
        self.label.pack(pady=10)

        self.file_button = ctk.CTkButton(root, text="Choose File", command=self.choose_file)
        self.file_button.pack(pady=10)

        self.encrypt_button = ctk.CTkButton(root, text="Encrypt", command=self.encrypt_file)
        self.encrypt_button.pack(side='left', padx=50, pady=50)

        self.decrypt_button = ctk.CTkButton(root, text="Decrypt", command=self.decrypt_file)
        self.decrypt_button.pack(side='right', padx=50, pady=50)

        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

        self.conn = sqlite3.connect("fileDB.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS encrypted_files
                               (id INTEGER PRIMARY KEY,
                               file_name TEXT,
                               encrypt_data BLOB)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS decrypted_files
                               (id INTEGER PRIMARY KEY,
                               file_name TEXT,
                               decrypt_data BLOB)''')
        self.conn.commit()

    def choose_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.label.configure(text=f"selected File: {self.file_path}")

    def encrypt_file(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                encrypt_data = self.fernet.encrypt(file_data)

                # Saving the encrypted data to a file with the original file extension
                file_name = self.file_path.split('/')[-1]
                encrypted_file_name = file_name + '.encrypted'  # Append extension to indicate encryption
                with open(encrypted_file_name, 'wb') as encrypted_file:
                    encrypted_file.write(encrypt_data)

                # Inserting into the database
                self.cursor.execute('''INSERT INTO encrypted_files (file_name, encrypt_data)
                                    VALUES (?, ?)''', (file_name, encrypt_data))
                self.conn.commit()
                self.label.configure(text="File encrypted and saved!")
        else:
            self.label.configure(text="No file selected!")

    def decrypt_file(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                try:
                    decrypt_data = self.fernet.decrypt(file_data)

                    # Extract original filename and extension
                    original_file_name = self.file_path.split('/')[-1]
                    decrypted_file_name = original_file_name[:-10]

                    # Save the decrypted data to a new file
                    with open(decrypted_file_name, 'wb') as decrypted_file:
                        decrypted_file.write(decrypt_data)

                    self.label.configure(text="File decrypted and saved as: " + decrypted_file_name)

                except InvalidToken:
                    self.label.configure(text="Error: Unable to decrypt file. Invalid or corrupted data.")

        else:
            self.label.configure(text="No file selected!")


if __name__ == "__main__":
    root = ctk.CTk()
    app = FileEncryptionTool(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()
