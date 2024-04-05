import customtkinter 
from customtkinter import *
from PIL import Image
from tkinter import filedialog, messagebox
import sqlite3
class InboxApp:
    def __init__(self, userinf):
        self.main = CTk()
        self.main.title("Home Page")
        self.main.config(bg="white")
        self.userinf=userinf
        self.conn = sqlite3.connect("loginDB.db")
        self.cursor = self.conn.cursor()

        self.main.configure(fg_color="#121212")

        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()

        self.main.geometry(f"{screen_width}x{screen_height}")

        self.center_window()

        self.navbar = CTkFrame(self.main, height=50, fg_color="#121212",width=1600,border_width=2,border_color="purple")
        self.navbar.grid(row=0,columnspan=10 ,sticky="ew")

        self.home_btn = CTkButton(self.navbar, text="Home", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.about_btn = CTkButton(self.navbar, text="About", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.about_btn.place(relx=0.4, rely=0.5, anchor="center")
        self.contact_btn = CTkButton(self.navbar, text="Contact Us", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.contact_btn.place(relx=0.6, rely=0.5, anchor="center")
        self.inbox_frame = CTkFrame(self.main,height=600,width=300,fg_color="blue")
        self.inbox_frame.grid(row=2, column=0, sticky="w")
        self.main.grid_columnconfigure(0, weight=1)

        self.display_inbox()
        self.main.mainloop()

    def display_inbox(self):
        self.cursor.execute("SELECT senders_name, subject, message, attachment_name  FROM {}".format(self.userinf))
        messages = self.cursor.fetchall()
        a = 0
        for index, message in enumerate(messages, start=1):
            sender, subject, mes, attachment_name = message
            message_label = CTkLabel(self.inbox_frame, text=f"{index}. From: {sender}, Subject: {subject}", height=50, width=300, fg_color="black")
            message_label.grid(row=a, column=0, sticky="w")
            a += 1



        



        

    def center_window(self):
        x = (self.main.winfo_reqwidth() - 200) 
        y = (self.main.winfo_reqheight() - 200) 
        self.main.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    userinf = "om" 
    app = InboxApp(userinf)
