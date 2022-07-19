import mysql.connector
ars=mysql.connector.connect(host='localhost',port='3306',user='root',password='12345')
cur=ars.cursor()
cur.execute("CREATE DATABASE store")
