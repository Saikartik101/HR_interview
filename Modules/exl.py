import mysql.connector
import base64
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Saikarthik@321",
  database="sys"
)

mycursor = mydb.cursor()
sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
mycursor.execute(sql)
row2 = mycursor.fetchall();
y2 = list(row2[0])
mycursor.execute ("""
   UPDATE magesh1
   SET pdf=%s
   WHERE id=%s
""", (,100))
mydb.commit()
mydb.close()