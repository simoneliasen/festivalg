import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT GROUP_CONCAT(name) FROM roskildefestival")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# import json
# jsonObj = json.dumps(myresult)
# print(jsonObj)


# for x in myresult:
#     print(x)
# print(myresult)
