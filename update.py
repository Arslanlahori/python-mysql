import mysql.connector
mydb=mysql.connector.connect(host='localhost',port='3306',user='root',password='12345',database='store')
cur=mydb.cursor()
query="UPDATE book SET bookTITLE='BOOK' WHERE bookTITLE='programming book'"
cur.execute(query)
mydb.commit()