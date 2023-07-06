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
    cursor_obj.execute("DROP TABLE IF EXISTS Genre")

    # Creating User table
    table = """ CREATE TABLE User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        User_Name TEXT NOT NULL
    ); """
    cursor_obj.execute(table)

    # Creating AND populating Genre table
    table = """ CREATE TABLE Genre (
        GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
        Genre_Name TEXT NOT NULL
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
        Game_Platform TEXT NOT NULL,
        Game_Review TEXT NOT NULL,
        Game_GenreID INTEGER NOT NULL,
        FOREIGN KEY(Game_GenreID) REFERENCES Genre(GenreID)
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

    # Creating WishListGame table
    table = """ CREATE TABLE WishListGame (
        WLGID INTEGER PRIMARY KEY AUTOINCREMENT,
        WLG_GameID INTEGER NOT NULL,
        WLG_UserID INTEGER NOT NULL,
        FOREIGN KEY (WLG_GameID) REFERENCES Game (GameID),
        FOREIGN KEY (WLG_UserID) REFERENCES User (UserID)
    ); """
    cursor_obj.execute(table)

    # Populating Genre table
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('Horror')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('Platformer')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('Racing')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('MMORPG')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('RPG')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('Fighting')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('Shooter')")
    cursor_obj.execute("INSERT INTO Genre(Genre_Name) VALUES('Sports')")

    connection_obj.close()

    return "DB is fresh and ready"


@app.route("/get-users")
def get_users():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM User ORDER BY UserID DESC")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-users.html", users=output)


@app.route("/create-user")
def create_user():  # Creates a user
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

    return render_template("get-games.html", games=output)


@app.route("/create-game")
def create_game():
    name = str(request.args.get("name")).strip()
    developer = str(request.args.get("developer")).strip()
    player_capacity = str(request.args.get("capacity")).strip()
    release_date = str(request.args.get("releaseDate")).strip()
    price = str(request.args.get("price")).strip()
    platform = str(request.args.get("platform")).strip()
    review = str(request.args.get("review")).strip()
    genre = str(request.args.get("genre")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(
        f"INSERT INTO Game (Game_Name, Game_Developer, Game_Player_Capacity, Game_Release_Date, Game_Price, Game_Platform, Game_Review, Game_GenreID) VALUES ('{name}', '{developer}', '{player_capacity}', '{release_date}', '{price}', '{platform}', '{review}', '{genre}')")
    connection_obj.commit()

    connection_obj.close()

    return "Created a new game"


@app.route("/get-ugl")
def get_ugl():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(
        "SELECT * FROM Game WHERE Game.GameID IN (SELECT UGL_GameID FROM UserGameLibrary WHERE UGL_UserID = 1)")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-ugl.html", ugl=output)


@app.route("/create-ugl")
def create_ugl():
    userid = str(request.args.get("userid")).strip()
    gameid = str(request.args.get("gameid")).strip()
    difficulty = str(request.args.get("difficulty")).strip()
    playtime = str(request.args.get("playtime")).strip()
    achievements = str(request.args.get("achievements")).strip()
    rating = str(request.args.get("rating")).strip()
    date = str(request.args.get("date")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(
        f"INSERT INTO UserGameLibrary (UGL_UserID, UGL_GameID, UGL_Difficulty, UGL_Playtime, UGL_Achievements, UGL_Rating, UGL_Date_Added) VALUES ('{userid}', '{gameid}', '{difficulty}', '{playtime}', '{achievements}', '{rating}', '{date}')")
    connection_obj.commit()

    connection_obj.close()

    return "Added to the user game library"


@app.route("/get-wlg")
def get_wlg():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(
        "SELECT * FROM Game WHERE Game.GameID IN (SELECT WLG_GameID FROM WishListGame WHERE WLG_UserID = 1)")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-wlg.html", wlg=output)


@app.route("/create-wlg")
def create_wlg():
    gameid = str(request.args.get("gameid")).strip()
    userid = str(request.args.get("userid")).strip()
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"INSERT INTO WishListGame (WLG_GameID, WLG_UserID) VALUES ('{gameid}', '{userid}')")
    connection_obj.commit()

    connection_obj.close()

    return "Added to the user wish list"


# GENRE FILTERS
@app.route("/get-genre")
def get_genre():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    genre = str(request.args.get("genre")).strip()

    # 1 --> Horror
    # 2 --> Platformer
    # 3 --> Racing
    # 4 --> MMORPG
    # 5 --> RPG
    # 6 --> Fighting
    # 7 --> Shooter
    # 8 --> Sports

    cursor_obj.execute(
        f"SELECT * FROM Game WHERE Game_GenreID IN (SELECT Genre.GenreID FROM Genre WHERE Genre.GenreID = {genre}) ORDER BY Game.Game_Name")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-genre.html", games=output)


if __name__ == '__main__':
    app.run(debug=True)
