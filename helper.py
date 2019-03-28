
import os
import time
import datetime

######### change here #########
timeInSeconds = 40
###############################

exercises = ['joga para cima',
            'alonga o tronco para a direita',
            'alonga o tronco para a esquerda',
            'puxa o braço para direita e olha para esquerda',
            'puxa o braço para esquerda e olha para direita',
            'alonga o punho direito para baixo',
            'alonga o punho esquerdo para baixo',
            'alonga o punho direito para cima',
            'alonga o punho esquerdo para cima',
            'alonga perna direita',
            'alonga perna esquerda',
            'alonga tronco para baixo',
            'sentado, alonga tronco para frente',
            'posiçao cleópatra para direita',
            'posiçao cleópatra para esquerda',
            'alonga igual cachorro de férias',
            'bora aproveitar o dia']

os.system('say bom dia, agora são ' + str(datetime.datetime.now().hour) + ' e ' + str(datetime.datetime.now().minute))
os.system('say ' + exercises[0])
time.sleep(5)

for i in range(1, len(exercises)):
    time.sleep(timeInSeconds)
    os.system('say ' + exercises[i])

os.system('say agora são ' + str(datetime.datetime.now().hour) + ' e ' + str(datetime.datetime.now().minute))
