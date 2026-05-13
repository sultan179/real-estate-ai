"""
Purpose: Convert NumpPy image arrays into viewable JPEG preview images
"""

from pathlib import Path
import cv2
import numpy as np

def save_preview_image(image:np.ndarray,output_path:str)->None:
    """
    save a 16 bit RGB image as a preview JPG

    We normalize 0-65535 to 0-255 16 bit to 8 bit because Opnecv expects JPEG images to be uint8
    """

    #Normalize 16 bit images down to 8-bit
    image_8bit=cv2.convertScaleAbs(image,alpha=(255.0/65535.0))

    #convert RGB TO BGR
    #OpenCV internally uses BGR ordering

    image_bgr=cv2.cvtColor(image_8bit,cv2.COLOR_RGB2BGR)

    #ensure output folder exists
    output_file=Path(output_path)

    output_file.parent.mkdir(parents=True,exist_ok=True)

    #save image
    cv2.imwrite(str(output_file),image_bgr)
    print(f"[INFO] Preview saved:{output_file}")
