import time
import os
import sys

from PIL import Image


screen = open('screen.txt', 'w', encoding='utf8')
if len(sys.argv) == 1:
    f = open('data.txt', 'r', encoding='utf8')
else:
    f = open(sys.argv[1], 'r', encoding='utf8')
    

frames = []
frame_num = 0

def clear_screen():
    return open('screen.txt', 'w', encoding='utf8')

def draw_frame(num):
    screen = clear_screen()
    count = 0
    for i in frames[num]:
        screen.write(i)
        count += 1
        if count == 174:
            screen.write('\n')
            count = 0


lstr = f.read()
frames = lstr.split('2')

time.sleep(1)
print(5)
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)

print("START!")

while frame_num != len(os.listdir('image')):
    draw_frame(frame_num)
    frame_num += 1
    time.sleep(1/11)
    
print("Done!")
