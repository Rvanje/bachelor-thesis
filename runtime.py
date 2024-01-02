from gui_custom import GUI

import threading

# from pixtend_communication import PIXC

import RPi.GPIO as GPIO

def main_loop():
    lock.acquire()
    gui.update_gui()
    lock.release()

if __name__ == "__main__":
    # Establish RS48 communication channel to the TEC-controller
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
    GPIO.setup(18, GPIO.OUT)
    if GPIO.input(18) == 0:
        GPIO.output(18, GPIO.HIGH)
    """

    # State Machine to check, if the TEC-Controller and the PiXtend PLC
    # are in a good state
    # Initalising of the GUI and passing the parameters required
    gui = GUI()  # pixtend=PiXtendV2L()

    # Defining the lock method for threading -> Deadlock
    lock = threading.Lock()

    """ THREAD 0: Start thread with program main loop """
    main_thread = threading.Thread(target=main_loop)
    main_thread.start()

    # Start the GUI
    gui.mainloop()
