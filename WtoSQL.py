import MySQLdb

con = MySQLdb.connect('servername', 'username', 'password', 'database');

with con:
    cur = con.cursor()
    cur.execute("INSERT INTO couponchief(title) VALUES('')")

#sample code to write results into sql db
