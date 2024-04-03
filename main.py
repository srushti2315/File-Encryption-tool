import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, Menu
import os
from cryptography import fernet
from cryptography.fernet import Fernet
import sqlite3
from cryptography.fernet import InvalidToken
from tkinter import ttk
from PIL import Image, ImageTk

class FileEncryptionTool:
    def __init__(self, root):
        self.encrypted_file_path = None
        self.root = root
        self.file_path = None
        self.root.title("File Encryption Tool")

        # self.bg_image = Image.open("Safeimagekit-resized-img (1).png")
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        # self.background_label = tk.Label(root, image=self.bg_photo)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.tab_control = ttk.Notebook(root, width=400, height=300)
        self.tab_control.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.create_navbar()

        heading_label = ctk.CTkLabel(self.root, text="Welcome to File Encryption Tool", font=('Helvetica', 24))
        heading_label.pack(pady=10)

        self.sender_tab = ctk.CTkFrame(self.tab_control)
        self.tab_control.add(self.sender_tab, text="Sender")

        self.receiver_tab = ctk.CTkFrame(self.tab_control)
        self.tab_control.add(self.receiver_tab, text="Receiver")

        self.create_sender_tab()
        self.create_receiver_tab()

        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

        self.conn = sqlite3.connect("fileDB.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

        self.root.geometry("800x600")

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

    def create_navbar(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def create_buttons(self):
        encrypt_button = ctk.CTkButton(self.main_frame, text="Encrypt File", command=self.encrypt_file)
        encrypt_button.pack(pady=10)

        decrypt_button = ctk.CTkButton(self.main_frame, text="Decrypt File", command=self.decrypt_file)
        decrypt_button.pack(pady=10)
        select_button = ctk.CTkButton(self.main_frame, text="Select File", command=self.choose_file)
        decrypt_button.pack(pady=10)

    def about(self):
        messagebox.showinfo("About", "File Encryption Tool\nVersion 1.0\nDeveloped by Your Name")

    def create_sender_tab(self):
        file_button = ctk.CTkButton(self.sender_tab, text="Select File", command=self.choose_file)
        file_button.pack(pady=10)

        encrypt_button = ctk.CTkButton(self.sender_tab, text="Encrypt", command=self.encrypt_file)
        encrypt_button.pack(pady=10)

        send_button = ctk.CTkButton(self.sender_tab, text="Send Encrypted File", command=self.send_encrypted_file)
        send_button.pack(pady=10)

    def create_receiver_tab(self):
        self.decrypt_button = ctk.CTkButton(self.receiver_tab, text="Decrypt", command=self.decrypt_file)
        self.decrypt_button.pack(pady=10)

    def send_encrypted_file(self):
        self.cursor.execute("SELECT file_name FROM encrypted_files ORDER BY id DESC LIMIT 1")
        encrypted_file_data = self.cursor.fetchone()

        if encrypted_file_data:
            encrypted_file_name = encrypted_file_data[0] + '.encrypted'
            encrypted_file_path = os.path.join('encrypted_files', encrypted_file_name)

            encrypted_path_label = ctk.CTkLabel(self.receiver_tab, width=50)
            encrypted_path_label.configure(text=f"Encrypted File Path: {encrypted_file_path}")
            encrypted_path_label.pack(pady=10)

            self.encrypted_file_path = encrypted_file_path
            messagebox.showinfo("Success", "File sent to Receiver successfully!")
        else:
            messagebox.showerror("Error", "No encrypted file found in the database.")

    def encrypt_file(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                encrypt_data = self.fernet.encrypt(file_data)

                file_name = self.file_path.split('/')[-1]
                encrypted_file_name = file_name + '.encrypted'

                encrypted_files_dir = 'encrypted_files'
                if not os.path.exists(encrypted_files_dir):
                    os.makedirs(encrypted_files_dir)

                encrypted_file_path = os.path.join(encrypted_files_dir, encrypted_file_name)
                with open(encrypted_file_path, 'wb') as encrypted_file:
                    encrypted_file.write(encrypt_data)

                self.cursor.execute('''INSERT INTO encrypted_files (file_name, encrypt_data)
                                    VALUES (?, ?)''', (file_name, encrypt_data))
                self.conn.commit()
                messagebox.showinfo("Success", "File encrypted and saved successfully!")
        else:
            messagebox.showerror("Error", "No file selected!")

    def decrypt_file(self):
        encrypted_file_path = self.encrypted_file_path

        if encrypted_file_path:
            try:
                with open(encrypted_file_path, 'rb') as file:
                    file_data = file.read()
                    decrypt_data = self.fernet.decrypt(file_data)

                    file_name = os.path.splitext(os.path.basename(encrypted_file_path))[0]

                    decrypted_files_dir = 'decrypted_files'
                    if not os.path.exists(decrypted_files_dir):
                        os.makedirs(decrypted_files_dir)

                    decrypted_file_path = os.path.join(decrypted_files_dir, file_name)

                with open(decrypted_file_path, 'wb') as decrypted_file:
                    decrypted_file.write(decrypt_data)

                messagebox.showinfo("Success", "File decrypted and saved successfully!")
            except InvalidToken:
                messagebox.showerror("Error", "Invalid or corrupted data. Failed to decrypt file.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to decrypt file: {str(e)}")
        else:
            messagebox.showerror("Error", "No encrypted file path provided.")

    def choose_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            messagebox.showinfo("Success", "File selected successfully!")

if __name__ == "__main__":
    root = ctk.CTk()
    app = FileEncryptionTool(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()
