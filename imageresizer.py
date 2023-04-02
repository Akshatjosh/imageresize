from PIL import Image
from resizeimage import resizeimage
import sys

if len(sys.argv) < 2:
    filename = input("Please enter the filename of the image to resize: ")
else:
    filename = sys.argv[1]

with open(filename, 'rb') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [500, 900])
        cover.save('img_resize.jpeg', 'JPEG')
