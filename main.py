#!/usr/bin/python3 
import os, rawpy, imageio

#TODO add argparse to input RAW file exttension 
#   or list common format for autodetection 

def main()
    images = listdir()
    for image in images:
    if 'NEF' in image:
        print(raw_to_jpg(image))

def raw_to_jpg(image):
    try:
        with rawpy.imread(image) as raw:
            rgb = raw.postprocess()
            imagename=str(image)+'.jpg'
            imageio.imsave(imagename, rgb)
        return f'image converted: {image}'
    except:
        return 'image conversion failed'

if "__name__" == "__main__":
    main()