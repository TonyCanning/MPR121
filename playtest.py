# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time
import pygame

import Adafruit_MPR121.MPR121 as MPR121
from mote import Mote
from threading import Thread

# Thanks to Scott Garner & BeetBox!
# https://github.com/scottgarner/BeetBox/

print 'Adafruit MPR121 Capacitive Touch Audio Player + Pimoroni mote (USB)'

# Create MPR121 instance.
cap = MPR121.MPR121()
mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

def redPulse():
                for channel in range (1,2):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 255, 0, 0)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,2):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 20, 0, 0)
                             mote.show()
                             time.sleep(0.01)
def greenPulse():
                for channel in range (2,3):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 255, 0)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (2,3):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 20, 0)
                             mote.show()
                             time.sleep(0.01)
def bluePulse():
                for channel in range (3,4):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 0, 255)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (3,4):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 0, 20)
                             mote.show()
                             time.sleep(0.01)
def whitePulse():
                for channel in range (4,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 255, 255, 255)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (4,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 20, 20, 20)
                             mote.show()
                             time.sleep(0.01)
def redAll():
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 255, 0, 0)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 20, 0, 0)
                             mote.show()
                             time.sleep(0.01)
def greenAll():
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 255, 0)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 20, 0)
                             mote.show()
                             time.sleep(0.01)
def blueAll():
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 0, 255)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 0, 0, 20)
                             mote.show()
                             time.sleep(0.01)
def whiteAll():
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 255, 255, 255)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (16):
                             mote.set_pixel(channel, pixel, 20, 20, 20)
                             mote.show()
                             time.sleep(0.01)
def redRev():
                for channel in range (1,5):
                        for pixel in range(15, -1, -1):
                             mote.set_pixel(channel, pixel, 255, 0, 0)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 20, 0, 0)
                             mote.show()
                             time.sleep(0.01)
def greenRev():
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 0, 255, 0)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 0, 20, 0)
                             mote.show()
                             time.sleep(0.01)
def blueRev():
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 0, 0, 255)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 0, 0, 20)
                             mote.show()
                             time.sleep(0.01)
def whiteRev():
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 255, 255, 255)
                             mote.show()
                             time.sleep(0.01)
                for channel in range (1,5):
                        for pixel in range (15, -1, -1):
                             mote.set_pixel(channel, pixel, 20, 20, 20)
                             mote.show()
                             time.sleep(0.01)

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Alternatively, specify a custom I2C address such as 0x5B (ADDR tied to 3.3V),
# 0x5C (ADDR tied to SDA), or 0x5D (ADDR tied to SCL).
#cap.begin(address=0x5B)

# Also you can specify an optional I2C bus with the bus keyword parameter.
#cap.begin(busnum=1)

pygame.mixer.pre_init(4420, -16, 12, 512)
pygame.init()

# Define mapping of capacitive touch pin presses to sound files
# tons more sounds are available but because they have changed to .flac in /opt/sonic-pi/etc/samples/ some will not work
# more .wav files are found in /usr/share/scratch/Media/sounds/ that work fine this example uses Aniamal sounds.

SOUND_MAPPING = {
  0: '/home/pi/sounds/E808_Loop_BD_105-02.wav',
  1: '/home/pi/sounds/E808_Loop_BD_105-03.wav',
  2: '/home/pi/sounds/E808_Loop_SD_105-02.wav',
  3: '/home/pi/sounds/E808_Loop_SD_105-03.wav',
  4: '/home/pi/sounds/E808_Loop_Toms_105-02.wav',
  5: '/home/pi/sounds/E808_Loop_Toms_105-03.wav',
  6: '/home/pi/sounds/E808_Loop_Hats_105-02.wav',
  7: '/home/pi/sounds/E808_Loop_Hats_105-03.wav',
  8: '/home/pi/sounds/E808_Loop_Perc_105-02.wav',
  9: '/home/pi/sounds/E808_Loop_Perc_105-03.wav',
  10: '/home/pi/sounds/E808_Loop_Hats_105-04.wav',
  11: '/home/pi/sounds/E808_Loop_Hats_105-05.wav',
}

