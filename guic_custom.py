import tkinter
import tkinter.messagebox
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        global dict_user
        dict_user = {"999999": "Administrator",
                     "888888": "Service Technician",
                     "111111": "Leroy Harreh",
                     "222222": "Tobias Graetzer",
                     "333333": "Bojan Resan"}
        super().__init__()

        # configure window
        self.title("Laser Configuration Utility")
        self.geometry(f"{1024}x{600}")
        self.overrideredirect(True)  # omits the taskbar on top of the window
        # self.deactivate_automatic_dpi_awareness()

        # configure grid layout (4x4)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        # self.grid_columnconfigure((2, 3, 4, 5, 6), weight=)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # create tabviews
        self.tabview = customtkinter.CTkTabview(self, width=1100, height=580)
        self.tabview.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.tabview.add("Sign In")
        self.tabview.add("Main")
        self.tabview.add("Graphs")
        self.tabview.add("Export")
        self.tabview.add("Settings")
        self.tabview.tab("Main").grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                                                      weight=1)  # configure grid of individual tabs
        self.tabview.tab("Sign In").grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                                                         weight=1)  # configure grid of individual tabs
        self.tabview.tab("Settings").grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                                                          weight=1)  # configure grid of individual tabs
        self.tabview.tab("Settings").grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # "Sign In"-tab
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="Sign In",
                                                           command=self.sign_in_button_event)
        self.string_input_button.grid(row=5, column=5)
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="Sign Out",
                                                           command=self.sign_in_button_event)
        self.string_input_button.grid(row=5, column=7)
        self.string_input_button_1 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="1",
                                                             command=self.sign_in_authent("1"), height=100, width=100)
        self.string_input_button_1.grid(row=1, column=5, padx=(10, 10), pady=(10, 10))
        self.string_input_button_2 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="2",
                                                             command=self.sign_in_authent("2"), height=100, width=100)
        self.string_input_button_2.grid(row=1, column=6, padx=(10, 10), pady=(10, 10))
        self.string_input_button_3 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="3",
                                                             command=self.sign_in_authent("3"), height=100, width=100)
        self.string_input_button_3.grid(row=1, column=7, padx=(10, 10), pady=(10, 10))
        self.string_input_button_4 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="4",
                                                             command=self.sign_in_authent("4"), height=100, width=100)
        self.string_input_button_4.grid(row=2, column=5, padx=(10, 10), pady=(10, 10))
        self.string_input_button_5 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="5",
                                                             command=self.sign_in_authent("5"), height=100, width=100)
        self.string_input_button_5.grid(row=2, column=6, padx=(10, 10), pady=(10, 10))
        self.string_input_button_6 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="6",
                                                             command=self.sign_in_authent("6"), height=100, width=100)
        self.string_input_button_6.grid(row=2, column=7, padx=(10, 10), pady=(10, 10))
        self.string_input_button_7 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="7",
                                                             command=self.sign_in_authent("7"), height=100, width=100)
        self.string_input_button_7.grid(row=3, column=5, padx=(10, 10), pady=(10, 10))
        self.string_input_button_8 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="8",
                                                             command=self.sign_in_authent("8"), height=100, width=100)
        self.string_input_button_8.grid(row=3, column=6, padx=(10, 10), pady=(10, 10))
        self.string_input_button_9 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="9",
                                                             command=self.sign_in_authent("9"), height=100, width=100)
        self.string_input_button_9.grid(row=3, column=7, padx=(10, 10), pady=(10, 10))
        self.string_input_button_0 = customtkinter.CTkButton(self.tabview.tab("Sign In"), text="0",
                                                             command=self.sign_in_authent("0"), height=100, width=100)
        self.string_input_button_0.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))

        # create main entry and button
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Main"), text="Logged in as:")
        self.appearance_mode_label.grid(row=0, column=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Main"), text=dict_user["999999"])  # below
        self.appearance_mode_label.grid(row=1, column=10)  # , padx=0, pady=0 logged in as dict entry

        progressbar = customtkinter.CTkProgressBar(master=self.tabview.tab("Main"),
                                                   width=160,
                                                   height=20,
                                                   border_width=5)
        progressbar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        value = 0.1
        progressbar.set(value)

        self.string_input_button_sign_in = customtkinter.CTkButton(self.tabview.tab("Main"), text="Enter",
                                                                   command=self.sign_in_button_event, anchor="center")
        self.string_input_button_sign_in.grid(row=7, column=0, padx=(10, 0), pady=(0, 0))

        self.entry_p = customtkinter.CTkEntry(self.tabview.tab("Main"), placeholder_text="P Parameter")
        self.entry_p.grid(row=1, column=0, columnspan=1, padx=(10, 0), pady=(0, 0))  # , sticky="nsew"
        self.entry_i = customtkinter.CTkEntry(self.tabview.tab("Main"), placeholder_text="I Parameter")
        self.entry_i.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(5, 0))  # , sticky="nsew"
        self.entry_d = customtkinter.CTkEntry(self.tabview.tab("Main"), placeholder_text="D Parameter")
        self.entry_d.grid(row=3, column=0, columnspan=1, padx=(10, 0), pady=(5, 0))  # , sticky="nsew"

        # configuration "settings"-tab
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Appearance Mode:")
        self.appearance_mode_label.grid(row=9, column=10, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=10, padx=20, pady=(10, 0))
        self.string_input_button_quit = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Quit",
                                                                command=self.quit, anchor="center")
        self.string_input_button_quit.grid(row=10, column=10)  # , padx=100, pady=(10, 10)

        # disabling widgets
        self.entry_p.configure(state="disabled")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sign_in_button_event(self):
        pass

    def sign_in_authent(self, digit):
        psw = ""
        print(digit)
        if len(psw) < 6:
            psw += digit
        try:
            if psw in dict_user:
                return True
        except KeyError:
            print("User name or password not wrong or user not existing")


if __name__ == "__main__":
    global app
    app = App()
    app.mainloop()
