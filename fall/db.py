import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")
c.execute("INSERT INTO roser(\"Tyler\", 0)")
c.execute("INSERT INTO roser(\"Bob\", 1)")
c.execute("INSERT INTO roser(\"John\", 2)")

db.commit() #save changes
print(db.tables())
db.close()
