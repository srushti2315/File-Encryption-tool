import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, Menu

from cryptography import fernet
from cryptography.fernet import Fernet
import sqlite3
from cryptography.fernet import InvalidToken
from tkinter import ttk
# from moviepy.editor import VideoFileClip
# from PIL import Image, ImageTk


# noinspection PyTypeChecker,PyUnresolvedReferences
class FileEncryptionTool:
    # noinspection PyUnresolvedReferences
    def __init__(self, root):
        self.encrypted_file_path = None
        self.root = root
        self.file_path = None
        self.root.title("File Encryption Tool")
        ctk.set_default_color_theme("MoonlitSky.json")

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(expand=True, fill='both')
        
        heading_label = ctk.CTkLabel(self.main_frame, text="Welcome to File Encryption Tool",font=('Helvetica', 24))
        heading_label.pack(pady=10)
        # Navbar
        self.create_navbar()

        # Heading
        

        self.tab_control = ttk.Notebook(self.main_frame)
        self.tab_control.pack(expand=True, fill='both')

        # Sender tab
        self.sender_tab = ctk.CTkFrame(self.tab_control)
        self.tab_control.add(self.sender_tab, text="Sender")

        # Receiver tab
        self.receiver_tab = ctk.CTkFrame(self.tab_control)
        self.tab_control.add(self.receiver_tab, text="Receiver")


        # Create sender tab
        self.create_sender_tab()

        # Create receiver tab
        self.create_receiver_tab()

        # Navbar
        # navbar_frame = ctk.CTkFrame(self.main_frame)
        # navbar_frame.pack(fill='x')
        #
        # heading_label = ctk.CTkLabel(navbar_frame, text="File Encryption Tool", font=('Helvetica', 18))
        # heading_label.pack(pady=10)

        # self.label = ctk.CTkLabel(root, text="Select a file to encrypt:")
        # self.label.pack(pady=10)

        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

        self.conn = sqlite3.connect("fileDB.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

        # self.create_buttons()

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
        # select_file_button = tk.Button(self.sender_tab, text="Select File", command=self.encrypt_file)
        # select_file_button.pack(pady=10)
        file_button = ctk.CTkButton(self.sender_tab, text="Select File", command=self.choose_file)
        file_button.pack(pady=10)

        encrypt_button = ctk.CTkButton(self.sender_tab, text="Encrypt", command=self.encrypt_file)
        encrypt_button.pack(pady=10)

        send_button = ctk.CTkButton(self.sender_tab, text="Send Encrypted File", command=self.send_encrypted_file)
        send_button.pack(pady=10)

    def create_receiver_tab(self):
        self.encrypted_file_path = tk.StringVar()
        encrypted_file_entry = tk.Entry(self.receiver_tab, textvariable=self.encrypted_file_path)
        encrypted_file_entry.pack(pady=10)

        self.decrypt_button = ctk.CTkButton(self.receiver_tab, text="Decrypt", command=self.decrypt_file)
        self.decrypt_button.pack(pady=10)

        # receive_button = tk.Button(self.receiver_tab, text="Receive and Decrypt File",
        #                            command=self.decrypt_file)
        # receive_button.pack(pady=10)

    def send_encrypted_file(self):
        # Retrieve encrypted file data from the database
        self.cursor.execute("SELECT encrypt_data FROM encrypted_files ORDER BY id DESC LIMIT 1")
        encrypted_file_data = self.cursor.fetchone()

        if encrypted_file_data:
            # Display the encrypted file data in the receiver's tab
            encrypted_data_label = tk.Label(self.receiver_tab, text="Encrypted File Data:")
            encrypted_data_label.pack(pady=10)

            encrypted_data_entry = tk.Entry(self.receiver_tab, width=50)
            encrypted_data_entry.insert(0, encrypted_file_data[0])
            encrypted_data_entry.pack(pady=10)

            decrypt_button = tk.Button(self.receiver_tab, text="Decrypt File",
                                       command=lambda: self.decrypt_file(encrypted_file_data[0]))
            decrypt_button.pack(pady=10)
        else:
            messagebox.showerror("Error", "No encrypted file found in the database.")

    def encrypt_file(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                encrypt_data = self.fernet.encrypt(file_data)
                file_name = self.file_path.split('/')[-1]
                self.cursor.execute('''INSERT INTO encrypted_files (file_name, encrypt_data)
                                    VALUES (?, ?)''', (file_name, encrypt_data))
                self.conn.commit()
                # self.label.configure(text="File encrypted and saved!")
                messagebox.showinfo("Success", "File encrypted and saved successfully!")

            with open('encrypted_file.dat', 'wb') as encrypted_file:
                encrypted_file.write(encrypt_data)
        else:
            # self.label.configure(text="No file selected!")
            messagebox.showerror("Error", f"Failed to encrypt file: {str(e)}")

    def decrypt_file(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                try:
                    decrypt_data = self.fernet.decrypt(file_data)

                    file_name = self.file_path.split('/')[-1]
                    self.cursor.execute('''INSERT INTO decrypted_files (file_name, decrypt_data)
                                        VALUES (?, ?)''', (file_name, decrypt_data))
                    self.conn.commit()
                    # self.label.configure(text="File decrypted and saved!")
                    messagebox.showinfo("Success", "File decrypted and saved successfully!")

                # except InvalidToken:
                #     self.label.configure(text="Error: Unable to decrypt file. Invalid or corrupted data.")

                except InvalidToken:
                    messagebox.showerror("Error", "Invalid or corrupted data. Failed to decrypt file.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to decrypt file: {str(e)}")

        else:
            # self.label.configure(text="No file selected!")
            messagebox.showerror("Error", "No File selected")

    def choose_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            # self.label.configure(text=f"selected File: {self.file_path}")
            messagebox.showinfo("Success", "File selected successfully!")




if __name__ == "__main__":
    root = ctk.CTk()
    app = FileEncryptionTool(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:

        root.destroy()
