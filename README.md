# Project Title: The GameHub
* **Contributors**: 
  *
       **Team Members**
      *    **Daniel**
      * **Baran**
      * **Krishna**
      * **Ralph**

## Run App on MacOS

### **Prerequisites:**

Python 3.x should be installed on your system.
Steps:

1. [x] **Create virtual environment:** _python3 -m venv env_
2. [x] **Install requirements:** pip3 install -r requirements.txt
3. [x] **Activate virtual environment:** source env/bin/activate
4. [x] **Run app:** python3 run.py runserver

Access the app in your web browser using the specified address.

This repository contains the source code for a Flask web application that serves as a game catalog.
It allows users to explore and manage their game collection, wishlist, and reviews. The app provides a user-friendly interface to interact with the database and perform various operations such as adding new games, updating game details, managing user reviews, and organizing games into different categories.

Features:
- **User Registration and Authentication:** We don't have this feature implemented yet.
- **Game Management:** Users can add new games to their collection, update game details such as name, genre, developer, platform, and price.
- **Wishlist:** Users can maintain a wishlist of games they wish to acquire, prioritize them, and keep track of upcoming releases.
- **User Reviews:** Users can write and publish reviews for games, share their thoughts, and rate their gaming experience.
- **Genre-Specific Attributes:** The app supports genre-specific attributes for games, such as pay-to-win status, classes for MMORPGs, perspective and realism for shooters, sports types, racing realism, platformer momentum-based mechanics, fighting game modes, and horror elements.
- **Database Integration:** The app utilizes a SQLite database to store game and user-related data, ensuring data persistence and efficient retrieval.

This Flask app provides an intuitive and efficient way for gamers to manage their game catalog, wishlist, and reviews. It can be easily customized and extended to include additional features and functionalities based on specific requirements.



  * Setting up a quick flask app with user interface and db connection.
### Cloned repo from TA 
## Install libs:
* python3 -m pip install mysql-connector-python
* python3 -m pip install flask

### Database manager:
* https://www.beekeeperstudio.io/

### Learn more about flask:
* https://www.geeksforgeeks.org/flask-tutorial/

### Learn about sqlite:
* https://docs.python.org/3/library/sqlite3.html
* https://www.sqlite.org/index.html


### Learn about connecting to MySQL DB:
* https://www.w3schools.com/python/python_mysql_getstarted.asp
* https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
