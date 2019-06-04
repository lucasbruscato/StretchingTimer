
import os
import time
import datetime

######### change here #########
time_in_seconds = 34
###############################

exercises = ['joga para cima',
             'alonga o tronco para baixo',
             'alonga o tronco para a direita',
             'alonga o tronco para a esquerda',
             'alonga o punho direito para baixo',
             'alonga o punho esquerdo para baixo',
             'alonga o punho direito para cima',
             'alonga o punho esquerdo para cima',
             'alonga a cabeça para a direita',
             'alonga a cabeça para a esquerda',
             'gira a cabeça lentamente',
             'alonga a perna direita',
             'alonga a perna esquerda',
             'bora aproveitar o dia']

os.system('say bom dia, agora são ' + str(datetime.datetime.now().hour) + ' e ' + str(datetime.datetime.now().minute))
os.system('say ' + exercises[0])
time.sleep(3)

for i in range(1, len(exercises)):

    for j in range(1, time_in_seconds):
        print(exercises[i-1] + ' - ' + str(j))
        time.sleep(1)
    os.system('say ' + exercises[i])


os.system('say agora são ' + str(datetime.datetime.now().hour) + ' e ' + str(datetime.datetime.now().minute))
