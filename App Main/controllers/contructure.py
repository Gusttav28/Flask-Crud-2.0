from flask import Flask, request, render_template


class app:
    def __init__(self, appFlask_name_):
        self.appFlask_name_ = appFlask_name_
        self.appFlask_name_ = Flask(__name__)
        self.route_home = "/"
        self.route_tableView = "/tableView"
        self.route_tableUpdate = "/tableUpdate"
        self.route_tableDelete = "/tableDelete"
        self.appFlask_name_.secret_key = "mysssecretkey"
        self.users = {
            'gus': "1234",
            "adf": "adfas"
        }


    def app_main(self):
        self.appFlask_name_.run(port=8080, debug=True)

    def app_routes(self):
        @self.appFlask_name_.route(self.route_home)
        def index():
            return render_template("home.html")
        
        @self.appFlask_name_.route(self.route_tableView, methods=['GET'])
        def table_view():
            if request.method == 'GET':
                username = request.args.get('username')
                password = request.args.get('password')
                if username in self.users and self.users[username] == password:
                    print(username, password)
                    return "Welcome"
                else:
                    return "invalid credentials"
            else:
                return render_template("home.html")
        
        @self.appFlask_name_.route(self.route_tableUpdate)
        def table_update():
            return render_template("table_update.html")
        
        @self.appFlask_name_.route(self.route_tableDelete)
        def table_delete():
            return "This is the table delete page"
        
        
        
        


        

    


        


