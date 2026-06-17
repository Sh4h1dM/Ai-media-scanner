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
        print("File does not exist!")
        
    # Else condition to extract the format of the file
    else:
        filename, extension = os.path.splitext(file_path)
        # Extracts the extension to determine if media is static or moving text
        
        print(f"File detected with extension : {extension}")



# Test execution
if __name__ == "__main__":
    scan_media("test_image.jpg")