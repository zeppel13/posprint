#!/usr/bin/python3

import sys
from escpos.printer import Usb
from PIL import Image



print("running...")

p = Usb(0x0416, 0x5011, 0, profile="TM-T88III")
#p.text("Hello World\n")

filenames = sys.argv[1:]

    # Loop through each filename in the list
for filename in filenames:
    try:
        # Open the image using Pillow
        with Image.open(filename) as im:
            print(f"Image {filename} has format {im.format}, size {im.size}, and mode {im.mode}")
            im.save("image.gif")
            im2 = Image.open("image.gif")
            new_width = (int)(380)
            new_height = (int)(new_width * im2.height / im2.width)
            # im2 = Image.BICUBIC
            im2 = im2.resize((new_width, new_height), Image.BICUBIC)

            p.image(im2, impl='bitImageRaster')
            p.text("\n")

            
    except IOError as e:
        print(f"Could not open file {filename}: {e}")


