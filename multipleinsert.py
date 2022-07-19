import mysql.connector
mydb_variable=mysql.connector.connect(host='localhost',port='3306',user='root',password='12345',database='store')
cur=mydb_variable.cursor()
query="INSERT INTO book(bookID,bookNAME,bookTITLE) VALUES (%s,%s,%s)"
book=[(2,'c++','programming book'),(3,'php','programming backend'),(4,'pyt','programming book')]
cur.executemany(query,book)
mydb_variable.commit()