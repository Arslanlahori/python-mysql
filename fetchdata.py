import mysql.connector
mydb=mysql.connector.connect(host='localhost',port='3306',user='root',database='alpha')
cur=mydb.cursor()
query="SELECT * FROM user"
cur.execute(query)
result=cur.fetchall()
for x in result:
    print(x)