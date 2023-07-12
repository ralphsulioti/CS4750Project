from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, IntegerField, FloatField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


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
    cursor_obj.execute("DROP TABLE IF EXISTS RPG")
    connection_obj.commit()

     # Users Table
    table = """
    CREATE TABLE User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        User_Name VARCHAR(255)
    )
    """
    cursor_obj.execute(table)

    # Game Table
    table = """
    CREATE TABLE Game (
        GameID INTEGER PRIMARY KEY,
        Game_Name TEXT,
        Game_Developer TEXT,
        Game_Release_Date TEXT,
        Game_Platform TEXT,
        Game_Player_Capacity INTEGER,
        Game_Price REAL,
        Game_Genre TEXT
    )
    """
    cursor_obj.execute(table)

    # User_Game_Library Table
    table = """
    CREATE TABLE UserGame (
        UserGameID INTEGER PRIMARY KEY,
        UserID INTEGER,
        GameID INTEGER,
        Difficulty TEXT,
        Playtime INTEGER CHECK (Playtime > 0),
        Achievements INTEGER CHECK (Achievements >= 0 AND Achievements <= 100),
        Rating REAL CHECK (Rating > 0 AND Rating <= 10),
        Review TEXT,
        Date_Added TEXT,
        FOREIGN KEY (UserID) REFERENCES Users (UserID),
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # Wishlist_Game Table
    table = """
    CREATE TABLE WishListGame (
        WLGID INTEGER PRIMARY KEY,
        WLG_GameID INTEGER,
        WLG_UserID INTEGER,
        WLG_Priority TEXT,
        FOREIGN KEY (WLG_GameID) REFERENCES Game (GameID),
        FOREIGN KEY (WLG_UserID) REFERENCES Users (UserID)
    )
    """
    cursor_obj.execute(table)

    # Fighting Table
    table = """
    CREATE TABLE Fighting (
        GameID INTEGER PRIMARY KEY,
        Game_Mode TEXT,
        Combo_Importance INTEGER,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # Horror Table
    table = """
    CREATE TABLE Horror (
        GameID INTEGER PRIMARY KEY,
        Jump_Scare_Rating INTEGER,
        Suspense_Level INTEGER,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # Racing Table
    table = """
    CREATE TABLE Racing (
        GameID INTEGER PRIMARY KEY,
        Realistic INTEGER,
        Number_Of_Vehicles INTEGER,
        Number_Of_Tracks INTEGER,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # Platformer Table
    table = """
    CREATE TABLE Platformer (
        GameID INTEGER PRIMARY KEY,
        Momentum_Based TEXT,
        Total_Levels INTEGER,
        Total_Environments INTEGER,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # Shooter Table
    table = """
    CREATE TABLE Shooter (
        GameID INTEGER PRIMARY KEY,
        Perspective TEXT,
        Realistic INTEGER,
        Ranked TEXT,
        Game_Mode TEXT,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # MMORPG Table
    table = """
    CREATE TABLE MMORPG (
        GameID INTEGER PRIMARY KEY,
        Pay_to_Win INTEGER,
        MMORPG_Class TEXT,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)

    # Creating RPG Table
    table = """ CREATE TABLE RPG (
        GameID INTEGER PRIMARY KEY,
        RPG_GameID INTEGER,
        RPG_Total_Attributes INTEGER,
        RPG_Classes INTEGER,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    ); """
    cursor_obj.execute(table)

    # Sports Table
    table = """
    CREATE TABLE Sports (
        GameID INTEGER PRIMARY KEY,
        Type TEXT,
        Realistic INTEGER,
        FOREIGN KEY (GameID) REFERENCES Game (GameID)
    )
    """
    cursor_obj.execute(table)


    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("The Witcher 3", "RPG", "CD Projekt Red", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Doom", "Shooter", "id Software", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Animal Crossing", "RPG", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Red Dead Redemption 2", "RPG", "Rockstar Games", "PS4", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Call of Duty: Modern Warfare", "Shooter", "Infinity Ward", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Among Us", "MMORPG", "InnerSloth", "PC", 4.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Grand Theft Auto V", "MMORPG", "Rockstar Games", "PS4", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Minecraft", "RPG", "Mojang Studios", "PC", 26.95))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Legend of Zelda: Breath of the Wild", "RPG", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Super Smash Bros. Ultimate", "Fighting", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("God of War", "RPG", "Santa Monica Studio", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fortnite", "Shooter", "Epic Games", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("PlayerUnknown's Battlegrounds", "Shooter", "PUBG Corporation", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Overwatch", "Shooter", "Blizzard Entertainment", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Cyberpunk 2077", "RPG", "CD Projekt", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Horizon Zero Dawn", "RPG", "Guerrilla Games", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Last of Us Part II", "RPG", "Naughty Dog", "PS4", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Final Fantasy VII Remake", "RPG", "Square Enix", "PS4", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Super Mario Odyssey", "Platform", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Animal Crossing: New Horizons", "MMORPG", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Death Stranding", "RPG", "Kojima Productions", "PS4", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Apex Legends", "Shooter", "Respawn Entertainment", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fall Guys: Ultimate Knockout", "Platform", "Mediatonic", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("BioShock Infinite", "Shooter", "Irrational Games", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Stardew Valley", "RPG", "ConcernedApe", "PC", 14.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Elder Scrolls V: Skyrim", "RPG", "Bethesda Game Studios", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("League of Legends", "MMORPG", "Riot Games", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Mass Effect 2", "RPG", "BioWare", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Genshin Impact", "RPG", "miHoYo", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Undertale", "RPG", "Toby Fox", "PC", 9.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Terraria", "RPG", "Re-Logic", "PC", 9.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Rocket League", "Sports", "Psyonix", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Borderlands 3", "Shooter", "Gearbox Software", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Far Cry 5", "Shooter", "Ubisoft Montreal", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Uncharted 4: A Thief's End", "RPG", "Naughty Dog", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Sims 4", "RPG", "Maxis, The Sims Studio", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Persona 5", "RPG", "P-Studio", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("FIFA 22", "Sports", "EA Sports", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Civilization VI", "RPG", "Firaxis Games", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Resident Evil 3", "Horror", "Capcom", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Diablo III", "RPG", "Blizzard Entertainment", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Halo: The Master Chief Collection", "Shooter", "343 Industries", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Valorant", "Shooter", "Riot Games", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Destiny 2", "Shooter", "Bungie", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Splatoon 2", "Shooter", "Nintendo", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Dragon Quest XI", "RPG", "Square Enix", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Donkey Kong Country: Tropical Freeze", "Platformer", "Retro Studios", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Luigi's Mansion 3", "RPG", "Next Level Games", "Switch", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Resident Evil 2 Remake", "Horror", "Capcom", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Dead by Daylight", "Horror", "Behaviour Interactive", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Hollow Knight", "Platformer", "Team Cherry", "PC", 14.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Sekiro: Shadows Die Twice", "RPG", "FromSoftware", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Final Fantasy XIV: A Realm Reborn", "MMORPG", "Square Enix", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Rainbow Six Siege", "Shooter", "Ubisoft Montreal", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Need for Speed Heat", "Racing", "Ghost Games", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("FIFA 20", "Sports", "EA Vancouver", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("FIFA 21", "Sports", "EA Vancouver", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Street Fighter V", "Fighting", "Capcom", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Amnesia: The Dark Descent", "Horror", "Frictional Games", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Outlast 2", "Horror", "Red Barrels", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Little Nightmares", "Platformer", "Tarsier Studios", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Celeste", "Platformer", "Matt Makes Games", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Dragon Age: Inquisition", "RPG", "BioWare", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Guild Wars 2", "MMORPG", "ArenaNet", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Battlefield V", "Shooter", "DICE", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Forza Horizon 4", "Racing", "Playground Games", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("NBA 2K21", "Sports", "Visual Concepts", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Mortal Kombat 11", "Fighting", "NetherRealm Studios", "PC", 49.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Silent Hill 2", "Horror", "Konami", "PC", 9.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Project Cars 3", "Racing", "Slightly Mad Studios", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("NHL 21", "Sports", "EA Vancouver", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Tekken 7", "Fighting", "Bandai Namco Entertainment", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Until Dawn", "Horror", "Supermassive Games", "PS4", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Alien: Isolation", "Horror", "Creative Assembly", "PC", 39.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Rayman Legends", "Platformer", "Ubisoft", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Dark Souls III", "RPG", "FromSoftware", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("World of Warcraft", "MMORPG", "Blizzard Entertainment", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Call of Duty: Warzone", "Shooter", "Infinity Ward", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Grid Autosport", "Racing", "Codemasters", "PC", 34.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Madden NFL 21", "Sports", "EA Tiburon", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Injustice 2", "Fighting", "NetherRealm Studios", "PC", 49.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Outlast", "Horror", "Red Barrels", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Layers of Fear", "Horror", "Bloober Team", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Ori and the Will of the Wisps", "Platformer", "Moon Studios", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Star Wars: The Old Republic", "MMORPG", "BioWare", "PC", 14.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Counter-Strike: Global Offensive", "Shooter", "Valve", "PC", 0.00))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Burnout Paradise Remastered", "Racing", "Criterion Games", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("MLB The Show 21", "Sports", "San Diego Studio", "PS4", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Soulcalibur VI", "Fighting", "Project Soul", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("The Forest", "Horror", "Endnight Games", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Observer", "Horror", "Bloober Team", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Spelunky 2", "Platformer", "Mossmouth, LLC", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fallout 3", "RPG", "Bethesda Game Studios", "PC", 9.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fallout New Vegas", "RPG", "Bethesda Game Studios", "PC", 9.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Fallout 4", "RPG", "Bethesda Game Studios", "PC", 29.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Elder Scrolls Online", "MMORPG", "Zenimax Online Studios", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Assetto Corsa", "Racing", "Kunos Simulazioni", "PC", 19.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("UFC 4", "Sports", "EA Vancouver", "PS4", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                        ("Dragon Ball FighterZ", "Fighting", "Arc System Works", "PC", 59.99))
    cursor_obj.execute("INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
                    ("Guild Wars 2", "MMORPG", "ArenaNet", "PC", 29.99))
    
    cursor_obj.execute("INSERT INTO Fighting (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'Fighting'")
    cursor_obj.execute("INSERT INTO Horror (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'Horror'")
    cursor_obj.execute("INSERT INTO Racing (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'Racing'")
    cursor_obj.execute("INSERT INTO Platformer (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'Platformer'")
    cursor_obj.execute("INSERT INTO Shooter (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'Shooter'")
    cursor_obj.execute("INSERT INTO MMORPG (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'MMORPG'")
    cursor_obj.execute("INSERT INTO RPG (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'RPG'")
    cursor_obj.execute("INSERT INTO Sports (GameID) SELECT GameID FROM Game WHERE Game_Genre = 'Sports'")

    connection_obj.commit()

    connection_obj.close()

    return render_template("create_db.html")





class GameAddForm(FlaskForm):
   game = SelectField('Game', coerce=int, validators=[DataRequired()])
   difficulty = SelectField('Difficulty', choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Normal', 'Normal'),
                                                   ('Hard', 'Hard'), ('Very Hard', 'Very Hard')])
   playtime = IntegerField('Playtime (in hours)', validators=[DataRequired()])
   achievements = IntegerField('Achievements (in %)', validators=[
       DataRequired(), NumberRange(min=0, max=100, message="Achievements should be between 0 and 100%")])
   rating = IntegerField('Rating (0-10)',
                         validators=[DataRequired(), NumberRange(min=0, max=10, message="Rating should be between 0 and 10")])
   submit = SubmitField('Add Game')




class GameEditForm(FlaskForm):
   difficulty = SelectField('Difficulty', choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Normal', 'Normal'),
                                                   ('Hard', 'Hard'), ('Very Hard', 'Very Hard')])
   playtime = IntegerField('Playtime (in hours)', validators=[DataRequired()])
   achievements = IntegerField('Achievements (in %)', validators=[
       DataRequired(), NumberRange(min=0, max=100, message="Achievements should be between 0 and 100%")])
   rating = IntegerField('Rating (0-10)',
                         validators=[DataRequired(), NumberRange(min=0, max=10, message="Rating should be between 0 and 10")])
   submit = SubmitField('Update Game')


class WishListForm(FlaskForm):
   game = SelectField('Game Name:', coerce=int)
   priority = IntegerField('Priority:', validators=[DataRequired()])
   submit = SubmitField('Add to Wishlist')


class ReviewForm(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Save Review')

def create_form(field_names):
    class DynamicForm(FlaskForm):
        pass

    for field_name in field_names:
        setattr(DynamicForm, field_name, StringField(field_name))

    setattr(DynamicForm, "submit", SubmitField("Save"))
    return DynamicForm


@app.route('/view-details/<int:game_id>', methods=['GET', 'POST'])
def view_details(game_id):
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()

    # retrieve the game from the Game table and UserGame table
    c.execute("""
        SELECT 
            Game.GameID, 
            Game.Game_Name, 
            Game.Game_Developer, 
            Game.Game_Platform, 
            Game.Game_Genre, 
            UserGame.Review,
            UserGame.Date_Added
        FROM Game 
        JOIN UserGame ON Game.GameID = UserGame.GameID 
        WHERE Game.GameID = ?
    """, (game_id,))
    game = c.fetchone()

    print(game)

    genre_table = game[4]
    c.execute(f"PRAGMA table_info({genre_table})")
    columns = [column[1] for column in c.fetchall()]

    c.execute(f"SELECT {', '.join(columns)} FROM {genre_table} WHERE GameID = ?", (game_id,))
    genre_data = c.fetchone()

    form_review = ReviewForm()
    form_genre = create_form(columns[1:])()

    if request.method == 'GET':
        form_review.review.data = game[5]
        for field_name, data in zip(columns[1:], genre_data[1:]):
            getattr(form_genre, field_name).data = data

    if form_review.validate_on_submit():
        # update the review in the UserGame table
        c.execute("UPDATE UserGame SET Review = ? WHERE GameID = ?", (form_review.review.data, game_id))
        conn.commit()
        flash('Review updated successfully!')
        return redirect(url_for('view_details', game_id=game_id))

    if form_genre.validate_on_submit():
        # Update the genre data in the genre table
        updates = ", ".join(f"{field_name} = ?" for field_name in columns[1:])
        c.execute(f"UPDATE {genre_table} SET {updates} WHERE GameID = ?", (*[getattr(form_genre, field_name).data for field_name in columns[1:]], game_id))
        conn.commit()
        flash('Genre data updated successfully!')
        return redirect(url_for('view_details', game_id=game_id))

    conn.close()

    return render_template('view_details.html', game=game, form_review=form_review, form_genre=form_genre)



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
            UserGame.GameID, 
            Game.Game_Name, 
            Game.Game_Genre,
            UserGame.Difficulty, 
            UserGame.Playtime, 
            UserGame.Achievements, 
            UserGame.Rating 
        FROM UserGame 
        JOIN Game ON UserGame.GameID = Game.GameID 
        ORDER BY UserGame.Date_Added DESC
    """)
    games = c.fetchall()
    conn.close()
    return render_template('landingPage.html', games=games)

@app.route("/top-rated-games")
def top_rated_games():
    conn = sqlite3.connect('CS4750Project.db')
    c = conn.cursor()
    c.execute("""
        SELECT
            UserGame.UserGameID,
            Game.Game_Name,
            Game.Game_Genre,
            UserGame.Playtime,
            UserGame.Achievements,
            UserGame.Rating
        FROM UserGame
        JOIN Game ON UserGame.GameID = Game.GameID
        WHERE UserGame.Rating >= 7
        ORDER BY UserGame.Rating DESC
    """)
    top_rated_games = c.fetchall()
    conn.close()
    return render_template('top_rated_games.html', games=top_rated_games)



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
    error = None  # No error message to start with

    # handle form submission
    if form.validate_on_submit():
        # check if the game is already in the UserGame table
        c.execute("SELECT * FROM UserGame WHERE GameID = ?", (form.game.data,))
        game = c.fetchone()

        if game:
            error = 'This game is already in your library!'
        else:
            # insert the new game into the UserGame table
            c.execute("INSERT INTO UserGame (GameID, Difficulty, Playtime, Achievements, Rating, Date_Added) VALUES (?, ?, ?, ?, ?, date('now'))",
                      (form.game.data, form.difficulty.data, form.playtime.data, form.achievements.data, form.rating.data))
            conn.commit()
            flash('Game added successfully!')
            return redirect(url_for('home'))

    conn.close()

    # render the form
    return render_template('add_game.html', form=form, error=error)




@app.route('/edit-game/<int:game_id>', methods=['GET', 'POST'])
def edit_game(game_id):
   # connect to the database
   conn = sqlite3.connect('CS4750Project.db')
   c = conn.cursor()


   # retrieve the game from the UserGame table
   c.execute("SELECT * FROM UserGame WHERE UserGameID = ?", (game_id,))
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
       c.execute("UPDATE UserGame SET Difficulty = ?, Playtime = ?, Achievements = ?, Rating = ? WHERE UserGameID = ?",
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
   c.execute("DELETE FROM UserGame WHERE UserGameID = ?", (game_id,))
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
   c.execute("SELECT UserGameID, Game.Game_Name FROM UserGame JOIN Game ON UserGame.GameID = Game.GameID WHERE UserGameID = ?",
             (game_id,))
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

    error = None

    if form.validate_on_submit():
        # Check if the game is already in the wishlist
        c.execute("SELECT * FROM WishListGame WHERE WLG_GameID = ?", (form.game.data,))
        existing_game = c.fetchone()

        if existing_game is None:
            # Insert the game into the Wishlist table
            c.execute("INSERT INTO WishListGame (WLG_GameID, WLG_Priority) VALUES (?, ?)",
                      (form.game.data, form.priority.data))
            conn.commit()

            flash('Game added to wishlist successfully!')
            return redirect(url_for("wishlist"))
        else:
            error = 'This game is already in your wishlist'

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
    return render_template("wishlist.html", form=form, wishlist=wishlist, error=error)




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







