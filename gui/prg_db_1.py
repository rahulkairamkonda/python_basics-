import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='test')

mycursor = conn.cursor()

mycursor.execute("INSERT INTO `rahul`(`id`) VALUES (4)")

mycursor.execute("SELECT `id` FROM `rahul` ")

print(mycursor.fetchall())

conn.commit() # this is very imp to add values to database elese values wont add to the database

'''
SQL1.py accepting values as tuples using % also ie string formatting 



SQlGUI.py good eg 

query should look like a tuple 
ie in the format string % tuple


'''