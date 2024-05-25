import time
import sys
import os
from datetime import date, datetime
import keyboard

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
    return current_time

def run_timer():
    print("running timer\n")
    start_time = datetime.now()
    while True:
        current_time = datetime.now()
        sys.stdout.write(f'\r{format_timer(time_diff_in_seconds(start_time, current_time))}')
        sys.stdout.flush()
        if keyboard.is_pressed('space'):
            stop_and_log(start_time, current_time)
            break
        time.sleep(0.01)

def stop_and_log(start_time, current_time):
    print(f'\nlogged {format_timer(time_diff_in_seconds(start_time, current_time))}')
    cont = input("type s to continue: ")
    if cont[-1] == "s":
        os.system('clear')
        run_timer()
    else:
        print("bruh")


def time_diff_in_seconds(start, stop):
    time_delta = stop - start
    return int(time_delta.total_seconds())

def format_timer(num_seconds : int):
    """
    Given a number of seconds format to HH:MM:SS
    """

    def format_time(t):
        return str(t) if t >= 10 else "0"+str(t)

    hours = num_seconds // 3600
    minutes = (num_seconds % 3600) // 60
    seconds = num_seconds % 60
    return format_time(hours) + ":" + format_time(minutes) + ":" + format_time(seconds)

### Entry Point ###
if __name__ == '__main__':
    print("TASK: FOREVERFAN")
    run_timer()
