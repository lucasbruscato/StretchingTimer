
import os
import time

######### only change here #########
timeInSeconds = 60
numberOfExercises = 13
####################################

os.system('say "começou"')
time.sleep(5)

for i in range(0, numberOfExercises):
    time.sleep(timeInSeconds)
    if i != numberOfExercises - 1:
        os.system('say "próximo"')

os.system('say "fim"')
