import os # Interacts wuth the file system to verify file existence
from PIL import Image # Security measure for corrupted files and validates media 
import cv2 # Can process .mp4 and .avi file to read videos frame by frame



def scan_media(file_path):
    
    """
    STAGE 1: Input Ingestion Gatekeeper
    Validates file existence, determines media type via extension extraction, 
    and routes the file to the appropriate processing pipeline (Pillow or OpenCV).
    """

    check = os.path.exists(file_path)

    if check is not True:
        print("File does not exist!")
        
    else:
        filename, extension = os.path.splitext(file_path)
        print(f"File detected with extension : {extension}")



# Test execution
if __name__ == "__main__":
    scan_media("test_image.jpg")