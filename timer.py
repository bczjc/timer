import datetime
import time
import os
from os import system
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


def play(filename):
    winpath = os.environ['WINDIR'] + "\\Media\\"
    pygame.mixer.music.load(winpath+filename)
    pygame.mixer.music.play()
    time.sleep(0.95)

system("title 定時提醒器")
pygame.init()
pygame.mixer.init()

while True:
    try:
        t = int(input("請輸入間隔的分鐘 (1/5/15/30/60): "))
        if t in [1, 5, 15, 30, 60]:
            print("\n--------Timer Start--------")
            print(datetime.datetime.today().strftime("   %Y/%m/%d %a %H:%M"))
            print("---------------------------")
            play("Windows Unlock.wav")
            break
        else:
            print("請重新輸入")
            continue
    except TypeError:
        print("請重新輸入")
    except KeyboardInterrupt:
        exit(1)
    except:
        print("請重新輸入")

while(1):
    hour, min, sec, wday = time.localtime()[3:7]

    if wday >= 0 and wday <= 4:
        # Stock Opening
        if (hour == 8 and min == 45) and sec == 0:
            print("期貨開盤 {0:02d}:{1:02d}".format(hour, min))
            play("Alarm10.wav")
        elif (hour == 9 and min == 0) and sec == 0:
            print("股市開盤 {0:02d}:{1:02d}".format(hour, min))
            play("Alarm10.wav")

        # Stock Close
        if (hour == 13 and min == 30) and sec == 0:
            print("股市收盤 {0:02d}:{1:02d}".format(hour, min))
            play("Ring10.wav")
        elif (hour == 13 and min == 45) and sec == 0:
            print("期貨收盤 {0:02d}:{1:02d}".format(hour, min))
            play("Ring10.wav")

    if (min+1) % t == 0 and (sec != 0 and sec % 53 == 0):
        if min == 59:
            print("REMIND   {0:02d}:{1:02d}".format(
                hour+1, (min+1) % 60))
        else:
            print("REMIND   {0:02d}:{1:02d}".format(
                hour, (min+1) % 60))
        play("Alarm03.wav")

    time.sleep(0.95)
