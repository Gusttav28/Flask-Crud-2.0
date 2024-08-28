from flask import Flask, request


class app:
    def __init__(self, appFlask_name_):
        self.appFlask_name_ = appFlask_name_
        self.appFlask_name_ = Flask(__name__)
        self.route_home = "/"
        self.route_tableView = "/tableView"
        self.route_tableUpdate = "/tableUpdate"
        self.route_tableDelete = "/tableDelete"
        

    def app_main(self):
        self.appFlask_name_.run(port=8080, debug=True)

    def app_routes(self):
        @self.appFlask_name_.route(self.route_home)
        def index():
            return "This is the home page"
        
        @self.appFlask_name_.route(self.route_tableView)
        def table_view():
            return "This is the table view page"
        
        @self.appFlask_name_.route(self.route_tableUpdate)
        def table_update():
            return "This is the table update page"
        
        @self.appFlask_name_.route(self.route_tableDelete)
        def table_delete():
            return "This is the table delete page"
        
        
        
        


        

    


        


