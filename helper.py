
import os
import time
import datetime

######### change here #########
time_in_seconds = 35
###############################

exercises = [
    'push up',
    'lengthen the trunk down',
    'lengthen the trunk to the right',
    'lengthen the trunk to the left',
    'stretch the right fist down',
    'stretch the left fist down',
    'stretch the right fist up',
    'stretch the left fist up',
    'lengthen the right leg',
    'lengthen the left leg',
    'lets enjoy the day'
]

os.system('say good morning, it is ' + str(datetime.datetime.now().hour) + ' e ' + str(datetime.datetime.now().minute))
os.system('say ' + exercises[0])
time.sleep(3)

for i in range(1, len(exercises)):

    # print exercise and current time (in seconds)
    for j in range(1, time_in_seconds):
        print(exercises[i-1] + ' - ' + str(j))
        time.sleep(1)
    os.system('say ' + exercises[i])


os.system('say it is ' + str(datetime.datetime.now().hour) + ' e ' + str(datetime.datetime.now().minute))
