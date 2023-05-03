# ACSD-Jetson-Code

This repo contains code to run the ACSD, computer vision system. Note that this code will only run properly if run on with the proper dependencies, as outlined in the Yolov7 repo, as well ask ZED SDK.

Note if you do not have CUDA compatibility for Pytorch, Torchvision and OpenCV Python detect.py will run on CPU leading to longer inference times. 

This code can be run by simply executing loop.sh, ideally this would be configured to run upon boot, in a headless system.
