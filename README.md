# fourletterword
## Four letter word generator for Akafugu VFD Raspberry Pi shield

Simple four letter word generator displaying a continuous list of four letter words, each somehow connected.

For example:

    NECK -> PECK -> KISS -> LOVE -> HOPE

## Requirements

Hardware

* Raspberry Pi with [Adafruit Occidentals 0.2 distro](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2) (or similar with enabled SPI support)
* Akafugu VFD Raspberry Pi shield

Software

    sudo apt-get install python-pip
    sudo pip install wiringpi2
    sudo pip install spidev

## Running from Raspberry Pi commandline

    sudo ./fourletterword.py wordlist.txt

Will output a list of four letter words to device, one every 500ms.

## Generating wordlist.txt

(You should never really need to do this...)

To generate wordlist.txt from the original, you can do the following:

    wget https://github.com/perjg/fourletterword/blob/master/flw/sr_concise?raw=true -O sr_concise
	wget https://github.com/perjg/fourletterword/blob/master/flw/rs_concise?raw=true -O rs_concise
	./makelist.py sr_concise rs_concise > wordlist.txt

After generating wordlist.txt, you can safely remove sr_concise and rs_concise

