import os # Interacts wuth the file system to verify file existence
from PIL import Image # Security measure for corrupted files and validates media 
import cv2 # Can process .mp4 and .avi file to read videos frame by frame


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

        if format in [".jpg", ".jpeg", ".png"]:
            print("Routing to Pillow for static image processing...")
            # If condition to send data to its respective function 

        elif format in [".mp4",  ".avi", ".gif"]:
            print("Routing to Open Cv for video slicing....")
            # elif condition to send data to its respective function 

        else:
            print("Error, unsupported media format.")
            # Else statement for error handling 

# Test execution
if __name__ == "__main__":
    scan_media("test_image.jpg")