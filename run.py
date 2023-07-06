from flask import Flask, render_template, request, redirect
import sqlite3
import csv
from datetime import datetime
app = Flask(__name__,template_folder='templates')


@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/game-list")
def game_list():
    # Retrieve the game list from the database (replace with your database logic)
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("SELECT * FROM Game")
    games = cursor_obj.fetchall()
    connection_obj.close()

    return render_template("game-list.html", games=games)



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

    table = """
    CREATE TABLE WishListGame (
        WLGID INTEGER PRIMARY KEY AUTOINCREMENT,
        Game_Name TEXT NOT NULL, 
        Genre TEXT NOT NULL,
        Platform TEXT NOT NULL,
        Price REAL NOT NULL,
        WLG_UserID INTEGER NOT NULL,
        FOREIGN KEY (WLG_UserID) REFERENCES User (UserID)
    );
    """

    # Execute the CREATE TABLE statement
    cursor_obj.execute(table)

    # Execute the ALTER TABLE statement separately
    alter_table = "ALTER TABLE WishListGame ADD COLUMN Game_Name TEXT"
    cursor_obj.execute(alter_table)

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
    users = cursor_obj.fetchall()

    # Get the game library description and game list URL
    game_library_description = "This is your game library description."
    game_list_url = "/get-games"  # Replace with the appropriate URL for the game list page

    connection_obj.close()

    return render_template("get-users.html", users=users, game_library_description=game_library_description, game_list_url=game_list_url)



@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name").strip()

    if name == '':
        return "Name cannot be empty"

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("INSERT INTO User (User_Name) VALUES (?)", (name,))
    connection_obj.commit()

    connection_obj.close()

    return "User created successfully"


@app.route("/delete-user", methods=["POST"])
def delete_user():
    user_id = request.form.get("user_id")

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    # Get the user name before deleting
    cursor_obj.execute("SELECT User_Name FROM User WHERE UserID = ?", (user_id,))
    user_name = cursor_obj.fetchone()[0]

    cursor_obj.execute("DELETE FROM User WHERE UserID = ?", (user_id,))
    connection_obj.commit()

    connection_obj.close()

    return f"User {user_name} deleted successfully. <a href='/get-users'>Return to User List</a>"





@app.route("/wishlist")
def wishlist():
    # Retrieve the wishlist from the database (replace with your database logic)
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("SELECT * FROM WishListGame")
    wishlist = cursor_obj.fetchall()
    connection_obj.close()

    return render_template("wishlist.html", wishlist=wishlist)

@app.route("/add-to-wishlist", methods=["POST"])
def add_to_wishlist():
    game_name = request.form.get("game_name")
    genre = request.form.get("genre")
    platform = request.form.get("platform")
    price = request.form.get("price")

    # Insert the game into the Wishlist table (replace with your database logic)
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute(
        "INSERT INTO WishListGame (Game_Name, Genre, Platform, Price) VALUES (?, ?, ?, ?)",
        (game_name, genre, platform, price)
    )
    connection_obj.commit()
    connection_obj.close()

    return redirect("/wishlist")  # Redirect back to the wishlist page after adding the game


@app.route("/get-games")
def get_games():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("SELECT * FROM Game ORDER BY GameID DESC")
    games = cursor_obj.fetchall()
    connection_obj.close()

    return render_template("get-games.html", games=games)



# THIS WORKS BUT IT DOESN'T STORE THE URL DATA (Ex: it stores "name" instead of "Valorant")
@app.route("/create-game", methods=["GET", "POST"])
def create_game():
    if request.method == "POST":
        # Retrieve the game details from the request
        name = request.form.get("Game_Name")
        developer = request.form.get("Game_Developer")
        player_capacity = request.form.get("Game_Player_Capacity")
        release_date = request.form.get("Game_Release_Date")
        price = request.form.get("Game_Price")
        platform = request.form.get("Game_Platform")

        # Insert the game into the database (replace with your database logic)
        connection_obj = sqlite3.connect('CS4750Project.db')
        cursor_obj = connection_obj.cursor()
        cursor_obj.execute(
            "INSERT INTO Game (Game_Name, Game_Developer, Game_Player_Capacity, Game_Release_Date, Game_Price, Game_Platform) VALUES (?, ?, ?, ?, ?, ?)",
            (name, developer, player_capacity, release_date, price, platform)
        )
        connection_obj.commit()
        connection_obj.close()

        return redirect("/game-list")  # Redirect to the game list page after successful game creation

    return render_template("create-game.html")





