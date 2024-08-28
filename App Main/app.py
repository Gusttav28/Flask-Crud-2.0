from controllers import contructure

if __name__ == "__main__":
    app = contructure.app(__name__)
    app.app_routes()
    app.app_main()  
