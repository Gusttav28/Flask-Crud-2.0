from flask import Flask, request, render_template, url_for, redirect
from . import db_connection


class app:
    def __init__(self, appFlask_name_):
        self.appFlask_name_ = appFlask_name_

        #Constructure of flask
        self.appFlask_name_ = Flask(__name__)



        #Creation of the route parameters
        self.route_home = "/"    #home
        self.route_login = "/login"  #login
        self.route_userlogin = "/userlogin" #user login
        self.route_tableView = "/tableView"  #this is the view of the general table
        self.route_tableUpdate = "/tableUpdate"   #this is a page for make updates
        self.route_tableDelete = "/tableDelete"  #and this is for delete (but it might will disappear because we might no need it)
        self.appFlask_name_.secret_key = "mysssecretkey"  #secret key defination for POST http request  
        
        #this is the dictionary who have the user and the password of each user (this is just for test, than we are gonna change this for the data base) 
        self.users = {
            'gus': "1234",
            "adf": "adfas"
        }
        
        self.mysql_db = db_connection

    # main method for run the application
    def app_main(self):
        self.appFlask_name_.run(port=8090, debug=True)

    
    #method for starts the routes
    def app_routes(self):
        

        @self.appFlask_name_.route(self.route_userlogin)
        def userlogin():
            return render_template("userlogin.html")
        

        #method for the home route
        @self.appFlask_name_.route(self.route_home)
        def index():
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
            # return render_template("table_view.html")
            data_list = []
            if request.method == 'POST':
                try:
                    age = request.form['Age']
                    name = request.form['Name'] 
                    last_name = request.form['lastName']
                    ocupation = request.form['Ocupation']
                    print(age)
                    print(name)
                    print(last_name)
                    print(ocupation)
                    self.mysql_db.inserting_into_theDb(age, name, last_name, ocupation)
                except:
                    print("was some error while you was puting the data")
                    return render_template("table_view.html")
                for i in data_list:
                    print(i)
            # db_data = db.data_consulting()
            # print(db_data)
            return render_template("table_view.html")

        #method for handle the login http request with [GET]
        
        #method for the table update route
        @self.appFlask_name_.route(self.route_tableUpdate)
        def table_update():
            return render_template("table_update.html")
        
        #method for the table delete route (it could be delete)
        @self.appFlask_name_.route(self.route_tableDelete)
        def table_delete():
            return "This is the table delete page"
        
        
        
        


        

    


        


