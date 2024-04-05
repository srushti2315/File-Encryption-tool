import customtkinter 
from customtkinter import *
from PIL import Image
from tkinter import filedialog, messagebox
import sqlite3
import os
from cryptography.fernet import InvalidToken
from cryptography import fernet
from cryptography.fernet import Fernet
import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import filedialog, messagebox, Menu
from PIL import Image
from cryptography import fernet
from cryptography.fernet import Fernet
import sqlite3
from cryptography.fernet import InvalidToken
import sqlite3
import os
import inbox


class InboxApp:
    def __init__(self, userinf="om"):
        self.main = CTk()
        self.main.title("Home Page")
        self.main.config(bg="white")
        self.userinf = userinf
        self.conn = sqlite3.connect("loginDB.db")
        self.cursor = self.conn.cursor()
        self.main.configure(fg_color="#121212")

        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()

        self.main.geometry(f"{screen_width}x{screen_height}")

        self.center_window()

        self.navbar = CTkFrame(self.main, height=50, fg_color="#121212", width=1600, border_width=2, border_color="purple")
        self.navbar.grid(row=0, columnspan=10, sticky="ew")

        self.home_btn = CTkButton(self.navbar, text="Home", fg_color="black", height=40, border_width=2, border_color="#39FF14", font=("", 15, "bold"), hover_color="green")
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.about_btn = CTkButton(self.navbar, text="About", fg_color="black", height=40, border_width=2, border_color="#39FF14", font=("", 15, "bold"), hover_color="green")
        self.about_btn.place(relx=0.4, rely=0.5, anchor="center")
        self.contact_btn = CTkButton(self.navbar, text="Contact Us", fg_color="black", height=40, border_width=2, border_color="#39FF14", font=("", 15, "bold"), hover_color="green")
        self.contact_btn.place(relx=0.6, rely=0.5, anchor="center")
        self.inbox_frame = CTkFrame(self.main, height=600, width=300, fg_color="blue", border_width=2, border_color="blue")
        self.inbox_frame.grid(row=2, column=0, sticky="w")
        self.main.grid_columnconfigure(0, weight=1)
        self.message_but = {}

        self.display_inbox()
        self.main.mainloop()

    def display_inbox(self):
        self.cursor.execute("SELECT senders_name, subject, message, attachment_name, attachment,key  FROM {}".format(self.userinf))
        messages = self.cursor.fetchall()
        a = 0
        for index, message in enumerate(messages, start=1):
            sender, subject, mes, attachment_name,attachment,key = message
            self.message_but[a] = CTkButton(self.inbox_frame, text=f"{index}. From: {sender}, Subject: {subject}", height=50, width=300, fg_color="black")
            self.message_but[a].grid(row=a, column=0, sticky="n")
            self.message_but[a].bind("<Button-1>", lambda event, msg=mes, attach=attachment, attach_name=attachment_name,key=key: self.message_frame(msg, attach, attach_name,key))

            a += 1

    def decrypt_attachment(self, attachment, attachment_name,key):
        encrypted_files_dir = 'encrypted_files'
        print(attachment)
        if not os.path.exists(encrypted_files_dir):
            os.makedirs(encrypted_files_dir)

        encrypted_file_path = os.path.join(encrypted_files_dir, attachment_name)
        with open(encrypted_file_path, 'wb') as encrypted_file:
                            encrypted_file.write(attachment)
        self.decrypt_file(encrypted_file_path,key)






    def decrypt_file(self,encryptedfilepath2,key):

        encrypted_file_path = encryptedfilepath2
        self.fernet = Fernet(key)
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
                
            

    def message_frame(self, message, attachment,attachment_name,key):
    
        message_frame = CTkFrame(self.main, fg_color="black", border_width=2, border_color="black")
        message_frame.grid(row=2, column=1, sticky="nsew")
        self.main.grid_rowconfigure(2, weight=200)
        self.main.grid_columnconfigure(1, weight=200)
    
        message_label = CTkLabel(message_frame, text=message, font=("", 20))
        message_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    
        if attachment:
            attachment_label = CTkLabel(message_frame, text=f"Attachment: {attachment_name}", font=("", 20))
            attachment_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
            decrypt_button = CTkButton(message_frame, text="Decrypt", command=lambda: self.decrypt_attachment(attachment,attachment_name,key))
            decrypt_button.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    def center_window(self):
        x = (self.main.winfo_reqwidth() - 200) 
        y = (self.main.winfo_reqheight() - 200) 
        self.main.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    userinf = "om" 
    app = InboxApp(userinf)