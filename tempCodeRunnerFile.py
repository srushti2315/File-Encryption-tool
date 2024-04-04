        tab_width = 800
        tab_height = 400
        tab_x = (screen_width - tab_width) / 2
        tab_y = (screen_height - tab_height) / 2
        self.tab = customtkinter.CTkTabview(self.main, width=tab_width, height=tab_height, fg_color="green")
        self.tab.place(x=tab_x, y=tab_y)