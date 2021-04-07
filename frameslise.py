import os
import sys

import imageio
from PIL import Image


reader = imageio.get_reader(sys.argv[1])

for filename in os.listdir('image'):
    os.remove('image/' + filename)
    
count = 0

for frame_number, im in enumerate(reader):
    # im is numpy array
    if frame_number % 3 == 0:
        imageio.imwrite(f'image/frame_{count}.jpg', im)
        count += 1

for filename in os.listdir('image'):
    image_file = Image.open(f'image/{filename}')
    image_file = image_file.convert('1')
    image_file.save(f'image/{filename}')

print("Done!")
