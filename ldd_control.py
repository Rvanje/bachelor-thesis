from __future__ import print_function

import sys
import time
import numpy as np

from pixtendv2l import PiXtendV2L


class ldd_control:
    """
    Class to control the whole behaveour of the PiXtend PLC. Get and set
    information and parameters.
    """

    def __init__(self):
        # Initialization of misc. variables
        self.laser_start_bit: bool = 0
        self.ldd_current_sp: float = 1

        # Initialization of the PLC
        self.p = PiXtendV2L()
        if self.p != PiXtendV2L():
            self.p = PiXtendV2L()

    # configuration of the setpoint (sp) of the LDD Current
    def ldd_get_sp(self):
        """
        Return the setpoint of the setting the user has choosen on the hmi.
        """
        return self.ldd_current_sp  # return the actual current

    def ldd_sp_increase(self):
        """
        Increase the current setpoint by 0.1
        """
        self.ldd_current_sp += 0.1

    def ldd_sp_decrease(self):
        """
        Decrease the current setpoint by 0.1
        """        
        self.ldd_current_sp -= 0.1

    # Configuration / pull of the actual value of the laser
    def ldd_get_av(self):
        """
        Try to get the current information from the PiXtend PLC.
        "try" method in place if an abortion/error occures in the
        pulling process.
        """
        try:
            return self.p.analog_in0  # Get the analog input signal of 0
        except(
            IOError, ValueError, RuntimeError, KeyboardInterrupt
        ):
            print("Error Handler Active")
            self.p.close()
            time.sleep(1)
            del self.p
            self.p = None

    # Configuration of laser ignition prerequisites current / voltage
    def A_ramper(self):
        """
        Method to ramp the laser output if it already has started and
        does not start from 0.
        """
        if self.laser_start_bit == 0:
            self.A_limit

    def A_limit(self):
        """
        Check if the limit of the current/voltage has not been exeeded.
        """
        if round(self.ldd_current_sp, 3) > 1.5:
            print(f'Max of 1.5A exeeded {self.ldd_current_sp}')
            # return f'User input too high\nLaser current limit exeeded'
            # return f'Max of 1.5A exeeded'

        elif round(self.ldd_current_sp) < 0:
            print(f'Min. of 0A exeeded {self.ldd_current_sp}')
            # return f'User input too low\nLaser current limit exeeded'
            # return f'Max of min. 0A exeeded'
            
        else:
            pass

    def A_bits(self):
        """
        Calculate the the output voltage / current bits for the analog
        utput. 0 is 0V/0A 1023 is 5V/1.5A MAX of the spec. LDD
        """
        return 511 / 2 * self.ldd_current_sp

    # Configurations of start / stop the laser depending on the 
    def laser_start(self):
        """
        Laser ignition / start -> Depending on the prerequesites of the
        methods above (A_calc, A_limit, A_ramper)
        """
        if round(self.ldd_current_sp, 3) > 1.5:
            print(f'Max of 1.5A exeeded {self.ldd_current_sp}')
            # return f'Max of 1.5A exeeded'

        elif round(self.ldd_current_sp) < 0:
            print(f'Min. of 0A exeeded {self.ldd_current_sp}')
            # return f'Max of min. 0A exeeded'
            
        else:
            laser_bits_2 = 511 / 2 * self.ldd_current_sp
            try:
                for ramps in np.linspace(
                    laser_bits,
                    laser_bits_2,
                    num=5,
                    endpoint=True
                ):
                    self.current = self.p.set_dac_output(
                        self.p.DAC_A, int(ramps)
                    )
                    print(ramps)
                    time.sleep(0.5)
                    # return f'Laser @ {self.current / laser_bits * ramps}A'
                # return "Laser started up..."

            except(
                    IOError, ValueError, RuntimeError, KeyboardInterrupt
            ):
                    print("Error Handler Active")
                    self.p.close()
                    time.sleep(0.5)
                    del self.p
                    self.p = None

    def laser_stop(self):
        """
        Laser stop -> ramps down the current of the ldd
        """
        laser_bits = 511 / 2 * self.ldd_current_sp
        print(laser_bits)
        if laser_bits != 0:
            try:
                for ramps in np.linspace(
                    laser_bits, 0, num=5, endpoint=True
                ):
                    self.current = self.p.set_dac_output(
                        self.p.DAC_A, int(ramps)
                    )
                    print(ramps)
                    time.sleep(0.5)
                    # return f'Laser @ {self.ldd_current_sp / laser_bits * ramps}A'
                # return "Laser stopped..."

            except(
                    IOError, ValueError, RuntimeError, KeyboardInterrupt
            ):
                print("Error Handler Active")
                self.p.close()
                time.sleep(0.5)
                del self.p
                self.p = None

    def ldd_test(self):
        if self.p is not None:
            # Set some variables needed in the main loop
            is_config = False
            cycle_counter = 0
            while True:
                try:
                    # Check if SPI communication is running and the received data is correct
                    if self.p.crc_header_in_error is False and self.p.crc_data_in_error is False:
                        cycle_counter += 1

                        if not is_config:
                            is_config = True
                            self.p.relay0 = self.p.ON
                            self.p.digital_out0 = self.p.ON
                        # Toggle the relays and digital outputs on and off
                        self.p.relay0 = not self.p.relay0
                        self.p.digital_out0 = not self.p.digital_out0
                    else:                        
                        self.p.relay0 = self.p.OFF
                        self.p.digital_out0 = self.p.OFF
                        time.sleep(1)
                        self.p.close()
                        del self.p
                        self.p = None
                        break

                # Catch errors and if an error is caught, leave the program
                except(
                    IOError, ValueError, RuntimeError, KeyboardInterrupt
                ):
                    print("Error Handler Active")
                    self.p.close()
                    time.sleep(1)
                    del self.p
                    self.p = None
                    break

if __name__ == "__main__":
    ldd = ldd_control()
    ldd.laser_start()
    # ldd.ldd_get()
