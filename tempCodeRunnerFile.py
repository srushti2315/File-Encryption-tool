 
        self.bg_img = CTkImage(dark_image=Image.open("assets/images/hyy.png"), size=(50, 50))

        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.grid(row=0, column=0)
