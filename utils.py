import os
import pyheif
from PIL import Image, ImageOps
import time
import numpy as np
from typing import Dict

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

def group_duplicate(dir: str) -> Dict[str, str]:
    res = {}
    images = os.listdir(dir)
    for im in images:
        try:
            image = Image.open(os.path.join(dir, im))
        except:
            continue
        hash = average_hashing(image)
        res[hash] = res.get(hash, []) + [im]
    return res

    
def average_hashing(image: Image) -> str: 
    image = image.resize((8, 8))
    image = ImageOps.grayscale(image)
    im_arr = np.array(image)
    im_mean = np.mean(im_arr)
    for r in range(len(im_arr)):
        for c in range(len(im_arr[0])):
            if im_arr[r][c] > im_mean:
                im_arr[r][c] = 1
            else:
                im_arr[r][c] = 0
    res = []
    for row in im_arr:
        res.extend(row)
    res = "".join(str(r) for r in res)
    return res



if __name__ == "__main__":
    # heic_folder = os.path.abspath("/Volumes/Data/Picture/UnsupportedFile/HEIC_file")
    start_time = time.time()
    heic_folder = os.path.join("test_images", "heic_folder")
    jpg_folder = os.path.join("test_images", "jpg_folder")
    heic_to_jpg(heic_folder, jpg_folder)
    print("Time spent = " + str(time.time() - start_time))