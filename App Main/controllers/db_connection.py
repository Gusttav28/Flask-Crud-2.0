import mysql.connector

cnn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "30696222",
    database = "crudusersTwo"
)

def db_connection_test():
    print(cnn)

def data_consulting():
    cur = cnn.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    for i in data:
        print(i)

def inserting_into_theDb():
    cur = cnn.cursor()
    cur.execute('INSERT INTO user (id, age, first_name, last_name, ocupation, email, firstname, lastname) VALUES("1", "20", "Gustavo", "Camacho", "Software Engineer", "gusttav28@gmail.com", "Adolfo", "Vargas")')
    cnn.commit()

def updating_data():
    cur = cnn.cursor()
    cur.execute('UPDATE user SET ocupation = "Software Engineer"')
    cnn.commit()
    cur.close()



# verifying the connection with the data base
db_connection_test()

# Inserting data into the table of the data base
# inserting_into_theDb()


updating_data()

# collecting general data from the data base
data_consulting()







