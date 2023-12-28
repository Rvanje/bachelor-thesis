import customtkinter

import tec_control as tec_ctrl

import os

import threading

from gpiozero import CPUTemperature

import numpy as np

# Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler  # I.O.
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
#     NavigationToolbar2Tk)
# from matplotlib.figure import Figure

# Colour schemes of the application
customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class WidgetDesign: pass


class WidgetFunction: pass


class GUI(customtkinter.CTk):

    def __init__(self, pixtend=None):
        super().__init__()
        self.title("Laser Configuration Utility")
        self.geometry("1000x600")
        self.ldd_current_av = None
        self.mt_1 = tec_ctrl.MeerstetterTEC(channel=1)
        self.mt_2 = tec_ctrl.MeerstetterTEC(channel=2)
        # self.slider_mode = "disabled"
        # self.cpu_temp_av = None  # f'{round(CPUTemperature().temperature,1)}°C'

        # Definie the tab configuration
        signin, overview, settings = "Sign In", "Overview", "Settings"
        self.tabview = customtkinter.CTkTabview(
            self, width=1000, height=580
        )
        self.tabview.grid(
            row=0,
            column=1,
            padx=(0, 0),
            pady=(0, 0)
        )

        # self.tabview.add(signin)
        self.tabview.add(overview)
        self.tabview.add(settings)

        # Characteristics of the tabs
        self.tabview.tab(overview).grid_columnconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            weight=1
        )
        self.tabview.tab(overview).grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            weight=1
        )
        self.tabview.tab(settings).grid_columnconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            weight=1
        )
        self.tabview.tab(settings).grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            weight=1
        )

        # Design "Sign In" tab

        # Design "Overview" tab
        self.sidebar_frame1 = customtkinter.CTkFrame(
            self.tabview.tab(overview),
            width=900,
            height=40,
            fg_color="grey80",
            corner_radius=5
        )
        self.sidebar_frame1.grid(
            row=1,
            column=1,
            padx=10,
            pady=(10, 0),
            sticky="nsew"
        )
        self.sidebar_frame1.grid_rowconfigure(4, weight=1)

        self.sidebar_frame2 = customtkinter.CTkFrame(
            self.tabview.tab(overview),
            width=900,
            height=40,
            fg_color="grey80",
            corner_radius=5
        )
        self.sidebar_frame2.grid(
            row=2,
            column=1,
            padx=10,
            pady=(10, 0),
            sticky="nsew"
        )
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        self.sidebar_frame3 = customtkinter.CTkFrame(
            self.tabview.tab(overview),
            width=900,
            height=40,
            fg_color="grey80",
            corner_radius=5
        )
        self.sidebar_frame3.grid(
            row=3,
            column=1,
            padx=10,
            pady=(10, 0),
            sticky="nsew"
        )
        self.sidebar_frame3.grid_rowconfigure(4, weight=1)

        # Channel 1 Properties
        self.ch1_label = customtkinter.CTkLabel(
            self.sidebar_frame1,
            text=f'TEC Channel 1',
            font=("Arial", 25)
        )
        self.ch1_label.grid(row=0,
                            column=0,
                            padx=(5, 0),
                            pady=(0, 0),
                            sticky="w"
                            )
        self.ch1_temp_av = customtkinter.CTkLabel(
            self.sidebar_frame1,
            text=f'{self.mt_1.get_data()["object temperature"][0]:.3f}°C',
            font=("Arial", 22)
        )
        self.ch1_temp_av.grid(
            row=1,
            column=0,
            padx=(5, 0),
            pady=(0, 0),
            sticky="w"
        )

        self.ch1_temp_sp = customtkinter.CTkLabel(
            self.sidebar_frame1,
            text=f'{self.mt_1.get_data()["target object temperature"][0]:.3f}°C',
            font=("Arial", 22),
        )
        self.ch1_temp_sp.grid(
            row=1,
            column=2,
            padx=(0, 0),
            pady=(0, 0),
            sticky="w"
        )

        self.ch1_button_increase = customtkinter.CTkButton(
            self.sidebar_frame1,
            text="+", command=self.ch1_increase_button_event,
            height=30,
            width=30,
        )
        self.ch1_button_increase.grid(
            row=1,
            column=3,
            padx=10,
            pady=0,
            sticky="w"
        )

        self.ch1_button_decrease = customtkinter.CTkButton(
            self.sidebar_frame1,
            text="-",
            command=self.ch1_decrease_button_event,
            height=30,
            width=30
        )
        self.ch1_button_decrease.grid(
            row=1,
            column=3,
            padx=50,
            pady=0
        )

        # Channel 2 Properties
        self.ch2_label = customtkinter.CTkLabel(
            self.sidebar_frame2,
            text=f'TEC Channel 2',
            font=("Arial", 25)
        )
        self.ch2_label.grid(row=0,
                            column=0,
                            padx=(5, 0),
                            pady=(0, 0),
                            sticky="w"
                            )

        self.ch2_temp_av = customtkinter.CTkLabel(
            self.sidebar_frame2,
            text=f'{self.mt_2.get_data()["object temperature"][0]:.3f}°C',
            font=("Arial", 22)
        )
        self.ch2_temp_av.grid(
            row=1,
            column=0,
            padx=(5, 0),
            pady=(0, 0),
            sticky="w"
        )

        self.ch2_temp_sp = customtkinter.CTkLabel(
            self.sidebar_frame2,
            text=f'{self.mt_2.get_data()["target object temperature"][0]:.3f}°C',
            font=("Arial", 22)
        )
        self.ch2_temp_sp.grid(
            row=1,
            column=2,
            padx=(0, 0),
            pady=(0, 0),
            sticky="w"
        )

        self.ch2_button_increase = customtkinter.CTkButton(
            self.sidebar_frame2,
            text="+", command=self.ch2_increase_button_event,
            height=30,
            width=30
        )
        self.ch2_button_increase.grid(
            row=1,
            column=3,
            padx=10,
            pady=0,
            sticky="w"
        )

        self.ch2_button_decrease = customtkinter.CTkButton(
            self.sidebar_frame2,
            text="-",
            command=self.ch2_decrease_button_event,
            height=30,
            width=30
        )
        self.ch2_button_decrease.grid(
            row=1,
            column=3,
            padx=50,
            pady=0,
            sticky="w"
        )

        # Laser Beam bar Properties
        self.ch2_label = customtkinter.CTkLabel(
            self.sidebar_frame3,
            text=f'LDD Laser Settings',
            font=("Arial", 25)
        )
        self.ch2_label.grid(row=0,
                            column=0,
                            padx=(5, 0),
                            pady=(0, 0),
                            sticky="w"
                            )

        self.ldd_current_av = customtkinter.CTkLabel(
            self.sidebar_frame3,
            text=f'{self.ldd_current_av}A',
            font=("Arial", 22)
        )
        self.ldd_current_av.grid(
            row=1,
            column=0,
            padx=(5, 0),
            pady=(0, 0),
            sticky="w"
        )

        self.ldd_current_sp = customtkinter.CTkLabel(
            self.sidebar_frame3,
            text=f'{None}A',
            font=("Arial", 22)
        )
        self.ldd_current_sp.grid(
            row=1,
            column=2,
            padx=(0, 0),
            pady=(0, 0),
            sticky="w"
        )

        self.ldd_current_increase = customtkinter.CTkButton(
            self.sidebar_frame3,
            text="+",
            command=self.ldd_increase_button_event,
            height=30,
            width=30
        )
        self.ldd_current_increase.grid(
            row=1,
            column=3,
            padx=10,
            pady=0,
            sticky="w"
        )

        self.ldd_current_decrease = customtkinter.CTkButton(
            self.sidebar_frame3,
            text="-",
            command=self.ldd_decrease_button_event,
            height=30,
            width=30
        )
        self.ldd_current_decrease.grid(
            row=1,
            column=3,
            padx=50,
            pady=0,
            sticky="w"
        )

        self.laser_beam_bar = customtkinter.CTkSlider(
            self.sidebar_frame3,
            from_=0,
            to=1
        )
        self.laser_beam_bar.grid(
            row=2,
            column=0,
            padx=(5, 0),
            pady=(10, 10),
            rowspan=1
        )

        # Design Settings tab
        # self.button_dialog = customtkinter.CTkButton(
        # self.tabview.tab(settings),
        #  text="Dialog",
        #   command=self.button_click_event
        # )
        # self.button_dialog.grid(row=0, column=0, padx=20, pady=20)
        # CPU Temperature
        self.cpu_temp_av_label = customtkinter.CTkLabel(
            self.tabview.tab(settings),
            text="CPU Temperature:",
            anchor="w"
        )
        self.cpu_temp_av_label.grid(
            row=7,
            column=0,
            padx=20,
            pady=(0, 0)
        )

        self.cpu_temp_av = customtkinter.CTkLabel(
            self.tabview.tab(settings),
            text=f"{CPUTemperature().temperature:.3f}",
            anchor="w"
        )
        self.cpu_temp_av.grid(
            row=7,
            column=0,
            padx=20,
            pady=(40, 0)
        )

        # Appearance mode properties
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.tabview.tab(settings),
            text="Appearance Mode:",
            anchor="w"
        )
        self.appearance_mode_label.grid(
            row=9,
            column=0,
            padx=20,
            pady=(0, 0)
        )
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.tabview.tab(settings),
            values=["Light", "Dark"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionemenu.grid(
            row=9,
            column=0,
            padx=20,
            pady=(50, 0)
        )

        self.quiter = customtkinter.CTkButton(
            self.tabview.tab(settings),
            text="Quit",
            command=self.quit  # self.shut_down
        )
        self.quiter.grid(
            row=8,
            column=8,
            padx=0,
            pady=0
        )
        self.shut_down = customtkinter.CTkButton(
            self.tabview.tab(settings),
            text="Shut down",
            command=self.shut_down_button_event  # self.shut_down
        )
        self.shut_down.grid(
            row=9,
            column=8,
            padx=0,
            pady=0
        )

        # temperatur configurations
        self.ch1_temp_av.configure(
            text=f'{self.mt_2.get_data()["target object temperature"][0]:.3f}°C'
        )
        self.ch2_temp_av.configure(
            text=f'{self.mt_2.get_data()["target object temperature"][0]:.3f}°C'
        )
        self.cpu_temp_av.configure(
            text=f'{CPUTemperature().temperature:.3f}°C'
        )

        if __name__ != "__main__":
            self.quiter.configure(state="disabled")

        if __name__ != "__main__":
            self.shut_down.configure(state="enabled")

    def sign_in_button_event(self):
        pass

    def ch1_increase_button_event(self):
        self.mt_1.set_temp(
            self.mt_1.get_data()["target object temperature"][0] + 1.0
        )

    def ch1_decrease_button_event(self):
        self.mt_1.set_temp(
            self.mt_1.get_data()["target object temperature"][0] - 1.0
        )

    def ch2_increase_button_event(self):
        self.mt_2.set_temp(
            self.mt_2.get_data()["target object temperature"][0] + 1.0
        )

    def ch2_decrease_button_event(self):
        self.mt_2.set_temp(
            self.mt_2.get_data()["target object temperature"][0] - 1.0
        )

    def update_ch1_temp_av(self):
        self.ch1_temp_av.configure(
            text=f'{self.mt_1.get_data()["object temperature"][0]:.3f}°C'
        )
        self.ch1_temp_av.after(1000, self.update_ch1_temp_av)

    def update_ch1_temp_sp(self):
        self.ch1_temp_sp.configure(
            text=f'{self.mt_1.get_data()["target object temperature"][0]:.3f}°C'
        )
        self.ch1_temp_sp.after(1000, self.update_ch1_temp_sp)

    def update_ch2_temp_av(self):
        self.ch2_temp_av.configure(
            text=f'{self.mt_2.get_data()["object temperature"][0]:.3f}°C'
        )
        self.ch2_temp_av.after(1000, self.update_ch2_temp_av)

    def update_ch2_temp_sp(self):
        self.ch2_temp_sp.configure(
            text=f'{self.mt_2.get_data()["target object temperature"][0]:.3f}°C'
        )
        self.ch2_temp_sp.after(1000, self.update_ch2_temp_sp)

    def update_ldd_current_av(self):
        self.ldd_current_av = None

    def ldd_increase_button_event(self):
        pass

    def ldd_decrease_button_event(self):
        pass

    def laser_go_button_event(self):
        if self.laser_beam_bar.get() != 1:
            self.laser_go.configure(state="disable")
        else:
            self.laser_go.configure(state="normal")
        self.laser_beam_bar.after(100, self.laser_go_button_event)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def cpu_temp(self):
        self.cpu_temp_av.configure(
            text=f'{CPUTemperature().temperature:.3f}°C'
        )
        self.cpu_temp_av.after(2000, self.cpu_temp)

    def shut_down_button_event(self):
        os.system("sudo shutdown")

    def update_gui(self):
        # threading.Lock().acquire()
        self.update_ch1_temp_av()
        self.update_ch1_temp_sp()
        self.update_ch2_temp_av()
        self.update_ch2_temp_sp()
        self.update_ldd_current_av()
        # self.laser_go_button_event()
        self.cpu_temp()
        # threading.Lock().release()


if __name__ == "__main__":
    # Initialising the GUI
    app = GUI()
    threaded_task = threading.Thread(target=app.update_gui())
    threaded_task.start()

    # Starting the mainloop of the GUI
    app.mainloop()
