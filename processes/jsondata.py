import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM roskildefestival")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

o = [i for (i) in myresult]
print(o)
#
import json

jsonObj = json.dumps(o)

print(jsonObj)

#
# type(jsonObj)
# #
# # [list (i) for i in myresult]
#
# x = [i for i in myresult]
#
# print(x)



#List comprehension
