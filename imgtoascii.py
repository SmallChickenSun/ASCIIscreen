import time
import os
import sys

from PIL import Image


def crop(input, width, height):
    frame = list()
    im = Image.open(input)
    for i in range(55):
        for j in range(174):
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
    
    s = len(all_pixels)
    
    s //= 5
    
    if white < s:
        return u'█'
    if white < s * 2:
        return u'▓'
    if white < s * 3:
        return u'▒'
    if white < s * 4:
        return u'░'
    else:
        return ' '
        
    # ░▒▓█

count = 0

if len(sys.argv) == 1:
    f = open('data.txt', 'w', encoding='utf8')
else:
    f = open(sys.argv[1], 'w', encoding='utf8')
    


img_width, img_height = Image.open('image/frame_0.jpg').size

widht = img_width / 174
height = img_height / 55

for i in range(len(os.listdir("image"))):
    filename = f"frame_{i}.jpg"
    print(filename)
    frame = crop(f'image/{filename}', widht, height)
    for c in frame:
        f.write(c)
    f.write(str(2))
    count += 1

print("Done!")
