import customtkinter
from customtkinter import *
from PIL import Image
from tkinter import filedialog, messagebox
import sqlite3

class SenderPage:
    def __init__(self):
        self.main = CTk()
        self.main.title("Sender Page")
        self.main.config(bg="white")
        self.main.resizable(False, False)
       
        
        # self.bg_img = CTkImage(dark_image=Image.open("assets/images/hyy.png"), size=(50, 50))

        # self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        # self.bg_lab.grid(row=0, column=0)

        self.frame1 = CTkFrame(self.main, fg_color="#D9D9D9", bg_color="white", height=500, width=500, corner_radius=20)
        self.frame1.grid(row=0, column=0, padx=10)

        self.title = CTkLabel(self.frame1, text="Welcome \nLogin to Account", text_color="black", font=("", 35, "bold"))
        self.title.grid(row=0, column=0, sticky="nw", pady=20, padx=10)

        self.sender_label = CTkLabel(self.main, text="From:", font=("", 12, "bold"),width=100, corner_radius=15, height=40)
        self.sender_label.grid(row=0, column=0, padx=30, pady=10,sticky="w")
        self.receiver_label = CTkLabel(self.main, text="To:", font=("", 12, "bold"), width=100, corner_radius=15, height=40)
        self.receiver_label.grid(row=1, column=0, padx=30, pady=10, sticky="w")
        self.message_label = CTkLabel(self.main, text="Message:", font=("", 12, "bold"), width=100, corner_radius=15, height=40)
        self.message_label.grid(row=2, column=0, padx=30, pady=1, sticky="w")
       
        self.sender_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Your Name", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=40)
        self.sender_entry.grid(row=1, column=1, sticky="nwe", padx=30)

        
        
        self.receiver_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Receiver's Username", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45)
        self.receiver_entry.grid(row=2, column=1, sticky="nwe", padx=30, pady=20)

        
        self.message_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Receiver's Username", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45)
        self.message_entry.grid(row=3, column=1, sticky="nwe", padx=30, pady=10)

        self.choose_file_button = CTkButton(self.main, text="Choose File", font=("", 12), fg_color="#0085FF", bg_color="white", cursor="hand2", command=self.choose_file)
        self.choose_file_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.send_button = CTkButton(self.main, text="Send", font=("", 12), fg_color="#0085FF", bg_color="white", cursor="hand2", command=self.send_message)
        self.send_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.inbox_button = CTkButton(self.main, text="Inbox", font=("", 12), fg_color="#0085FF", bg_color="white", cursor="hand2", command=self.open_inbox)
        self.inbox_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.main.geometry("900x900")
        self.main.mainloop()

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        # Handle the selected file as needed

    def send_message(self):
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        message = self.message_text.get()
        # Save the message in the receiver's user table in the database
        # Encrypt and save the file in the receiver's inbox

    def open_inbox(self):
        # Implement functionality to open the receiver's inbox
        pass

if __name__ == "__main__":
    SenderPage()
