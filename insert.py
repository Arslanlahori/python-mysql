import mysql.connector
ars=mysql.connector.connect(host='localhost',port='3306',user='root',password='12345',database='store')
cur=ars.cursor()
query="INSERT INTO BOOK(bookID,bookNAME,bookTITLE) VALUES (%s,%s,%s)"
b1=(1,'python','programming book')
cur.execute(query,b1)
ars.commit()
