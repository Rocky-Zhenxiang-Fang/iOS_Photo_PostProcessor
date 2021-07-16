import os
import pyheif
from PIL import Image
import time

def heic_to_jpg(heic_folder: str, jpg_folder: str) -> None:

    heics = os.listdir(heic_folder)
    unconverted = []
    for heic in heics:
        # f = open(heic)
        name, type = heic.split(".")[0], heic.split(".")[-1]
        if type != "HEIC":
            continue
        try:
            heif_file = pyheif.read(os.path.join(heic_folder, heic))
        except:
            unconverted.append(heic)
            continue
        image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )

        image.save(os.path.join(jpg_folder, name) + ".JPG", "JPEG")
    print(unconverted)
    print(len(unconverted))


if __name__ == "__main__":
    # heic_folder = os.path.abspath("/Volumes/Data/Picture/UnsupportedFile/HEIC_file")
    start_time = time.time()
    heic_folder = os.path.join("test_images", "heic_folder")
    jpg_folder = os.path.join("test_images", "jpg_folder")
    heic_to_jpg(heic_folder, jpg_folder)
    print("Time spent = " + str(time.time() - start_time))