import psycopg2
from datetime import datetime
from datetime import timedelta

conn = psycopg2.connect('dbname=wisemat')
cur= conn.cursor()


def lastxminutes(x):
    delta = timedelta(minutes=x)

    cur.execute(
        "select * from wmtable where timestamp >= current_timestamp - '%d minutes'::interval" % x

    )

    results = cur.fetchall()
    for result in results:
        print(result)



lastxminutes(5)

conn.close()
cur.close()

