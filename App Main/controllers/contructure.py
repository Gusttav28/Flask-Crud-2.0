from flask import Flask, request, render_template, url_for, redirect, flash
from . import db_connection
import mysql.connector

class app:
    def __init__(self, appFlask_name_):
        self.appFlask_name_ = appFlask_name_

        #Constructure of flask
        self.appFlask_name_ = Flask(__name__)



        #Creation of the route parameters
        self.route_home = "/"    #home
        self.route_login = "/login"  #login
        self.route_add_user = "/addUser" #this is a url for add new users into the data bases
        self.route_userlogin = "/userlogin" #user login
        self.route_tableView = "/tableView"  #this is the view of the general table
        self.route_tableEdit = "/tableEdit" #this url is for edit the user information
        self.route_tableUpdate = "/tableUpdate/<id>"   #this is a page for make updates
        self.route_tableDelete = "/tableDelete/<id>"  #and this is for delete (but it might will disappear because we might no need it)
        self.appFlask_name_.secret_key = "mysssecretkey"  #secret key defination for POST http request  
        self.mysql_db = db_connection
        #this is the dictionary who have the user and the password of each user (this is just for test, than we are gonna change this for the data base) 
        self.users = {
            'gus': "1234",
            "adf": "adfas"
        }
        
        self.cnn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "30696222",
            database = "crudusersTwo"
            )
        

    # main method for run the application
    def app_main(self):
        self.appFlask_name_.run(port=8092, debug=True)  

    
    #method for starts the routes
    def app_routes(self):
        

        @self.appFlask_name_.route(self.route_userlogin)
        def userlogin():
            return render_template("userlogin.html")
        

        #method for the home route
        @self.appFlask_name_.route(self.route_home)
        def index():
            # print(self.mysql_db.data_consulting())
            return render_template("home.html")

        @self.appFlask_name_.route(self.route_login, methods=['GET'])
        def handle_login():
            if request.method == 'GET':
                username = request.args.get('username')
                password = request.args.get('password')
                if username in self.users and self.users[username] == password:
                    print(username, password)
                    return render_template("home.html") 
                else:
                    return "invalid credentials"
            else:
                return render_template("userlogin.html")

        
        #method for the table view route
        @self.appFlask_name_.route(self.route_tableView, methods=['POST', 'GET'])
        def table_view():   
            cur = self.cnn.cursor()
            cur.execute('SELECT * FROM user')
            data = cur.fetchall()
            return render_template("table_view.html", user_information = data)

        @self.appFlask_name_.route(self.route_add_user, methods=['POST', 'GET'])
        def add_user():
            if request.method == 'POST':           
                age = request.form['Age']
                first_name = request.form['Name'] 
                last_name = request.form['lastName']
                ocupation = request.form['Ocupation']
                print(age)
                print(first_name)
                print(last_name)
                print(ocupation)
                # self.mysql_db.inserting_into_theDb(age, name, last_name, ocupation)
                try:    
                    cur = self.cnn.cursor()
                    cur.execute('INSERT INTO user (age, first_name, last_name, ocupation) VALUES(%s, %s, %s, %s)',(age, first_name, last_name, ocupation))
                    self.cnn.commit()
                    flash(f"The user starting with the name: {first_name} it was added successfully")
                    return redirect(url_for("table_view"))
                except:
                    flash(f"There was a problem traying to add to the data base the user who start with the name: {first_name}")
                    return redirect(url_for("table_view"))

        
        
        @self.appFlask_name_.route("/edit/<id>")     
        def table_edit(id):   
            cur = self.cnn.cursor()
            cur.execute(f'SELECT * FROM user WHERE id = {id}')
            data = cur.fetchall()
            self.cnn.commit()
            print(data)
            return render_template("table_edit.html", user_information = data[0])
           
        #method for handle the login http request with [GET]
        
        #method for the table update route
        @self.appFlask_name_.route(self.route_tableUpdate, methods = ['POST'])
        def table_update(id):
            if request.method == 'POST':
                try:
                    age = request.form['Age']
                    first_name = request.form['Name'] 
                    last_name = request.form['lastName']
                    ocupation = request.form['Ocupation']
                    cur = self.cnn.cursor()
                    cur.execute(f'UPDATE user SET age = %s, first_name = %s, last_name = %s, ocupation = %s WHERE id = {id}', (age, first_name, last_name,  ocupation))
                    self.cnn.commit()
                    flash(f"The user with the id: {id} was updated successfully")
                    return redirect(url_for("table_view"))
                except:
                    flash(f"something goes wrong while trying to update the user with the id: {id}")
            return redirect(url_for("table_view"))
        
        #method for the table delete route (it could be delete)
        @self.appFlask_name_.route(self.route_tableDelete)
        def table_delete(id):
            cur = self.cnn.cursor()
            try:
                cur.execute(f'DELETE FROM user WHERE id = {id}')
                self.cnn.commit()
                flash(f"The user with the id: {id} was delete successfully")
                return redirect(url_for("table_view"))
            except:
                print("It was some error, try again later")
            return "This is the table delete page" 