sudo apt-get install zram-config
sudo gedit /usr/bin/init-zram-swapping

#Replace the line:
#mem=$(((totalmem / 2 / ${NRDEVICES}) * 1024))

#with this line:

#mem=$(((totalmem / ${NRDEVICES}) * 1024))
