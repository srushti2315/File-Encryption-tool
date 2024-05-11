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
import homepage
class sendmail:

    file_path=None
    file_data=None
    Userinf=None
    def __init__(self,Userinf):
        self.conn = sqlite3.connect("loginDB.db")
        self.cursor = self.conn.cursor()
        self.main = CTk()
        self.main.title("Home Page")
        self.main.config(bg="white")
        self.userinf=Userinf
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()

        self.main.geometry(f"{screen_width}x{screen_height}")

        self.center_window()

        self.navbar = CTkFrame(self.main, height=50, fg_color="#121212")
        self.navbar.grid(row=0, column=0, sticky="ew")

        self.home_btn = CTkButton(self.navbar, text="Home", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green",command=self.home)
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.about_btn = CTkButton(self.navbar, text="About", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.about_btn.place(relx=0.4, rely=0.5, anchor="center")
        self.contact_btn = CTkButton(self.navbar, text="Contact Us", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.contact_btn.place(relx=0.6, rely=0.5, anchor="center")

        self.bg_img = CTkImage(dark_image=Image.open("assets/images/bg9.png"), size=(screen_width, screen_height))
        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.grid(row=1, column=0)
        ##############        ##############        ##############         ##############
        self.email_frame = CTkFrame(self.main, width=1200, height=800, border_width=2, border_color="black",fg_color="black")
        self.email_frame.place(relx=0.25,rely=0.08)
        self.recipient_label = CTkLabel(self.email_frame, text="Recipient\nName:")
        self.recipient_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.recipient_entry = CTkEntry(self.email_frame,placeholder_text="Recipient Name",height=40)
        self.recipient_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        self.subject_label = CTkLabel(self.email_frame, text="Subject:")
        self.subject_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.subject_entry = CTkEntry(self.email_frame,placeholder_text="Subject Name",width=700,height=40)
        self.subject_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.message_text = CTkTextbox(self.email_frame, height=530, width=300)
        self.message_text.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        self.send_button = CTkButton(self.email_frame, text="Send",font=("", 17, "bold"),height=40,width=280,command=self.send_file)
        self.send_button.grid(row=3, column=1, pady=10)
        self.send_button.place(relx=0.55,rely=0.91)
        self.attachment_button = CTkButton(self.email_frame, text="Attachment",font=("", 17, "bold"),height=40,width=280,command=self.choose_file)
        self.attachment_button.grid(row=3,column=1,pady=10)
        self.attachment_button.place(relx=0.15, rely=0.91)
        self.blank_label = CTkLabel(self.email_frame, text="")
        self.blank_label.grid(row=3, column=0, sticky="w", padx=10, pady=20)

        self.main.mainloop()

    def center_window(self):
        x = (self.main.winfo_reqwidth() - 200) 
        y = (self.main.winfo_reqheight() - 200) 
        self.main.geometry(f"+{x}+{y}")
    def choose_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            messagebox.showinfo("Success", "File selected successfully!")
    def home(self):
         self.main.destroy()
         homepage.homepage(self.userinf)
    
    def send_file(self):
        sendersname=self.recipient_entry.get()
        subject=self.subject_entry.get()
        text=self.message_text.get(0.0,'end')
        self.enc,self.attachent_name=self.encrypt_file()
        self.cursor.execute('''INSERT INTO {}
                           (senders_name, subject, message,attachment_name,attachment,key)
                           VALUES (?, ?, ?, ?, ?, ?)'''.format(sendersname), 
                           (self.userinf, subject,text,self.attachent_name,self.enc,self.key))
        self.conn.commit()
        messagebox.showinfo("Success", "Message sent successfully!")


    def encrypt_file(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
                encrypt_data = self.fernet.encrypt(file_data)

                file_name = self.file_path.split('/')[-1]
                encrypted_file_name = file_name + '.encrypted'
                
                return encrypt_data,encrypted_file_name
        
                # encrypted_files_dir = 'encrypted_files'
                # if not os.path.exists(encrypted_files_dir):
                #     os.makedirs(encrypted_files_dir)

                # encrypted_file_path = os.path.join(encrypted_files_dir, encrypted_file_name)
                # with open(encrypted_file_path, 'wb') as encrypted_file:
                #     encrypted_file.write(encrypt_data)

                



if __name__ == "__main__":
    sendmail()
