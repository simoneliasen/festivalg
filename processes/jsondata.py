#import mysql.connector
import json

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="festivalg"
#)

#cur = mydb.cursor()
#cur.execute("SELECT name FROM roskildefestival")
result_list = [row[0] for row in cur.fetchall()]
roskildeartists = (json.dumps(result_list))
print(roskildeartists)
