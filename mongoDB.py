from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
import random
import time

client = MongoClient(port=27017)

db=client.wiseMat

serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

pressureArray = [
                                [0,0,0,2,3,0,0,0],
                                [0,0,1,1,1,1,0,0],
                                [0,0,1,6,6,1,0,0],
                                [0,1,5,7,8,5,1,0],
                                [0,2,5,8,8,5,2,0],
                                [0,0,4,5,6,4,0,0],
                                [0,0,0,3,3,0,0,0],
                                [0,0,0,1,1,0,0,0]
                ]

def generateArray(array):
        for i in range(0,8):
                for j in range(0,8):
                        array[i][j] = random.randrange(0,100)



for x in range(1, 201):
	generateArray(pressureArray)
	wmdata = {
		'pressuremap' : pressureArray,
		'timestamp' : datetime.now()
		}
	result=db.wiseMat.insert_one(wmdata)
	print('Created {0} of 200 as {1}'.format(x,result.inserted_id))
	time.sleep(10)
	#print(wmdata)

