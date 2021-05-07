# See https://github.com/bleeptrack/picoplanet/blob/master/example/circuitpython/keyboard_text_example.py

import time
import board
import touchio
import pulseio
from digitalio import DigitalInOut, Direction, Pull

import usb_hid
#consumer_control
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

#keyboard
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

#init touch buttons
touch1 = touchio.TouchIn(board.A0)
touch2 = touchio.TouchIn(board.A1)
touch3 = touchio.TouchIn(board.A2)

#init led lines
ledG = DigitalInOut(board.D5)
ledG.direction = Direction.OUTPUT
ledR = DigitalInOut(board.D6)
ledR.direction = Direction.OUTPUT
ledB = DigitalInOut(board.D7)
ledB.direction = Direction.OUTPUT

#uncomment these if keyboard library is installed. See top comment
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
cc = ConsumerControl(usb_hid.devices)
 
# the keyboard object!
# sleep for a bit to avoid a race condition on some systems
time.sleep(1)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

print("starting...")
#important: capacitive values might need adjustment depending on your procedural design
raw_value_threshold = 3000

def turn_off_led(led):
    #important: LED is inactive when True!
    led.value = True

def turn_on_led(led):
    #important: LED is active when False!
    led.value = False

def turn_off_all_leds():
    turn_off_led(ledR)
    turn_off_led(ledG)
    turn_off_led(ledB)

def toggle_led(led):
    led.value = not led.value

def flash_led_for_confirmation():
    sleep_time = 0.3
    for x in range(2):
        toggle_led(ledB)
        time.sleep(sleep_time)
        toggle_led(ledB)
        time.sleep(sleep_time)

def mute_system():
    cc.send(ConsumerControlCode.MUTE)

def mute_microsoft_teams():
    kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)

def mute_microsoft_skype():
    kbd.send(Keycode.WINDOWS, Keycode.F4)  

def main():
    turn_off_all_leds()

    while True:
        if touch1.raw_value > raw_value_threshold:
            print(touch1.raw_value)
            mute_microsoft_skype()
            flash_led_for_confirmation()

        if touch2.raw_value > raw_value_threshold:
            print(touch2.raw_value)
            mute_microsoft_teams()
            flash_led_for_confirmation()

        if touch3.raw_value > raw_value_threshold:
            print(touch3.raw_value)
            mute_system()
            flash_led_for_confirmation()

if __name__ == "__main__":
    main()