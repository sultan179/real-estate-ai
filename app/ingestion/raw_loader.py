"""
purpose is to load raw real-estate bracketed images(.CR2) and convert them into OpenCV compatible NumPy arrays

pipeline flow= CR2 RAW-> rawpy -> 16-bit RGB image->Numpy array->OpenCV processing
"""

from pathlib import Path
import rawpy
import numpy as np

def load_raw_images(raw_path:str)->np.ndarray:
    """
    load a RAW image using rawpy

    returns: Numpy RGB image array

    numpy because opencv works interally with numpy arrays every pixel becomes numerical matrix data
    
    """

    #convert string path in path object

    raw_file=Path(raw_path)

    #safety check
    if not raw_file.exists():
        raise FileNotFoundError(f"Raw file not found:{raw_file}")
    
    #Open RAW image with rawpy

    with rawpy.imread(str(raw_file)) as raw:

        """
        convert raw sensor data into RGB image
        postprocess() performs demosaicing, white balance, color conversion, gamma adjustments
        """

        rgb_image=raw.postprocess(
            use_camera_wb=True, #keep camera white balance settings
            half_size=False, #dont reduce img size for faster processing
            no_auto_bright=True, #keep original exposure
            output_bps=16   #more bits per color preserve more color/detail
        )

        print ("[INFO] RAW image loaded successfully")
        return rgb_image
    
def print_image_info(image:np.ndarray)->None:

        print("\n[IMAGE INFO]")
        print(f"Shape:{image.shape}")
        print(f"Data type:{image.dtype}")
        print(f"Min pixel value:{image.min()}")
        print(f"Max pixel value:{image.max()}")

if __name__=="__main__":

        #test image
        test_image_path="data/input/IMG_9735.CR2"

        #load raw image
        image=load_raw_images(test_image_path)
        print_image_info(image)
