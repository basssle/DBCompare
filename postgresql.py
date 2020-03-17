import psycopg2
import time
from datetime import datetime
import random

conn = psycopg2.connect('dbname=wisemat')
cur= conn.cursor()



#CREATE TABLE
#sqlCreateTable = "create table "+"member"+" (id bigint, name text, age int);"
#cur.execute(sqlCreateTable)
#conn.commit()

#ALTER TABLE
sqlAlterTable = """ALTER TABLE wmtable
                   ALTER COLUMN timestamp SET DATA TYPE timestamp;"""

cur.execute(sqlAlterTable)
print('table altered')


sqlinsert = """INSERT INTO wmtable
      	       VALUES %s ;"""




wmdata = (datetime.now(),) 
for x in range(0, 64):
	rnd = random.randrange(0,100)
	wmdata = wmdata + (rnd,)

cur.execute(sqlinsert, (wmdata,)) #wmdata has to be a tuple, thus the comma
print('random dataset inserted')
conn.commit()


#cur.execute('select * from member where age>70')
#cur.execute('select * from wmtable')

results = cur.fetchall()

for result in results:
	print(result)



conn.close()
cur.close()
