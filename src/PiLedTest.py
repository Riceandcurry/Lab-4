import hal.hal_input_switch as switch
import hal.hal_led as led
from time import sleep

led.init()
switch.init()

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)



while(switch.read_slide_switch() == 0):
    for i in range(50):
        led.set_output(0,1)
        sleep(0.05)
        led.set_output(0,0)
        sleep(0.05)

    


