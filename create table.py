import mysql.connector
table=mysql.connector.connect(host='localhost',port='3306',user='root',password='12345',database='store')
cur=table.cursor()
cur.execute("CREATE TABLE BOOK(bookID int,bookNAME varchar(20),bookTITLE varchar(20))")