import time


f = open('screen.txt', 'w')
torward = True

def clear_screen():
    return open('screen.txt', 'w')

while True:
    if torward:
        for i in range(20):
            f = clear_screen()
            time.sleep(1/12)
            f.write('#' * i)
        torward = False
    else:
        for i in range(20, 0, -1):
            f = clear_screen()
            time.sleep(1/12)
            f.write('#' * i)
        torward = True
