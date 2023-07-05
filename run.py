from flask import Flask, render_template, request, g, session, redirect, url_for
import sqlite3


app = Flask(__name__)


@app.before_request
def before_request():
    g.db = sqlite3.connect('CS4750Project.db')
    g.user = None  # Global variable to store the current user

    # Check if user is logged in and retrieve user details
    if 'user_id' in session:
        cursor_obj = g.db.cursor()
        cursor_obj.execute("SELECT * FROM User WHERE UserID = ?", (session['user_id'],))
        g.user = cursor_obj.fetchone()

@app.route("/admin-dashboard")
def admin_dashboard():
    if g.user and g.user[2] == 'admin':
        # Render admin dashboard
        return render_template("admin-dashboard.html")
    else:
        return "Access denied."

@app.route("/user-dashboard")
def user_dashboard():
    if g.user:
        # Render user dashboard
        return render_template("user-dashboard.html")
    else:
        return "Access denied."




@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['user_name'].strip()

        connection_obj = sqlite3.connect('CS4750Project.db')
        cursor_obj = connection_obj.cursor()

        cursor_obj.execute("SELECT * FROM User WHERE User_Name = ?", (name,))
        user = cursor_obj.fetchone()

        connection_obj.close()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('index_page'))

        return "Invalid username."

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index_page'))

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
    # Inside the create_db function

    # Add User_Type column
    table = """ CREATE TABLE User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        User_Name TEXT NOT NULL,
        User_Type TEXT NOT NULL
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

@app.route("/register-user", methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        name = request.form['user_name'].strip()
        user_type = request.form['user_type']

        if name == '':
            return "Name cannot be empty."

        connection_obj = sqlite3.connect('CS4750Project.db')
        cursor_obj = connection_obj.cursor()

        cursor_obj.execute(f"INSERT INTO User (User_Name, User_Type) VALUES (?, ?)", (name, user_type))
        connection_obj.commit()

        connection_obj.close()

        return "User registered successfully."

    return render_template("register-user.html")


@app.route("/get-users")
def get_users():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM User ORDER BY UserID DESC")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-users.html", users=output)


@app.route("/create-user", methods=['GET', 'POST'])
def create_user():
    global user_counter  # Access the global counter

    if request.method == 'POST':
        name = request.form['user_name'].strip()

        if name == '':
            return "Name cannot be empty."

        connection_obj = sqlite3.connect('CS4750Project.db')
        cursor_obj = connection_obj.cursor()

        cursor_obj.execute(f"INSERT INTO User (User_Name) VALUES ('{name}')")
        connection_obj.commit()

        user_id = user_counter  # Assign the current user number
        user_counter += 1  # Increment the counter for the next user

        connection_obj.close()

        return f"Created a new user. User ID: {user_id}"

    return render_template("create-user.html")


@app.route("/get-games")
def get_games():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM Game ORDER BY GameID DESC")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-games.html", games=output)


@app.route("/create-game", methods=['GET', 'POST'])
def create_game():
    if request.method == 'POST':
        name = request.form['Game_Name'].strip()
        developer = request.form['Game_Developer'].strip()
        player_capacity = int(request.form['Game_Player_Capacity'])
        release_date = request.form['Game_Release_Date'].strip()
        price = float(request.form['Game_Price'])
        platform = request.form['Game_Platform'].strip()

        if name == '' or price == '':
            return "Name and price cannot be empty"

        connection_obj = sqlite3.connect('CS4750Project.db')
        cursor_obj = connection_obj.cursor()

        cursor_obj.execute(
            "INSERT INTO Game (Game_Name, Game_Developer, Game_Player_Capacity, Game_Release_Date, Game_Price, Game_Platform) VALUES (?, ?, ?, ?, ?, ?)",
            (name, developer, player_capacity, release_date, price, platform))
        connection_obj.commit()

        connection_obj.close()

        return "Created a new game"

    return render_template("create-game.html")

@app.route('/create-account')
def create_account():
    # Add your code to render the create account page
    return render_template('create-account.html')



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

