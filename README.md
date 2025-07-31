# Flask-CRUD
This is a RESTful API developed with Python and Flask that simulates a basic inventory management system. The project integrates frontend technologies such as JavaScript, HTML, and CSS to provide an interactive and functional interface. The goal of this application is to reinforce concepts related to RESTful services while applying them to a more practical and structured use case.

## Initialize the Project
To initialize the project, open your IDE terminal and navigate to the root directory of the application. Once there, run the following command:

python3 app.py
This command will start a development server. The application will be accessible at http://localhost:3001, where you can test the different routes and verify the proper functionality of the CRUD operations.

## Features
Create, Read, Update, and Delete data through HTTP requests.

Use of Flask routes to handle client-server communication.

Frontend interface built with HTML, CSS, and JavaScript for easier interaction with the API.

Simple and clean project structure for educational purposes.

/FLASKS-CRUD
│
├── static/ # CSS and client-side JavaScript files
├── templates/ # HTML templates
├── app.py # Main application file
└── README.md # Project documentation

## Requirements
Make sure to install the required dependencies before running the application. You can use the following command:

pip install -r requirements.txt
Alternatively, manually install Flask if you don't have a requirements file:

pip install Flask
API Endpoints

## Below are examples of basic routes:
GET / – Fetch all items (index function)

POST /add_contact – Create a new item (add_contact function)

POST /update/user_id – Update an existing item (update_contact function)

DELETE /delete/id – Delete an item by ID (delete function)

# Conclusion
This inventory application is a practical example of how RESTful APIs can be used to manage data-driven systems. Its structure and functionality aim to reflect a real-world inventory system, making it a useful resource for learning both backend and frontend integration in web development.
