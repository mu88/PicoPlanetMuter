# PicoPlanetMuter
Mute Skype and Teams using a [PicoPlanet](https://github.com/bleeptrack/picoplanet) and [CircuitPython](https://circuitpython.org/). It was developed using a Windows 10 machine, but it should be easy to adapt.

## Functionality
- Mute and unmute Microsoft Teams
- Mute and unmute Microsoft Skype for Business
- Mute and unmute the system speaker

Every command will be confirmed with a blue LED flash.

## Installation via CircuitPython
- Download Circuit Python from [circuitpython.org](https://circuitpython.org/board/picoplanet/)
- Connect your PicoPlanet to your PC. A drive called `PLANETBOOT` should appear.
- Place the firmware on the `PLANETBOOT` drive and wait for a moment. `PLANETBOOT` will dismount and a new drive called `CIRCUITPY` will appear. 
- Download Adafruit CircuitPython Bundle from https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases (e. g. `adafruit-circuitpython-bundle-6.x-mpy-20210507.zip` for version 6 of CircuitPython).
- From the download, copy the folder `lib\adafruit_hid` into the `lib` folder of the `CIRCUITPY` drive.
- Copy `code.py` from this repository into the root of the `CIRCUITPY` drive. The PicoPlanet will reboot.

## Usage
To see if it works simply press the bottommost button (*A2* in [this image](https://github.com/bleeptrack/picoplanet/blob/master/imgs/pinout_front.png)). It should mute or unmute the system speaker and you'll see a blue LED flash as confirmation.