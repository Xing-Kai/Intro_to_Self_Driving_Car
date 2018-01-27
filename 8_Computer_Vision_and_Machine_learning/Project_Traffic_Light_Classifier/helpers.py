# Helper functions
import cv2
import numpy as np
import os
import glob # library for loading images from a directory
import matplotlib.image as mpimg




# This function loads in images and their labels and places them in a list
# The list contains all images and their associated labels
# For example, after data is loaded, im_list[0][:] will be the first image-label pair in the list
def load_dataset(image_dir):
    
    # Populate this empty image list
    im_list = []
    image_types = ["red", "yellow", "green"]
    
    # Iterate through each color folder
    for im_type in image_types:
        
        # Iterate through each image file in each image_type folder
        # glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):
            
            # Read in the image
            im = mpimg.imread(file)
            
            # Check if the image exists/if it's been correctly read-in
            if not im is None:
                # Append the image, and it's type (red, green, yellow) to the image list
                im_list.append((im, im_type))

    return im_list


## Image Mask
def image_mask(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    v = hsv[:,:,2]
    lower_value = 110
    upper_value = 255
    mask = cv2.inRange(v, lower_value, upper_value)
    masked_image = np.copy(rgb_image)
    masked_image[mask == 0] = 0
    
    return masked_image

## Image Crop
def image_crop(rgb_image):
    image_crop = np.copy(rgb_image)
    row_crop = 5
    col_crop = 12
    image_crop = image_crop[row_crop:-row_crop, col_crop:-col_crop, :]
    return image_crop

## Brightness of different area
def image_brightness(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    v = hsv[:,:,2]
    # Sum the V component over all columns (axis = 0)
    v_row_sum = np.sum(v[:,:], axis=0)
    v_sum = sum(np.sum(v[:,:], axis=0))
    v1_sum = sum(np.sum(v[:7,:], axis=0))
    v2_sum = sum(np.sum(v[7:15,:], axis=0))
    v3_sum = sum(np.sum(v[15:,:], axis=0))
    
    return v_sum, v1_sum, v2_sum, v3_sum