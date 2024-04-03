import customtkinter
from customtkinter import *
from PIL import Image

class LoginPage:
    def __init__(self):
        self.main = CTk()
        self.main.title("Login Page")
        self.main.config(bg="white")
        self.main.resizable(False, False)
        
        self.bg_img = CTkImage(dark_image=Image.open("assets/images/bg5.jpg"), size=(500, 500))

        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.grid(row=0, column=0)

        self.frame1 = CTkFrame(self.main, fg_color="#D9D9D9", bg_color="white", height=350, width=300, corner_radius=20)
        self.frame1.grid(row=0, column=1, padx=40)

        self.title = CTkLabel(self.frame1, text="Welcome Back! \nLogin to Account", text_color="black", font=("", 35, "bold"))
        self.title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

        self.usrname_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45)
        self.usrname_entry.grid(row=1, column=0, sticky="nwe", padx=30)

        self.passwd_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Password", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
        self.passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)

        self.cr_acc = CTkButton(self.frame1, text="Create Account!", fg_color="#0085FF", cursor="hand2", font=("", 15, "bold"), height=40, width=80, command=self.create_account)
        self.cr_acc.grid(row=3, column=0, sticky="w", pady=20, padx=40)

        self.l_btn = CTkButton(self.frame1, text="Login", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF", cursor="hand2",
                          corner_radius=15)
        self.l_btn.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        self.main.mainloop()
    
    def create_account(self):
        self.main.destroy()
        SignUpPage()

class SignUpPage:
    def __init__(self):
        self.root = CTk()
        self.root.title("Sign Up")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        
        bg_img = CTkImage(dark_image=Image.open("assets/images/bg5.jpg"), size=(500, 500))

        bg_lab = CTkLabel(self.root, image=bg_img, text="")
        bg_lab.grid(row=0, column=0)

        frame1 = CTkFrame(self.root, fg_color="#D9D9D9", bg_color="white", height=350, width=300, corner_radius=20)
        frame1.grid(row=0, column=1, padx=40)

        title = CTkLabel(frame1, text="Sign Up", text_color="black", font=("", 35, "bold"))
        title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)
        self.usrname_entry = CTkEntry(frame1, text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45)
        self.usrname_entry.grid(row=1, column=0, sticky="nwe", padx=30)

        self.passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Password", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
        self.passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30,pady=10)

        self.passwd_entry2 = CTkEntry(frame1, text_color="white", placeholder_text="Confirm Password", fg_color="black", placeholder_text_color="white",
                             font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
        self.passwd_entry2.grid(row=3, column=0, sticky="nwe", padx=30)


        self.cr_acc = CTkButton(frame1, text="Sign Up", fg_color="#0085FF", cursor="hand2", font=("", 15, "bold"), height=40, width=80, command=self.signup)
        self.cr_acc.grid(row=4, column=0, columnspan=3, sticky="n", pady=20, padx=10) 


        self.root.mainloop()
    def signup():
        pass



        

if __name__ == "__main__":
    LoginPage()
