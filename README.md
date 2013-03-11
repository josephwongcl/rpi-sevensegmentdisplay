## Seven Segment LED Display

A simple Python script that controls a [KINGBRIGHT SC03-12RDB](http://www.farnell.com/datasheets/68712.pdf) using a [Raspberry Pi](http://www.raspberrypi.org/).

For reference, here are the GPIO mappings based on Model B [Revision 2.0 Pinout](http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/):
- GPIO 3 maps LED f
- GPIO 5 maps LED g
- GPIO 7 maps LED e
- GPIO 8 maps LED c
- GPIO 10 maps LED b
- GPIO 11 maps LED d
- GPIO 12 maps LED a

## Usage

You must have the [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) Python library package installed.

To run the script simply run:
```shell
sudo python sevensegmentdisplay.py
```

## About Me

At this time of writing I'm currently an Interactive Developer at Digiflare Inc. working heavily on the Android stack for both handhelds and tablets. On my free time I enjoy developing mobile applications and lightweight circuitry on my Raspberry Pi.

You can find more about me [here](http://inajstudios.com) (If I ever get around to finishing it).
