import sys
import mysql.connector as mc

try:
    connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonisi2018")
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()

cursor.execute ("DROP TABLE IF EXISTS employee")

# delete 
#cursor.execute("""DROP TABLE employee;""")

sql_command = """
CREATE TABLE employee ( 
matriculeemp INTEGER PRIMARY KEY, 
nomemp VARCHAR(20), 
prenomemp VARCHAR(30), 
adressemp VARCHAR(30), 
emailemp VARCHAR(30),
serviceemp INTEGER);"""

sql_command2 = """
CREATE TABLE service ( 
idservice INTEGER PRIMARY KEY, 
nomserv VARCHAR(20), 
datecreaserv DATE, 
matriculeemp INTEGER(1));"""

cursor.execute(sql_command)
cursor.execute(sql_command2)

#PARTIE INSERTION DE DONNEES

# staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"),
#                ("Frank", "Schiller", "m", "1955-08-17"),
#                ("Jane", "Wall", "f", "1989-03-14"),
#                ]
               
# for staff, p in enumerate(staff_data):
#     format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
#     VALUES ({staff_no}, '{first}', '{last}', '{gender}', '{birthdate}');"""

#     sql_command = format_str.format(staff_no=staff, first=p[0], last=p[1], gender=p[2], birthdate = p[3])
#     print(sql_command)
#     cursor.execute(sql_command)
    
connection.commit()


cursor.close()
connection.close()



#PARTIE AFFICHAGE DE DONNEES
try:
    connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonisi2018")
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee") 
print('''Result of "SELECT * FROM employee":''')
result = cursor.fetchall() 
for r in result:
    print(r)

cursor.close()
connection.close()
