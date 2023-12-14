import customtkinter
import example


mt = example.MeerstetterTEC()

# Colour schemes of the application
customtkinter.set_appearance_mode("System")
customtkinter.set_appearance_mode("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Laser Configuration Utility")
        self.geometry("1000x600")
        
        # Definie the tab configuration
        signin, overview, settings = "Sign In", "Overview", "Settings"
        self.tabview = customtkinter.CTkTabview(self, width=1000, height=580)
        self.tabview.grid(row=0, column=1, padx=(0, 0), pady=(0, 0))
        self.tabview.add(signin)
        self.tabview.add(overview)
        self.tabview.add(settings)
        
        self.tabview.tab(overview).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.tabview.tab(overview).grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.tabview.tab(settings).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        # Design Sign In tab
        
        # Design Overview tab
        self.button_increase = customtkinter.CTkButton(self.tabview.tab(overview), text="+", command=self.increase_button_event, height=30, width=30)
        self.button_increase.grid(row=1, column=2, padx=0, pady=0)
        
        self.button_decrease = customtkinter.CTkButton(self.tabview.tab(overview), text="-", command=self.decrease_button_event, height=30, width=30)
        self.button_decrease.grid(row=1, column=4, padx=0, pady=0)

        self.ch1_temp_av = customtkinter.CTkLabel(self.tabview.tab(overview), text=f'{mt.get_data()["object temperature"][0]:.3f}', font=("Arial", 25))
        self.ch1_temp_av.grid(row=1, column=1, padx=(0, 0), pady=(0, 0))
        
        self.ch1_temp_sp = customtkinter.CTkLabel(self.tabview.tab(overview), text=f'{mt.get_data()["target object temperature"][0]:.3f}', font=("Arial", 25))
        self.ch1_temp_sp.grid(row=1, column=3, padx=(0, 0), pady=(0, 0))
        
        self.button_increase = customtkinter.CTkButton(self.tabview.tab(overview), text="+", command=self.increase_button_event, height=30, width=30)
        self.button_increase.grid(row=2, column=2, padx=0, pady=0)
        
        self.button_decrease = customtkinter.CTkButton(self.tabview.tab(overview), text="-", command=self.decrease_button_event, height=30, width=30)
        self.button_decrease.grid(row=2, column=4, padx=0, pady=0)

        self.ch1_temp_av = customtkinter.CTkLabel(self.tabview.tab(overview), text=f'{mt.get_data()["object temperature"][0]:.3f}', font=("Arial", 25))
        self.ch1_temp_av.grid(row=2, column=1, padx=(0, 0), pady=(0, 0))
        
        self.ch1_temp_sp = customtkinter.CTkLabel(self.tabview.tab(overview), text=f'{mt.get_data()["target object temperature"][0]:.3f}', font=("Arial", 25))
        self.ch1_temp_sp.grid(row=2, column=3, padx=(0, 0), pady=(0, 0))

        # Design Settings tab
        # self.button_dialog = customtkinter.CTkButton(self.tabview.tab(settings), text="Dialog", command=self.button_click_event)
        # self.button_dialog.grid(row=0, column=0, padx=20, pady=20)

        self.button2 = customtkinter.CTkButton(self.tabview.tab(settings), text="my button", command=self.button_callbck)
        self.button2.grid(row=1, column=1, padx=0, pady=0)

        self.quit = customtkinter.CTkButton(self.tabview.tab(settings), text="Quit", command=self.quit)
        self.quit.grid(row=8, column=8, padx=0, pady=0)

        # Updating of all the changing values
        self.ch1_temp_av.after(1000, self.update_ch1_temp_av)
        self.ch1_temp_sp.after(1000, self.update_ch1_temp_sp)

    def button_click_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
        print("Number:", dialog.get_input())
    def sign_in_button_event(self):
        pass
        
    def button_callbck(self):
        mt.set_temp(mt.get_data()["target object temperature"][0]+1.0)

    def increase_button_event(self):  # , widget
        mt.set_temp(mt.get_data()["target object temperature"][0]+1.0)
        
    def decrease_button_event(self):  # , widget
        mt.set_temp(mt.get_data()["target object temperature"][0]-1.0)
        
    def update_ch1_temp_av(self):
        self.ch1_temp_av.configure(text=f'{mt.get_data()["object temperature"][0]:.3f}')
        self.ch1_temp_av.after(1000, self.update_ch1_temp_av)
        
    def update_ch1_temp_sp(self):
        self.ch1_temp_sp.configure(text=f'{mt.get_data()["target object temperature"][0]:.3f}')
        self.ch1_temp_sp.after(1000, self.update_ch1_temp_sp)


app = App()
app.mainloop()
