import tkinter
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import authentication as auth
import time
import asyncio
import websockets
import websocket_server_random as websra

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Laser Configuration Utility")
        self.geometry(f"{1024}x{600}")
        # self.overrideredirect(True)  # omits the taskbar on top of the window
        # self.deactivate_automatic_dpi_awareness()

        # configure grid layout (4x4)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        # self.grid_columnconfigure((2, 3, 4, 5, 6), weight=)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # create tabviews
        signin, overview, cristal, diode, export, settings = "Sign In", "Overview", "Cristal", \
            "Diode", "Export", "Settings"

        self.tabview = customtkinter.CTkTabview(self, width=1100, height=580)
        self.tabview.grid(row=0, column=1, padx=(0, 0), pady=(0, 0))  # , sticky="nsew"
        self.tabview.add(signin)
        self.tabview.add(overview)
        self.tabview.add(cristal)
        self.tabview.add(diode)
        self.tabview.add(export)
        self.tabview.add(settings)

        self.tabview.tab(signin).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), weight=1)
        self.tabview.tab(overview).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.tabview.tab(cristal).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.tabview.tab(diode).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.tabview.tab(export).grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), weight=1)
        self.tabview.tab(settings).grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # create / configuration "Sign In"-tab
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab(signin), text=signin, command=None)
        self.string_input_button.grid(row=5, column=5)
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab(signin), text="Sign Out", command=None)
        self.string_input_button.grid(row=5, column=7)
        self.string_input_button_1 = customtkinter.CTkButton(self.tabview.tab(signin), text="1",
                                                             command=auth.sign_in_button_event_1, height=100, width=100)
        self.string_input_button_1.grid(row=1, column=5, padx=(10, 10), pady=(10, 10))
        self.string_input_button_2 = customtkinter.CTkButton(self.tabview.tab(signin), text="2",
                                                             command=auth.sign_in_button_event_2, height=100, width=100)
        self.string_input_button_2.grid(row=1, column=6, padx=(10, 10), pady=(10, 10))
        self.string_input_button_3 = customtkinter.CTkButton(self.tabview.tab(signin), text="3",
                                                             command=auth.sign_in_button_event_3, height=100, width=100)
        self.string_input_button_3.grid(row=1, column=7, padx=(10, 10), pady=(10, 10))
        self.string_input_button_4 = customtkinter.CTkButton(self.tabview.tab(signin), text="4",
                                                             command=auth.sign_in_button_event_4, height=100, width=100)
        self.string_input_button_4.grid(row=2, column=5, padx=(10, 10), pady=(10, 10))
        self.string_input_button_5 = customtkinter.CTkButton(self.tabview.tab(signin), text="5",
                                                             command=auth.sign_in_button_event_5, height=100, width=100)
        self.string_input_button_5.grid(row=2, column=6, padx=(10, 10), pady=(10, 10))
        self.string_input_button_6 = customtkinter.CTkButton(self.tabview.tab(signin), text="6",
                                                             command=auth.sign_in_button_event_6, height=100, width=100)
        self.string_input_button_6.grid(row=2, column=7, padx=(10, 10), pady=(10, 10))
        self.string_input_button_7 = customtkinter.CTkButton(self.tabview.tab(signin), text="7",
                                                             command=auth.sign_in_button_event_7, height=100, width=100)
        self.string_input_button_7.grid(row=3, column=5, padx=(10, 10), pady=(10, 10))
        self.string_input_button_8 = customtkinter.CTkButton(self.tabview.tab(signin), text="8",
                                                             command=auth.sign_in_button_event_8, height=100, width=100)
        self.string_input_button_8.grid(row=3, column=6, padx=(10, 10), pady=(10, 10))
        self.string_input_button_9 = customtkinter.CTkButton(self.tabview.tab(signin), text="9",
                                                             command=auth.sign_in_button_event_9, height=100, width=100)
        self.string_input_button_9.grid(row=3, column=7, padx=(10, 10), pady=(10, 10))
        self.string_input_button_0 = customtkinter.CTkButton(self.tabview.tab(signin), text="0",
                                                             command=auth.sign_in_button_event_0, height=100, width=100)
        self.string_input_button_0.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))

        # create / configuration "Overview"-tab
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab(overview), text="Logged in as:")
        self.appearance_mode_label.grid(row=0, column=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab(overview), text="Larry")
        self.appearance_mode_label.grid(row=1, column=10)

        self.string_input_button_sign_in = customtkinter.CTkButton(self.tabview.tab(overview), text="Enter",
                                                                   command=None, anchor="center")
        self.string_input_button_sign_in.grid(row=7, column=0, padx=(10, 10), pady=(0, 0))

        self.entry_p = customtkinter.CTkEntry(self.tabview.tab(overview), placeholder_text="P Parameter")
        self.entry_p.grid(row=1, column=0, columnspan=1, padx=(10, 0), pady=(0, 0))
        self.random_value = customtkinter.CTkLabel(self.tabview.tab(overview), text=self.main_websocket())
        self.random_value.grid(row=0, column=2)
        self.entry_i = customtkinter.CTkEntry(self.tabview.tab(overview), placeholder_text="I Parameter")
        self.entry_i.grid(row=2, column=0, columnspan=1, padx=(10, 0), pady=(5, 0))
        self.entry_d = customtkinter.CTkEntry(self.tabview.tab(overview), placeholder_text="D Parameter")
        self.entry_d.grid(row=3, column=0, columnspan=1, padx=(10, 0), pady=(5, 0))

        # create / configuration "settings"-tab
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab(settings), text="Appearance Mode:")
        self.appearance_mode_label.grid(row=9, column=10, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab(settings),
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=10, padx=20, pady=(10, 0))

        self.string_input_button_quit = customtkinter.CTkButton(self.tabview.tab(settings), text="Quit",
                                                                command=self.quit, anchor="center")
        self.string_input_button_quit.grid(row=10, column=10)

        # disabling widgets
        self.entry_p.configure(state="disabled")
        # self.random_value.configure(text=self.randomisiert())
        # self.after(500, self.main_websocket())

        asyncio.run(self.main_websocket())

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def randomisiert(self):
        time.sleep(1)
        self.random_value = "{random.randint(0, 100)}"

    async def main_websocket(self):
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            print(f"Websocket on {uri} connected")
            response = await websocket.recv()
            # print(response)
            self.random_value.configure(text=response)


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # app.main_websocket()
