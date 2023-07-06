from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )


@app.route("/create-db")
def create_db():

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("DROP TABLE IF EXISTS User")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Game")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS UserGame")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Reviews")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS WishListGame")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Fighting")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS MMORPG")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Shooter")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Sports")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Platformer")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Racing")
    connection_obj.commit()
    cursor_obj.execute("DROP TABLE IF EXISTS Horror")
    connection_obj.commit()

    # Creating User table
    table = """ CREATE TABLE User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        User_Name TEXT
    ); """
    cursor_obj.execute(table)

    # Creating Game table
    table = """ CREATE TABLE Game (
        GameID INTEGER PRIMARY KEY AUTOINCREMENT,
        Game_Name TEXT, 
        Game_Genre TEXT,   
        Game_Developer TEXT,
        Game_Release_Date TEXT,
        Game_Platform TEXT,
        Game_Price REAL
    ); """
    cursor_obj.execute(table)

    # Creating UserGame table
    table = """ CREATE TABLE UserGame (
        UGID INTEGER PRIMARY KEY AUTOINCREMENT,
        UG_GameID INTEGER,
        Difficulty STRING,
        Playtime INTEGER,
        Achievements TEXT,
        Rating INTEGER,
        Date_Added DATE,
        FOREIGN KEY (UG_GameID) REFERENCES Game (GameID)
    ); """
    # FOREIGN KEY (UG_UserID) REFERENCES User (UserID),
    # UG_UserID INTEGER,

    cursor_obj.execute(table)

    # Creating Review table
    table = """ CREATE TABLE Reviews (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        Review_UGID INTEGER,
        Review_Thoughts TEXT,
        FOREIGN KEY (Review_UGID) REFERENCES UserGame (UGID)
    ); """
    cursor_obj.execute(table)

    # Creating WishListGame table
    table = """ CREATE TABLE WishListGame (
        WLGID INTEGER PRIMARY KEY AUTOINCREMENT,
        WLG_GameID INTEGER,
        WLG_UserID INTEGER,
        WLG_Priority INTEGER,
        FOREIGN KEY (WLG_GameID) REFERENCES Game (GameID),
        FOREIGN KEY (WLG_UserID) REFERENCES User (UserID)
    ); """
    cursor_obj.execute(table)

    # Creating Horror table
    table = """ CREATE TABLE Horror (
        HorrorID INTEGER PRIMARY KEY AUTOINCREMENT,
        Horror_GameID INTEGER,
        Horror_Jump_Scare_Rating INTEGER,
        Horror_Suspense_Level INTEGER,
        FOREIGN KEY (Horror_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Racing table
    table = """ CREATE TABLE Racing (
        RacingID INTEGER PRIMARY KEY AUTOINCREMENT,
        Racing_GameID INTEGER,
        Racing_Realistic INTEGER,
        Racing_Num_Vehicles INTEGER,
        Racing_Num_Tracks INTEGER,
        FOREIGN KEY (Racing_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating MMORPG table
    table = """ CREATE TABLE MMORPG (
        MMORPGID INTEGER PRIMARY KEY AUTOINCREMENT,
        MMORPG_GameID INTEGER,
        MMORPG_Pay_to_Win INTEGER,
        MMORPG_Classes INTEGER,
        FOREIGN KEY (MMORPG_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Fighting table
    table = """ CREATE TABLE Fighting (
        FightingID INTEGER PRIMARY KEY AUTOINCREMENT,
        Fighting_GameID INTEGER,
        Fighting_Game_Modes TEXT,
        Fighting_Combo_Importance INTEGER,
        FOREIGN KEY (Fighting_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Sports table
    table = """ CREATE TABLE Sports (
        SportsID INTEGER PRIMARY KEY AUTOINCREMENT,
        Sports_GameID INTEGER,
        Sports_Sport TEXT,
        Sports_Realistic INTEGER,
        FOREIGN KEY (Sports_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Shooter table
    table = """ CREATE TABLE Shooter (
        ShooterID INTEGER PRIMARY KEY AUTOINCREMENT,
        Shooter_GameID INTEGER,
        Shooter_Perspective TEXT,
        Shooter_Realistic INTEGER,
        Shooter_Ranked TEXT,
        Shooter_Game_Modes TEXT,
        FOREIGN KEY (Shooter_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Creating Platformer table
    #cursor_obj.execute("DROP TABLE IF EXISTS Platformer")
    #connection_obj.commit()
    table = """ CREATE TABLE Platformer (
        PlatformerID INTEGER PRIMARY KEY AUTOINCREMENT,
        Platformer_GameID INTEGER,
        Platformer_Momentum_Based TEXT,
        Platformer_Total_Levels INTEGER,
        Platformer_Total_Environments INTEGER,
        FOREIGN KEY (Platformer_GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)


    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("The Witcher 3", "MMORPG", "CD Projekt Red", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Doom", "Shooter", "id Software", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Animal Crossing", "MMORPG", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Red Dead Redemption 2", "Action Adventure", "Rockstar Games", "PS4", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Call of Duty: Modern Warfare", "First-person shooter", "Infinity Ward", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Among Us", "Party game", "InnerSloth", "PC", 4.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Grand Theft Auto V", "Action Adventure", "Rockstar Games", "PS4", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Minecraft", "Sandbox", "Mojang Studios", "PC", 26.95))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Legend of Zelda: Breath of the Wild", "Action Adventure", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Super Smash Bros. Ultimate", "Fighting", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("God of War", "Action Adventure", "Santa Monica Studio", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fortnite", "Battle Royale", "Epic Games", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("PlayerUnknown's Battlegrounds", "Battle Royale", "PUBG Corporation", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Overwatch", "First-person shooter", "Blizzard Entertainment", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Cyberpunk 2077", "Role-playing", "CD Projekt", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Horizon Zero Dawn", "Action role-playing", "Guerrilla Games", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Last of Us Part II", "Action-adventure", "Naughty Dog", "PS4", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Final Fantasy VII Remake", "Role-playing", "Square Enix", "PS4", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Super Mario Odyssey", "Platform", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Animal Crossing: New Horizons", "Social simulation", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Death Stranding", "Action", "Kojima Productions", "PS4", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Apex Legends", "Battle Royale", "Respawn Entertainment", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fall Guys: Ultimate Knockout", "Platform", "Mediatonic", "PC", 19.99))



    connection_obj.commit()

    connection_obj.close()

    return "DB is fresh and ready"

class GameAddForm(FlaskForm):
    game = SelectField('Game', coerce=int, validators=[DataRequired()])
    difficulty = SelectField('Difficulty', choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Very Hard', 'Very Hard')])
    playtime = IntegerField('Playtime (in hours)')
    achievements = IntegerField('Achievements (in %)', validators=[NumberRange(min=0, max=100, message="Achievements should be between 0 and 100%")])
    rating = IntegerField('Rating (0-10)', validators=[NumberRange(min=0, max=10, message="Rating should be between 0 and 10")])
    submit = SubmitField('Add Game')

class GameEditForm(FlaskForm):
    difficulty = SelectField('Difficulty', choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Very Hard', 'Very Hard')])
    playtime = IntegerField('Playtime (in hours)')
    achievements = IntegerField('Achievements (in %)', validators=[NumberRange(min=0, max=100, message="Achievements should be between 0 and 100%")])
    rating = IntegerField('Rating (0-10)', validators=[NumberRange(min=0, max=10, message="Rating should be between 0 and 10")])
    submit = SubmitField('Update Game')

class WishListForm(FlaskForm):
    game = SelectField('Game Name:', coerce=int)
    priority = IntegerField('Priority:', validators=[DataRequired()])
    submit = SubmitField('Add to Wishlist')


@app.route("/get-games")
def get_games():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("SELECT * FROM Game ORDER BY GameID DESC")
    games = cursor_obj.fetchall()
    connection_obj.close()

    return render_template("get-games.html", games=games)

@app.route("/search-games")
def search_games():
    search = request.args.get('q')

    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT GameID, Game_Name FROM Game WHERE Game_Name LIKE ?", ('%' + search + '%',))
    games = cursor_obj.fetchall()
    connection_obj.close()

    # Convert to the format that Select2 expects
    games = [{"id": game[0], "text": game[1]} for game in games]

    return jsonify(games)

@app.route("/get-users")
def get_users():
    connection_obj = sqlite3.connect('CS4750Project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM User ORDER BY UserID DESC")
    users = cursor_obj.fetchall()

    connection_obj.close()

    # Check if the request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template("user-table.html", users=users)

    return render_template("get-users.html", users=users)

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

@app.route('/')
def home():
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()
    c.execute("""
        SELECT 
            UserGame.UGID, 
            Game.Game_Name, 
            Game.Game_Genre,
            UserGame.Difficulty, 
            UserGame.Playtime, 
            UserGame.Achievements, 
            UserGame.Rating 
        FROM UserGame 
        JOIN Game ON UserGame.UG_GameID = Game.GameID 
        ORDER BY UserGame.Date_Added DESC
    """)
    games = c.fetchall()
    conn.close()
    return render_template('landingPage.html', games=games)

@app.route('/add-game', methods=['GET', 'POST'])
def add_game():
    # connect to the database
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()

    # retrieve all games from Game table ordered by Game_Name
    c.execute("SELECT * FROM Game ORDER BY Game_Name ASC")
    game_list = c.fetchall()

    # create the form and populate the select field with the games
    form = GameAddForm()
    form.game.choices = [(g[0], g[1]) for g in game_list]

    # handle form submission
    if form.validate_on_submit():
        # insert the new game into the UserGame table
        c.execute("INSERT INTO UserGame (UG_GameID, Difficulty, Playtime, Achievements, Rating, Date_Added) VALUES (?, ?, ?, ?, ?, date('now'))",
                  (form.game.data, form.difficulty.data, form.playtime.data, form.achievements.data, form.rating.data))
        conn.commit()
        conn.close()

        flash('Game added successfully!')
        return redirect(url_for('home'))

    # render the form
    return render_template('add_game.html', form=form)


@app.route('/edit-game/<int:game_id>', methods=['GET', 'POST'])
def edit_game(game_id):
    # connect to the database
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()

    # retrieve the game from the UserGame table
    c.execute("SELECT * FROM UserGame WHERE UGID = ?", (game_id,))
    game = c.fetchone()

    form = GameEditForm()

    if request.method == 'GET':
        # populate the form with the game's data
        # convert to int to make sure correct type is received, default to 0 if nothing is entered
        form.difficulty.data = game[2]
        form.playtime.data = int(game[3]) if game[3] is not None else 0
        form.achievements.data = int(game[4]) if game[4] is not None else 0
        form.rating.data = int(game[5]) if game[5] is not None else 0

    if form.validate_on_submit():
        # update the game in the UserGame table
        # if form is valid, update fields
        c.execute("UPDATE UserGame SET Difficulty = ?, Playtime = ?, Achievements = ?, Rating = ? WHERE UGID = ?",
                  (form.difficulty.data, form.playtime.data, form.achievements.data, form.rating.data, game_id))
        conn.commit()
        conn.close()
        flash('Game updated successfully!')
        return redirect(url_for('home'))

    return render_template('edit_game.html', form=form)

@app.route('/delete-game/<int:game_id>', methods=['POST'])
def delete_game(game_id):
    # connect to the database
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()

    # delete the game from the UserGame table
    c.execute("DELETE FROM UserGame WHERE UGID = ?", (game_id,))
    conn.commit()
    conn.close()

    flash('Game deleted successfully!')
    return redirect(url_for('home'))

@app.route('/confirm-delete/<int:game_id>')
def confirm_delete(game_id):
    # connect to the database
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()

    # retrieve the game from the UserGame table
    c.execute("SELECT UGID, Game.Game_Name FROM UserGame JOIN Game ON UserGame.UG_GameID = Game.GameID WHERE UGID = ?", (game_id,))
    game = c.fetchone()
    conn.close()

    # render the confirmation page
    return render_template('confirm_delete.html', game=game)


@app.route("/wishlist", methods=['GET', 'POST'])
def wishlist():
    # Connect to the database
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()

    # Retrieve all games from the Game table
    c.execute("SELECT * FROM Game ORDER BY Game_Name ASC")
    game_list = c.fetchall()

    # Create a wishlist form
    form = WishListForm()
    form.game.choices = [(g[0], g[1]) for g in game_list]

    if form.validate_on_submit():
        # Insert the game into the Wishlist table
        c.execute("INSERT INTO WishListGame (WLG_GameID, WLG_Priority) VALUES (?, ?)",
                  (form.game.data, form.priority.data))
        conn.commit()

        flash('Game added to wishlist successfully!')
        return redirect(url_for("wishlist"))

    # Retrieve wishlist data
    c.execute("""
        SELECT WLG_Priority, Game_Name, Game_Genre, Game_Platform, Game_Price 
        FROM WishListGame 
        JOIN Game ON WishListGame.WLG_GameID = Game.GameID
        ORDER BY WLG_Priority ASC
    """)
    wishlist = c.fetchall()

    conn.close()

    # Render the form and the wishlist
    return render_template("wishlist.html", form=form, wishlist=wishlist)




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
