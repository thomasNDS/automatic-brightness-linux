Automatic-brightness-linux
==========================
 
 Small script which adapt the brightness of the screen with your web cam.
 
 Dependencies
============

 - xbacklight
 - streamer
 - imagemagick
 - gstreamer (included in Debian/Ubuntu distributions) 
 - python (included in Debian/Ubuntu distributions) 
 
 On ubuntu:
 
 sudo apt-get install xbacklight streamer imagemagick
 
 Launch
 ======

python automatic-brightness.py [preference]

 preference option is an integer [0;100] to adapt the brightness
 
 example:     python automatic-brightness.py
 or with preference:   python automatic-brightness.py 25
 
 Licencing
==========
 
 MIT licence.
 
 see more in licence file
