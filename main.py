#!/usr/bin/python3 
import os, rawpy, imageio
from PIL import Image
from resizeimage import resizeimage

#TODO add argparse to input RAW file exttension 
#   or list common format for autodetection 

def main():
    images = os.listdir()
    for image in images:
        if 'NEF' in image:
            print(raw_to_jpg(image))

    new_images = os.listdir()
    for image in new_images:
        if 'jpg' in image:
            print(resize(image))

def raw_to_jpg(image):
    try:
        with rawpy.imread(image) as raw:
            rgb = raw.postprocess()
            imagename=str(image)+'.jpg'
            imageio.imsave(imagename, rgb)
        return f'image converted: {image}'
    except:
        return 'image conversion failed'


def resize(path):
    with open(path, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [1206, 802])
            cover.save('r'+path, image.format)
    return 'image resized.'


if "__name__" == "__main__":
    main()