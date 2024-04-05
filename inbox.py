import customtkinter
from customtkinter import *
from PIL import Image
from tkinter import filedialog, messagebox
import sqlite3
class InboxApp:
    def __init__(self, userinf):
        self.userinf = userinf
        self.root = CTk()
        self.root.title("Inbox")
        
        self.conn = sqlite3.connect("loginDB.db")
        self.cursor = self.conn.cursor()

        self.inbox_frame = CTkFrame(self.root)
        self.inbox_frame.pack()


        self.display_inbox()

        self.root.mainloop()

    def display_inbox(self):
        self.cursor.execute("SELECT senders_name, subject, message, attachment_name  FROM {}".format(self.userinf))
        messages = self.cursor.fetchall()

        for index, message in enumerate(messages, start=1):
            sender, subject, mes, attachment_name  = message
            message_label = CTkLabel(self.inbox_frame, text=f"{index}. From: {sender}, Subject: {subject}")
            message_label.pack()
        
        
    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    userinf = "om" 
    app = InboxApp(userinf)
