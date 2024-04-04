import customtkinter
from customtkinter import *
from PIL import Image
import sender

class homepage:
    def __init__(self):
        self.main = CTk()
        self.main.title("Home Page")
        self.main.config(bg="white")
        
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()

        self.main.geometry(f"{screen_width}x{screen_height}")

        self.center_window()

        self.navbar = CTkFrame(self.main, height=50, fg_color="#121212")
        self.navbar.grid(row=0, column=0, sticky="ew")

        self.home_btn = CTkButton(self.navbar, text="Home", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.about_btn = CTkButton(self.navbar, text="About", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.about_btn.place(relx=0.4, rely=0.5, anchor="center")
        self.contact_btn = CTkButton(self.navbar, text="Contact Us", fg_color="black",height=40,border_width=2,border_color="#39FF14",font=("", 15, "bold"),hover_color="green")
        self.contact_btn.place(relx=0.6, rely=0.5, anchor="center")

        self.bg_img = CTkImage(dark_image=Image.open("assets/images/bg9.png"), size=(screen_width, screen_height))
        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.grid(row=1, column=0)
        tab_width = 800
        tab_height = 400
        tab_x = (screen_width - tab_width) / 2
        tab_y = (screen_height - tab_height) / 2
        self.tab = CTkTabview(self.main, width=tab_width, height=tab_height)
        self.tab.place(x=tab_x, y=tab_y)
        self.send_mail_btn = CTkButton(self.tab, text="SEND \nMESSAGE", width=280,height=80,border_width=4,border_color="purple",font=("Times New Roman", 25, "bold"),hover_color="#007C7A",fg_color="black",command=self.sendmail)
        self.send_mail_btn.place(relx=0.3, rely=0.5, anchor="center")
        self.Inbox_btn = CTkButton(self.tab, text="INBOX", fg_color="black",width=280,height=80,border_width=4,border_color="purple",font=("Times New Roman", 25, "bold"),hover_color="#007C7A")
        self.Inbox_btn.place(relx=0.7, rely=0.5, anchor="center")
        self.main.mainloop()

    def center_window(self):
        x = (self.main.winfo_reqwidth() - 200) 
        y = (self.main.winfo_reqheight() - 200) 
        self.main.geometry(f"+{x}+{y}")
    
    def sendmail(self):
        self.main.destroy()
        sender.sendmail()



if __name__ == "__main__":
    homepage()
