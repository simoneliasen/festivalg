import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="festivalg"
)

cur = mydb.cursor()
cur.execute("SELECT name FROM roskildefestival")
result_list = [row[0] for row in cur.fetchall()]
for x in result_list:
    print(x)

roskildeartists = (json.dumps(result_list))

print(roskildeartists)

# newlist = []
# for i in myresult:
#     newlist.append(i)
#
# print (newlist)
#
# print(newlist[1])
# newlist.append(x)
#     print(newlist)

# import json
# jsonObj = json.dumps(myresult)
# print(jsonObj)


# for x in myresult:
#     print(x)
# print(myresult)
