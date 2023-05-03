import os
import cv2

input_dir = "images"
output_dir = "small_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        file_path = os.path.join(input_dir, filename)
        img = cv2.imread(file_path)
        h, w = img.shape[:2]
        
        # Calculate the aspect ratio of the image
        aspect_ratio = w / h
        
        # Set the desired width and height for 240p
        target_width = 426
        target_height = 240
        
        # If the aspect ratio is wider than 4:3, resize based on width
        if aspect_ratio > 4/3:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        # If the aspect ratio is taller than 16:9, resize based on height
        else:
            new_height = target_height
            new_width = int(target_height * aspect_ratio)
        
        # Resize the image
        resized_img = cv2.resize(img, (new_width, new_height))
        
        # Save the resized image to the output directory
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        new_file_path = os.path.join(output_dir, new_filename)
        cv2.imwrite(new_file_path, resized_img)
