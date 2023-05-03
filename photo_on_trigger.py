import pyzed.sl as sl
import time
import subprocess
import os
import Jetson.GPIO as GPIO

def main():
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    # To zoom in change focal length here
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720  # Use HD720 video mode
    init_params.camera_fps = 3  # Set fps at 3

    print("Init Time")

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Camera Error")
        print(err)
        exit(1)

    # Set up the GPIO input on pin 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.IN)

    # set up timer
    timer_duration = 60
    last_trigger_time = time.time()
    
    # Counting variable for file naming
    cnt = 1

    while(1):
        print("WAITING ON TRIGGER")
        # Pend on trigger from GPIO
        # GPIO.wait_for_edge(17,GPIO.RISING)
        print("TRIGGERED")

        # Check if timer expired, doesn't apply for first photo
        if time.time() - last_trigger_time > timer_duration and cnt != 1:
            break

        filepath = '/home/acsd/yolov7/images/'+str(cnt)+'.jpg'
        image = sl.Mat(memory_type=sl.MEM.CPU)
        # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab() == sl.ERROR_CODE.SUCCESS:
            zed.retrieve_image(image,view = sl.VIEW.LEFT)
            t = image.write(filepath,memory_type = sl.MEM.CPU, compression_level = -1)

        # Run YoloV7 on the Photo
        os.system("python3 detect.py --weights best.pt --source " + filepath + " --img-size 1280 --save-txt")

       # If output file contains 0 in first coulmn disease found
        disease = 0
        with open(filename, 'r') as file:
            for line in file:
                columns = line.strip().split()
                if columns[0] == '0':
                    disease = 1

       # Write decision to output text file
        with open("results.txt","a") as f:
            f.write(str(disease)+"\n")

        # Update Last Trigger Time
        last_trigger_time = time.time()

        # Update Count
        cnt = cnt + 1

    print("Exited Loop")

    # Close the camera
    zed.close()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
