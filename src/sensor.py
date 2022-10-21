# This code is used to simulate the Radation Sensors 

import random
import time
from ingestor import ingest_data

NAME_OF_SENSOR=input('Enter Name of Rad. sensors: ')
LOC_OF_SENSOR=input('Enter Location of the Rad. Sensor: ')
NO_OF_REQUEST=int(input('Enter Number of Request to Simulte: '))
counter = 0

while counter < NO_OF_REQUEST:
    data=random.random()
    print('Request'+str(counter+1)+': '+str(data)+' Sent' )
    ingest_data(NAME_OF_SENSOR,LOC_OF_SENSOR,str(data))
    time.sleep(5)
    counter += 1