
from __future__ import print_function
# Import PiXtend V2 class
from pixtendv2l import PiXtendV2L
import time
import sys

p = PiXtendV2L()
class ldd_control:
    
    def __init_():
        
        if p is not None:
            # Set some variables needed in the main loop
            is_config = False
            cycle_counter = 0

            while True:
                try:
                    # Check if SPI communication is running and the received data is correct
                    if p.crc_header_in_error is False and p.crc_data_in_error is False:
                        cycle_counter += 1

                        if not is_config:
                            is_config = True
                            p.relay0 = p.ON
                            p.digital_out0 = p.ON
                        # Toggle the relays and digital outputs on and off
                        p.relay0 = not p.relay0
                        p.digital_out0 = not p.digital_out0
                    else:                        
                        p.relay0 = p.OFF
                        p.digital_out0 = p.OFF
                        time.sleep(0.25)
                        p.close()
                        del p
                        p = None
                        break
                        
                    # Wait some time, SPI communication will continue in the background
                    time.sleep(1)

                # Catch errors and if an error is caught, leave the program
                except IOError as e:
                    # Print out the caught error and leave program
                    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                    p.close()
                    time.sleep(0.25)
                    del p
                    p = None
                    break
                    
                except ValueError as ve:
                    # Print out the caught error and leave program
                    print ("Value error({0}): {1}".format(ve.errno, ve.strerror))
                    p.close()
                    time.sleep(0.25)
                    del p
                    p = None
                    break

                except RuntimeError as re:
                    # Print out the caught error and leave program
                    print ("Runtime error({0}): {1}".format(re.errno, re.strerror))
                    p.close()
                    time.sleep(0.25)
                    del p
                    p = None
                    break            

                except KeyboardInterrupt:
                    # Keyboard interrupt caught, Ctrl + C, now clean up and leave program
                    for i in range(0, 45, 1):
                        print("")
                    print(strSlogan2)
                    p.relay0 = p.OFF
                    p.digital_out0 = p.OFF
                    time.sleep(0.25)
                    p.close()
                    del p
                    p = None
                    break
