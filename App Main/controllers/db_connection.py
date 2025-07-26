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
    print(data)
    # for i in data:
    #     print(i)

def inserting_into_theDb(age, first_name = str, last_name = str, ocupation = str):
    age = age
    first_name = first_name
    last_name = last_name   
    ocupation = ocupation
    cur = cnn.cursor()
    cur.execute('INSERT INTO user (age, first_name, last_name, ocupation) VALUES(%s, %s, %s, %s)',(age, first_name, last_name, ocupation))
    # cur.execute(f'INSERT INTO user (age, first_name, last_name, ocupation) VALUES({age}, {first_name}, {last_name}, {ocupation})')
    cnn.commit()
    

def updating_data(first_name = str, ocupation = str, id = int):
    first_name = first_name
    ocupation = ocupation
    id = id
    cur = cnn.cursor()
    cur.execute('UPDATE user SET age = %s, first_name = %s, last_name = %s, ocupation = %s WHERE id = %s', (first_name, ocupation, id))
    cnn.commit()
    

def delete_data(id = int):
    id = id
    cur = cnn.cursor()
    try:
        cur.execute(f'DELETE FROM user WHERE id = {id}')
        cnn.commit()
        print(f"the user = {id} was delete successfully")
    except:
        print("It was some error, try again later")
    cnn.close()



# verifying the connection with the data base
# db_connection_test()

# Inserting data into the table of the data base
# inserting_into_theDb(20, "Daniela", "Vindas", "Psichology Doctor - Neurological")

# updating data from the data base
# updating_data("Juan", "Mechanics Engineer", 2)

# delete data from the data base
# delete_data(14)

# collecting general data from the data base
# data_consulting()








