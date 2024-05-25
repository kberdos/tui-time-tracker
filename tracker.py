import time
import sys
from datetime import date, datetime

#---------------------NOTES---------------------
# print(date.today()) # get date in YYYY-MM-DD
# print(datetime.now()) # get date + time in HH:MM:SS.DDDD
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time) # HH:MM:SS
#-----------------------------------------------

def get_current_time_str():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return str(current_time)

def print_timer():
    while True:
        sys.stdout.write(f'\r{get_current_time_str()}')
        sys.stdout.flush()
        time.sleep(1)


if __name__ == '__main__':
    # print("hello world")
    print_timer()
