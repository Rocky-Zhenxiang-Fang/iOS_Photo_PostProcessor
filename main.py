import utils
import os
from PIL import Image, ImageOps
import numpy as np



if __name__ == '__main__':
    with Image.open(os.path.join("test_images", "test_dup", "IMG_2794.JPG")) as im:
        im = ImageOps.grayscale(im)
        im_arr = np.array(im)
        print(np.mean(im_arr))
    utils.average_hashing(im)
    res = utils.group_duplicate(os.path.join("test_images", "jpg_folder"))
    printed = 0
    for key in res:
        if len(res[key]) > 1:
            print(res[key])
            printed += 1
    if not printed:
        print("No duplicate images found.")