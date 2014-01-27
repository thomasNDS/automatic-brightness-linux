#!/usr/bin/python3.2
# -*-coding:Utf-8 -* 

##################################################################
# to launch: python automatic-brightness.py [preference]
# preference option is an integer [0;100] to adapt the brightness
#
# example:                 python automatic-brightness.py
# or with preference:         python automatic-brightness.py 25
#
# MIT licence
##################################################################

import os
import sys

preference = 15 # preference variable [0;100]

# get arguments
if len(sys.argv) > 1:
     preference = int(sys.argv[1])

# get the luminosity level
os.system("streamer -f jpeg -o image.jpeg")
os.system("convert image.jpeg -colorspace Gray -scale 1x1\! -format '%[fx:int(255*r)]' info:-")
cmd = os.popen("convert image.jpeg -colorspace Gray -scale 1x1\! -format '%[fx:int(255*r)]' info:-")

val=float(cmd.read())
brightness = ((val/55.0)*100 + preference)

# luminosity must be enter [15;100]
if brightness < 15:
        brightness = 15
elif brightness > 100:
        brightness = 100
print "Luminosity value: " + str(brightness) 
os.system("xbacklight -set %i" %(brightness)) # set the brightness
os.system("rm image.jpeg")
