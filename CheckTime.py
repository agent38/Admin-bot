import time
import os


def CheckTime():
    while True:
        current_time = time.localtime()
        current_minute = time.strftime("%H:%M", current_time)
        current_hour = time.strftime("%H", current_time)
        print(current_minute)
        if current_hour == "21":
                current_minute = time.strftime("%H:%M", current_time)
                if current_minute == "21:57" or current_minute == "21:58" or current_minute == "21:59":
                    os.system("python Weather.py")
                    time.sleep(600)
                else:
                  time.sleep(60)
        else:
            time.sleep(3600)
