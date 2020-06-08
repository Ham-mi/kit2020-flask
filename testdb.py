import sqlite3
conn = sqlite3.connect('mydb.db')

c=conn.cursor()

num = ('20190972',)
#num = '20190972'
#select * from student where num = '20190972'
#c.execute('select * from student where num = %s'%num)
c.execute('select * from student where num = ?',num)
print(c.fetchone())

conn.close()

#CREATE TABLE "users" (
#	"id"	varchar(50),
#	"pw"	varchar(50),
#	"name"	varchar(50),
#	PRIMARY KEY("id")
#);