#SOUND_MAPPING = {
#  0: '/opt/sonic-pi/etc/samples/ambi_piano.flac',
#  1: '/opt/sonic-pi/etc/samples/elec_hollow_kick.flac',
#  2: '/opt/sonic-pi/etc/samples/ambi_soft_buzz.flac',
#  3: '/opt/sonic-pi/etc/samples/bass_dnb_f.flac',
#  4: '/opt/sonic-pi/etc/samples/bass_hit_c.flac',
#  5: '/opt/sonic-pi/etc/samples/elec_plip.flac',
#  6: '/opt/sonic-pi/etc/samples/bass_trance_c.flac',
#  7: '/opt/sonic-pi/etc/samples/vinyl_backspin.flac',
#  8: '/opt/sonic-pi/etc/samples/elec_soft_kick.flac',
#  9: '/opt/sonic-pi/etc/samples/elec_tick.flac',
#  10: '/opt/sonic-pi/etc/samples/vinyl_rewind.flac',
#  11: '/opt/sonic-pi/etc/samples/elec_twang.flac',
#}

#UNCOMMENT FOR ANIMAL sounds :)

# SOUND_MAPPING = {
#   0: '/usr/share/scratch/Media/sounds/Animal/Bird.wav',
#   1: '/usr/share/scratch/Media/sounds/Animal/Cricket.wav',
#   2: '/usr/share/scratch/Media/sounds/Animal/Dog1.wav',
#   3: '/usr/share/scratch/Media/sounds/Animal/Dog2.wav',
#   4: '/usr/share/scratch/Media/sounds/Animal/Duck.wav',
#   5: '/usr/share/scratch/Media/sounds/Animal/Goose.wav',
#   6: '/usr/share/scratch/Media/sounds/Animal/Horse.wav',
#   7: '/usr/share/scratch/Media/sounds/Animal/Kitten.wav',
#   8: '/usr/share/scratch/Media/sounds/Animal/Meow.wav',
#   9: '/usr/share/scratch/Media/sounds/Animal/Owl.wav',
#   10: '/usr/share/scratch/Media/sounds/Animal/Rooster.wav',
#   11: '/usr/share/scratch/Media/sounds/Animal/WolfHowl.wav',
# }

sounds = [0,0,0,0,0,0,0,0,0,0,0,0]

for key,soundfile in SOUND_MAPPING.iteritems():
        sounds[key] =  pygame.mixer.Sound(soundfile)
        sounds[key].set_volume(1);

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')

last_touched = cap.touched()
while True:
#    mote.clear()
    cap.set_thresholds(12, 6)
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(i))
            if (sounds[i]):
                sounds[i].play()
	    if i == 0:
		t = Thread(target=redPulse)
		t.start()
	    if i == 1:
		t = Thread(target=greenPulse)
		t.start()
	    if i == 2:
		t = Thread(target=bluePulse)
		t.start()
	    if i == 3:
		t = Thread(target=whitePulse)
		t.start()
	    if i == 4:
		t = Thread(target=redAll)
		t.start()
	    if i == 5:
		t = Thread(target=greenAll)
		t.start()
	    if i == 6:
		t = Thread(target=blueAll)
		t.start()
	    if i == 7:
		t = Thread(target=whiteAll)
		t.start()
	    if i == 8:
		t = Thread(target=redRev)
		t.start()
	    if i == 9:
		t = Thread(target=greenRev)
		t.start()
	    if i == 10:
		t = Thread(target=blueRev)
		t.start()
	    if i == 11:
		t = Thread(target=whiteRev)
		t.start()
        if not current_touched & pin_bit and last_touched & pin_bit:
            print('{0} released!'.format(i))

    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.01)

    # Alternatively, if you only care about checking one or a few pins you can
    # call the is_touched method with a pin number to directly check that pin.
    # This will be a little slower than the above code for checking a lot of pins.
    #if cap.is_touched(0):
    #    print('Pin 0 is being touched!')

    # If you're curious or want to see debug info for each pin, uncomment the
    # following lines:
    #print('\t\t\t\t\t\t\t\t\t\t\t\t\t 0x{0:0X}'.format(cap.touched()))
    #filtered = [cap.filtered_data(i) for i in range(12)]
    #print('Filt:', '\t'.join(map(str, filtered)))
    #base = [cap.baseline_data(i) for i in range(12)]
    #print('Base:', '\t'.join(map(str, base)))
