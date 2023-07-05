from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)



@app.route("/")
def index_page():
    return "index page: under construction"


@app.route("/create-db")
def create_db():

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    # Dropping all old tables
    cursor_obj.execute("DROP TABLE IF EXISTS User")
    cursor_obj.execute("DROP TABLE IF EXISTS Game")
    cursor_obj.execute("DROP TABLE IF EXISTS UserGameLibrary")
    cursor_obj.execute("DROP TABLE IF EXISTS Reviews")
    cursor_obj.execute("DROP TABLE IF EXISTS WishListGame")
    cursor_obj.execute("DROP TABLE IF EXISTS Fighting")
    cursor_obj.execute("DROP TABLE IF EXISTS MMORPG")
    cursor_obj.execute("DROP TABLE IF EXISTS Shooter")
    cursor_obj.execute("DROP TABLE IF EXISTS Sports")
    cursor_obj.execute("DROP TABLE IF EXISTS Platformer")
    cursor_obj.execute("DROP TABLE IF EXISTS Racing")
    cursor_obj.execute("DROP TABLE IF EXISTS Horror")
    cursor_obj.execute("DROP TABLE IF EXISTS RPG")

    # Creating User table
    table = """ CREATE TABLE User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        User_Name TEXT NOT NULL
    ); """
    cursor_obj.execute(table)

    # Creating Game table
    table = """ CREATE TABLE Game (
        GameID INTEGER PRIMARY KEY AUTOINCREMENT,
        Game_Name TEXT NOT NULL,    
        Game_Developer TEXT NOT NULL,
        Game_Player_Capacity INTEGER NOT NULL,
        Game_Release_Date TEXT NOT NULL,
        Game_Price REAL NOT NULL,
        Game_Platform TEXT NOT NULL
    ); """
    cursor_obj.execute(table)

    # Creating UserGameLibrary table
    table = """ CREATE TABLE UserGameLibrary (
        UGLID INTEGER PRIMARY KEY AUTOINCREMENT,
        UGL_UserID INTEGER NOT NULL,
        UGL_GameID INTEGER NOT NULL,
        UGL_Difficulty INTEGER NOT NULL,
        UGL_Playtime REAL NOT NULL,
        UGL_Achievements TEXT NOT NULL,
        UGL_Rating INTEGER NOT NULL,
        UGL_Date_Added DATE NOT NULL,
        FOREIGN KEY (UGL_UserID) REFERENCES User (UserID),
        FOREIGN KEY (UGL_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Review table
    table = """ CREATE TABLE Reviews (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        Review_UGLID INTEGER NOT NULL,
        Review_Thoughts TEXT NOT NULL,
        FOREIGN KEY (Review_UGLID) REFERENCES UserGameLibrary (UGLID)
    ); """
    cursor_obj.execute(table)

    # Creating WishListGame table
    table = """ CREATE TABLE WishListGame (
        WLGID INTEGER PRIMARY KEY AUTOINCREMENT,
        WLG_GameID INTEGER NOT NULL,
        WLG_UserID INTEGER NOT NULL,
        FOREIGN KEY (WLG_GameID) REFERENCES Game (GameID),
        FOREIGN KEY (WLG_UserID) REFERENCES User (UserID)
    ); """
    cursor_obj.execute(table)

    # Creating Horror table
    table = """ CREATE TABLE Horror (
        HorrorID INTEGER PRIMARY KEY AUTOINCREMENT,
        Horror_GameID INTEGER NOT NULL,
        Horror_UGLID INTEGER NOT NULL,
        Horror_Jump_Scare_Rating INTEGER NOT NULL,
        Horror_Suspense_Level INTEGER NOT NULL,
        FOREIGN KEY (Horror_GameID) REFERENCES Game (GameID)
        FOREIGN KEY (Horror_UGLID) REFERENCES UserGameLibrary(UGLID)
    ); """
    cursor_obj.execute(table)

    # Creating Racing table
    table = """ CREATE TABLE Racing (
        RacingID INTEGER PRIMARY KEY AUTOINCREMENT,
        Racing_GameID INTEGER NOT NULL,
        Racing_Realistic INTEGER NOT NULL,
        Racing_Num_Vehicles INTEGER NOT NULL,
        Racing_Num_Tracks INTEGER NOT NULL,
        FOREIGN KEY (Racing_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating MMORPG table
    table = """ CREATE TABLE MMORPG (
        MMORPGID INTEGER PRIMARY KEY AUTOINCREMENT,
        MMORPG_GameID INTEGER NOT NULL,
        MMORPG_Pay_to_Win INTEGER NOT NULL,
        MMORPG_Classes INTEGER NOT NULL,
        FOREIGN KEY (MMORPG_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Fighting table
    table = """ CREATE TABLE Fighting (
        FightingID INTEGER PRIMARY KEY AUTOINCREMENT,
        Fighting_GameID INTEGER NOT NULL,
        Fighting_Game_Modes TEXT NOT NULL,
        Fighting_Combo_Importance INTEGER NOT NULL,
        FOREIGN KEY (Fighting_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Sports table
    table = """ CREATE TABLE Sports (
        SportsID INTEGER PRIMARY KEY AUTOINCREMENT,
        Sports_GameID INTEGER NOT NULL,
        Sports_Sport TEXT NOT NULL,
        Sports_Realistic INTEGER NOT NULL,
        FOREIGN KEY (Sports_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Shooter table
    table = """ CREATE TABLE Shooter (
        ShooterID INTEGER PRIMARY KEY AUTOINCREMENT,
        Shooter_GameID INTEGER NOT NULL,
        Shooter_Perspective TEXT NOT NULL,
        Shooter_Realistic INTEGER NOT NULL,
        Shooter_Ranked TEXT NOT NULL,
        Shooter_Game_Modes TEXT NOT NULL,
        FOREIGN KEY (Shooter_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Platformer table
    table = """ CREATE TABLE Platformer (
        PlatformerID INTEGER PRIMARY KEY AUTOINCREMENT,
        Platformer_GameID INTEGER NOT NULL,
        Platformer_Momentum_Based TEXT NOT NULL,
        Platformer_Total_Levels INTEGER NOT NULL,
        Platformer_Total_Environments INTEGER NOT NULL,
        FOREIGN KEY (Platformer_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating RPG Table
    table = """ CREATE TABLE RPG (
        RPGID INTEGER PRIMARY KEY AUTOINCREMENT,
        RPG_GameID INTEGER NOT NULL,
        RPG_Total_Attributes INTEGER NOT NULL,
        RPG_Classes INTEGER NOT NULL,
        FOREIGN KEY (RPG_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)



    connection_obj.close()

    return "DB is fresh and ready"


@app.route("/get-users")
def get_users():

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute("SELECT * FROM User ORDER BY UserID DESC")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-users.html", users = output)


@app.route("/create-user")
def create_user():                                                       # Creates a user

    name = str(request.args.get("name")).strip()
    if name == '':
        return "Name cannot be empty"

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"INSERT INTO User (User_Name) VALUES ('{name}')")
    connection_obj.commit()

    connection_obj.close()

    return "Created a new user"


@app.route("/get-games")
def get_games():

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute("SELECT * FROM Game ORDER BY GameID DESC")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-games.html", games = output)


@app.route("/create-game")
def create_game():

    name = str(request.args.get("name")).strip()
    developer = str(request.args.get("developer")).strip()
    player_capacity = str(request.args.get("capacity")).strip()
    release_date = str(request.args.get("releaseDate")).strip()
    price = str(request.args.get("price")).strip()
    platform = str(request.args.get("platform")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"INSERT INTO Game (Game_Name, Game_Developer, Game_Player_Capacity, Game_Release_Date, Game_Price, Game_Platform) VALUES ('{name}', '{developer}', '{player_capacity}', '{release_date}', '{price}', '{platform}')")
    connection_obj.commit()

    connection_obj.close()

    return "Created a new game"


@app.route("/create-ugl")
def create_ugl():

    #http://127.0.0.1:5000/create-ugl?userid=1&gameid=1&difficulty=5&playtime=50&achievements=None&rating=5&date=2018
    
    userID = str(request.args.get("userid")).strip()
    gameID = str(request.args.get("gameid")).strip()
    difficulty = str(request.args.get("difficulty")).strip()
    playtime = str(request.args.get("playtime")).strip()
    achievements = str(request.args.get("achievements")).strip()
    rating = str(request.args.get("rating")).strip()
    dateAdded = str(request.args.get("date")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"INSERT INTO UserGameLibrary(UGL_UserID, UGL_GameID, UGL_Difficulty, UGL_Playtime, UGL_Achievements, UGL_Rating, UGL_Date_Added VALUES ('{userID}', '{gameID}', '{difficulty}', '{playtime}', '{achievements}', '{rating}', '{dateAdded}')")
    connection_obj.commit()

    connection_obj.close()


    return "Added to the user game library"

@app.route("/add-fighting")
    #?gameid=1&gamemodes=4&comboimportance=3
def add_fighting():
    gameid = str(request.args.get("gameid")).strip()
    gamemodes = str(request.args.get("gamemodes")).strip()
    comboimportance = str(request.args.get("comboimportance")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"INSERT INTO Fighting(Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES('{gameid}','{gamemodes}','{comboimportance}')")
    connection_obj.commit()
    output = cursor_obj.fetchall()

    connection_obj.close()

    return "added fighting game"

@app.route("/class/<int:id>")
def class_(id):

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"SELECT * FROM classes WHERE id = {id} LIMIT 1")
    cls_info = cursor_obj.fetchone()

    if cls_info is None:
        return "No class found"

    cursor_obj.execute(f"SELECT * FROM users WHERE id IN ( SELECT user_id FROM user_class_reln WHERE class_id = {cls_info[0]} )")
    users = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("class.html", cls_info = cls_info, users = users)


@app.route("/user/<int:id>")
def user(id):

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"SELECT * FROM users WHERE id = {id} LIMIT 1")
    usr_info = cursor_obj.fetchone()

    if usr_info is None:
        return "No user found"

    cursor_obj.execute(f"SELECT * FROM classes WHERE id IN ( SELECT class_id FROM user_class_reln WHERE user_id = {usr_info[0]} )")
    classes = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("user.html", usr_info = usr_info, classes = classes)


@app.route("/connect")
def connect():

    class_id = int(request.args.get("class_id"))
    user_id = int(request.args.get("user_id"))

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM user_class_reln WHERE class_id = {class_id} AND user_id = {user_id} LIMIT 1")
    exist = cursor_obj.fetchone()

    if exist is not None:
        return "Connection already exists"

    try:
        cursor_obj.execute(f"INSERT INTO user_class_reln (class_id, user_id) VALUES ( {class_id}, {user_id} )")
        connection_obj.commit()
    except:
        return "Either user_id or class_id doens't exist"
    
    return "Done!"

if __name__ == '__main__':
    app.run(debug=True)

