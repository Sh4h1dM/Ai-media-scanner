import os 
# Interacts wuth the file system to verify file existence

from PIL import Image 
# Security measure for corrupted files and validates media 

import cv2 
# Can process .mp4 and .avi file to read videos frame by frame

import numpy as np 
# To convert visual image into a massive, multi dimension array of raw numerical data using NumPy

# Function 1 - handing file input and authentication before processing media 
def scan_media(file_path):

    """
    STAGE 1: Input Ingestion Gatekeeper
    Validates file existence, determines media type via extension extraction, 
    and routes the file to the appropriate processing pipeline (Pillow or OpenCV).
    """

    # Variable check that scans the current directory for a file
    check = os.path.exists(file_path)

    # If condition for error handling 
    if check is not True:
        print("The file does not exist or is not in the appropriate convention!")
        
    # Else condition to extract the format of the file
    else:
        filename, extension = os.path.splitext(file_path)
        # Extracts the extension to determine if media is static or moving text
        
        print(f"File detected with extension : {extension}")
        # Informs the user whether the system can detect the file

        format = extension.lower()
        # Variable that contains the lowercase string of the file extension

        # If condition to send data to its respective function 
        if format in [".jpg", ".jpeg", ".png"]:
            print("Routing to Pillow for static image processing...")
            process_static_image(file_path)

        # elif condition to send data to its respective function 
        elif format in [".mp4",  ".avi", ".gif"]:
            print("Routing to Open Cv for video slicing....")

        # Else statement for error handling 
        else:
            print("Error, unsupported media format.")


# Function 2 - Extracting information from the given image via the Pillow library
def process_static_image(image_path):

    """
    STAGE 1b: Pillow Guard (Static Media Ingestion)
    Opens the validated image file, extracts core metadata, and normalizes
    the color space to RGB to ensure compatibility with downstream AI models.
    """

 
    try: 
        # Attempt to open the target file using Pillow
        img = Image.open(image_path)

        # Outputting image properities
        print(f"Image format : {img.format}")
        print(f"Image size : {img.size}")

        # Variable holds the visual image into a mathematical grid
        img_array = np.array(img)


        # Prints the shape and the number type
        print(img_array.shape)
        print(img_array.dtype)

        # Data normalization - turns pixel integers down to decimals 
        normalised_array = img_array/255

        # Unit test for the created variable
        print(normalised_array)

        # Error handling 
    except Exception:
        print("Image file is corrupted or unreadable")


# Test execution
if __name__ == "__main__":
    scan_media("test_image.jpg")