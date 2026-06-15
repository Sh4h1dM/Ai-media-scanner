import os
from PIL import Image # Security measure for corrupted files and validates media 
import cv2 # Can process .mp4 and .avi file to read videos frame by frame

filename = "istockphoto-2086363366-612x612.jpg"

img = Image.open(filename)

img.show(img)
print(
    img.format,
    img.size,
    img.mode)