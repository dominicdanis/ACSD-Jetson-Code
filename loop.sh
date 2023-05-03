#!/bin/bash

source /home/acsd/env/bin/activate

if [ -f "results.txt" ]; then
    rm -fv results.txt
fi

touch results.txt

if [ -d "images" ]; then
    rm -rfv images
fi

mkdir images

python3 /home/acsd/yolov7/photo_on_trigger.py

# Write to USB
sudo mkdir -p /mnt/usb
sudo mount -t vfat /dev/sda1 /mnt/usb
cp -f results.txt /mnt/usb
cp -fr images /mnt/usb
sudo umount /dev/sda1

