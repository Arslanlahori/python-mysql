import mysql.connector
mydata=mysql.connector.connect(host='localhost',port='3306',user='root',password='12345',database='store')
cur=mydata.cursor()
query="DELETE FROM book WHERE bookID=2"
cur.execute(query)
mydata.commit()