@app.route("/add-UGL")
def add_UGL():
    userID = str(request.args.get("userid")).strip()
    gameID = str(request.args.get("gameid")).strip()
    difficulty = str(request.args.get("difficulty")).strip()
    playtime = str(request.args.get("playtime")).strip()
    achievements = str(request.args.get("achievements")).strip()
    rating = str(request.args.get("rating")).strip()
    dateAdded = str(request.args.get("date")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(
        f"INSERT INTO UserGameLibrary (UGL_UserID, UGL_GameID, UGL_Difficulty, UGL_Playtime, UGL_Achievements, UGL_Rating, UGL_Date_Added) VALUES ('{userID}', '{gameID}', '{difficulty}', '{playtime}', '{achievements}', '{rating}', '{dateAdded}')")
    connection_obj.commit()

    connection_obj.close()

    return "Added to the user game library"

@app.route("/add-game", methods=["POST"])
def add_game():
    data = request.get_json()
    name = data.get("name").strip()
    genre = data.get("genre").strip()
    platform = data.get("platform").strip()
    release_date = data.get("releaseDate").strip()
    price = data.get("price").strip()

    if name == '' or genre == '' or platform == '' or release_date == '' or price == '':
        return "All fields are required"

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Platform, Game_Release_Date, Game_Price) VALUES (?, ?, ?, ?, ?)",
                       (name, genre, platform, release_date, price))
    connection_obj.commit()
    connection_obj.close()

    return "Game added successfully"


@app.route("/add-fighting")
# ?gameid=1&gamemodes=4&comboimportance=3
def add_fighting():
    gameid = str(request.args.get("gameid")).strip()
    gamemodes = str(request.args.get("gamemodes")).strip()
    comboimportance = str(request.args.get("comboimportance")).strip()

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(
        f"INSERT INTO Fighting(Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES('{gameid}','{gamemodes}','{comboimportance}')")
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

    cursor_obj.execute(
        f"SELECT * FROM users WHERE id IN ( SELECT user_id FROM user_class_reln WHERE class_id = {cls_info[0]} )")
    users = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("class.html", cls_info=cls_info, users=users)

@app.route("/view-library")
def view_library():
    genre = request.args.get("genre")

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    if genre:
        cursor_obj.execute(f"SELECT * FROM Game WHERE Genre = '{genre}'")
    else:
        cursor_obj.execute("SELECT * FROM Game")

    games = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("view-library.html", games=games)

@app.route("/user/<int:id>")
def user(id):
    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM users WHERE id = {id} LIMIT 1")
    usr_info = cursor_obj.fetchone()

    if usr_info is None:
        return "No user found"

    cursor_obj.execute(
        f"SELECT * FROM classes WHERE id IN ( SELECT class_id FROM user_class_reln WHERE user_id = {usr_info[0]} )")
    classes = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("user.html", usr_info=usr_info, classes=classes)

@app.route("/import-game")
def import_game():
    return render_template("import-game.html")

@app.route("/import-games", methods=["POST"])
def import_games():
    file = request.files["file"]  # Assuming the CSV file is uploaded as "file" field in a form
    if file.filename.endswith(".csv"):
        connection_obj = sqlite3.connect('CS4750Project.db')
        cursor_obj = connection_obj.cursor()

        # Assuming the CSV file has columns: name, developer, player_capacity, release_date, price, platform
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row["name"].strip()
            developer = row["developer"].strip()
            player_capacity = row["player_capacity"].strip()
            release_date = row["release_date"].strip()
            price = row["price"].strip()
            platform = row["platform"].strip()

            cursor_obj.execute(
                f"INSERT INTO Game (Game_Name, Game_Developer, Game_Player_Capacity, Game_Release_Date, Game_Price, Game_Platform) VALUES (?, ?, ?, ?, ?, ?)",
                (name, developer, player_capacity, release_date, price, platform)
            )
        connection_obj.commit()
        connection_obj.close()

        return "Games imported successfully"
    else:
        return "Invalid file format. Please upload a CSV file."

@app.route("/populate-games")
def populate_games():
    with open('games.csv', 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip the header row
        games = []
        for row in csv_data:
            game = {
                'name': row[0],
                'developer': row[1],
                'player_capacity': int(row[2]),
                'release_date': row[3],
                'price': float(row[4]),
                'platform': row[5]
            }
            games.append(game)

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    for game in games:
        cursor_obj.execute(
            "INSERT INTO Game (Game_Name, Game_Developer, Game_Player_Capacity, Game_Release_Date, Game_Price, Game_Platform) VALUES (?, ?, ?, ?, ?, ?)",
            (game['name'], game['developer'], game['player_capacity'], game['release_date'], game['price'], game['platform'])
        )

    connection_obj.commit()
    connection_obj.close()

    return "Games populated successfully"

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

