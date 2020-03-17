import random
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from datetime import timedelta

client = MongoClient(port=27017)

db=client.wiseMat


def output(queryArray):
	for entry in queryArray:
		print('------------------------')
		print('\nID: ')
		print( entry['_id'])
		print('\nPressuremap: ')
		for x in range(0,7):
			print(entry['pressuremap'][x])
		print('\nTimestamp')
		print(entry['timestamp'])


def lastxminutes(x):
	delta= timedelta(minutes=x)
	pasttime = (datetime.now()-delta)
	wmretrieve = db.wiseMat.find(
		{'timestamp': {"$gt": pasttime} }
	) #is before date  timestamp >= pasttime
	print('Entries found:')
	print(wmretrieve.count())
	output(wmretrieve)


lastxminutes(10)	



#wmretrieve = db.wiseMat.find({'timestamp' : )
#output(wmretrieve)
