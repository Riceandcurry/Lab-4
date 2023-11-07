import hal.hal_input_switch as switch
import hal.hal_led as led
from time import sleep

led.init()
switch.init()




while(True):
    if switch.read_slide_switch():
        led.set_output(0,1)
        sleep(0.05)
        led.set_output(0,0)
        sleep(0.05)

   else:
    led.set_output(0,1)
    sleep(0.1)
    led.set_output(0,0)
    sleep(0.1)
       

