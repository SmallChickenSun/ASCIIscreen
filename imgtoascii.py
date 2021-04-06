import time
import os
import json

from PIL import Image


def crop(input, width, height):
    frame = list()
    im = Image.open(input)
    for i in range(44):
        for j in range(147):
            x = width * j
            y = height * i
            box = (x, y, x + width, y + height)
            a = im.crop(box)
            frame.append(get_dom_color(a))
    return frame


def get_dom_color(img):
    pixels = img.load()
    width, height = img.size

    all_pixels = []
    for x in range(width):
        for y in range(height):            
            cpixel = pixels[x, y]
            if cpixel > 127:
                all_pixels.append(255)
            else:
                all_pixels.append(0)
    
    black = 0
    white = 0
    for pixel in all_pixels:
        if pixel == 255:
            black += 1
        else:
            white += 1
    
    if black > white:
        return '#'
    else:
        return ' '

count = 0

f = open('data.txt', 'w')

for i in range(2191):
    filename = f"frame_{i}.jpg"
    print(filename)
    frame = crop(f'image/{filename}', 3.26, 8.2)
    for c in frame:
        f.write(c)
    f.write(str(2))
    print(count)
    count += 1
