# The Python Imaging Library (PIL), now maintained as Pillow, is a powerful library for opening,
# manipulating, and saving many different image file formats
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "running.gif", save_all=True, append_images=[images[1], images[2]], duration=200, loop=0
)
# The save() method is used to write/save an image to a file.