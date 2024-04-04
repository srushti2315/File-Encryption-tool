import customtkinter
from customtkinter import *
from PIL import Image

class sendmail:
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
        ##############        ##############        ##############         ##############
        self.email_frame = CTkFrame(self.main, width=600, height=800, border_width=2, border_color="black",fg_color="black")
        self.email_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.subject_label = CTkLabel(self.email_frame, text="Subject:")
        self.subject_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.subject_entry = CTkEntry(self.email_frame)
        self.subject_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

        self.message_label = CTkLabel(self.email_frame, text="")
        self.message_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.message_text = CTkTextbox(self.email_frame, height=200, width=250)
        self.message_text.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.send_button = CTkButton(self.email_frame, text="Send",font=("", 12, "bold"))
        self.send_button.grid(row=2, columnspan=2, pady=10)
        self.main.mainloop()

    def center_window(self):
        x = (self.main.winfo_reqwidth() - 200) 
        y = (self.main.winfo_reqheight() - 200) 
        self.main.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    sendmail()
