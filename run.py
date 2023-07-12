



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

    # User_Game_Library Table
   table = """ CREATE TABLE UserGame (
       UGID INTEGER PRIMARY,
       UG_GameID INTEGER,
       Difficulty STRING,
       Playtime INTEGER,
       Achievements TEXT,
       Rating INTEGER,
       Review TEXT,
       Date_Added DATE,
       FOREIGN KEY (UG_GameID) REFERENCES Game (GameID)
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
       MMORPG_Total_Attributes INTEGER,
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
   # cursor_obj.execute("DROP TABLE IF EXISTS Platformer")
   # connection_obj.commit()
   table = """ CREATE TABLE Platformer (
       PlatformerID INTEGER PRIMARY KEY AUTOINCREMENT,
       Platformer_GameID INTEGER,
       Platformer_Momentum_Based TEXT,
       Platformer_Total_Levels INTEGER,
       Platformer_Total_Environments INTEGER,
       FOREIGN KEY (Platformer_GameID) REFERENCES Game (GameID)
   ); """
   cursor_obj.execute(table)

   cursor_obj.executescript("""
      
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Celeste", "Platformer", "Matt Makes Games", "2018-01-25", "Switch", 19.99);
       INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments)
       VALUES (last_insert_rowid(), "Yes", 9, 5);

        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
        VALUES ("Call of Duty: Warzone", "Shooter", "Infinity Ward", "2020-03-10", "PC", 0);
        INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
        VALUES (last_insert_rowid(), "First Person", 1, "Yes", "Battle Royale, Plunder");
        
    
        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
        VALUES ("Final Fantasy XIV Online", "MMORPG", "Square Enix", "2010-09-30", "PC", 29.99);
        INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
        VALUES (last_insert_rowid(), 28, 12);
        
  
        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
        VALUES ("Forza Horizon 4", "Racing", "Playground Games", "2018-10-02", "Xbox One", 59.99);
        INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
        VALUES (last_insert_rowid(), 1, 450, 30);
    
    
        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
        VALUES ("Resident Evil 2 Remake", "Horror", "Capcom", "2019-01-25", "PC", 39.99);
        INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
        VALUES (last_insert_rowid(), 4, 5);
    
    
    
        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
        VALUES ("World of Warcraft: Shadowlands", "MMORPG", "Blizzard Entertainment", "2020-11-23", "PC", 39.99);
        INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
        VALUES (last_insert_rowid(), 30, 12);
    
        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
        VALUES ("NBA 2K22", "Sports", "Visual Concepts", "2021-09-10", "PS5", 59.99);
        INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
        VALUES (last_insert_rowid(), "Basketball", 1);
   
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("The Witcher 3: Wild Hunt", "RPG", "CD Projekt", "2015-05-19", "PC", 39.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 24, 3);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Overwatch", "Shooter", "Blizzard Entertainment", "2016-05-24", "PC", 39.99);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "First Person", 0, "Yes", "Competitive, Quick Play");

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Amnesia: The Dark Descent", "Horror", "Frictional Games", "2010-09-08", "PC", 19.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 5, 5);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Gran Turismo Sport", "Racing", "Polyphony Digital", "2017-10-17", "PS4", 39.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 1, 280, 82);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Mass Effect 2", "RPG", "BioWare", "2010-01-26", "PC", 19.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 20, 6);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Silent Hill 2", "Horror", "Konami", "2001-09-24", "PS2", 29.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 4, 5);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Counter-Strike: Global Offensive", "Shooter", "Valve", "2012-08-21", "PC", 0);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "First Person", 1, "Yes", "Competitive, Casual");

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Resident Evil 7: Biohazard", "Horror", "Capcom", "2017-01-24", "PC", 29.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 5, 4);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Final Fantasy XIV: A Realm Reborn", "MMORPG", "Square Enix", "2013-08-27", "PC", 19.99);
       INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
       VALUES (last_insert_rowid(), 26, 8);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Super Smash Bros. Ultimate", "Fighting", "Nintendo", "2018-12-07", "Switch", 59.99);
       INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance)
       VALUES (last_insert_rowid(), "Multiplayer", 3);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("DiRT Rally 2.0", "Racing", "Codemasters", "2019-02-26", "PC", 39.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 1, 75, 82);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("NHL 22", "Sports", "EA Vancouver", "2021-10-15", "PS5", 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "Ice Hockey", 1);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("The Legend of Zelda: Breath of the Wild", "RPG", "Nintendo", "2017-03-03", "Switch", 59.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 14, 2);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Outlast", "Horror", "Red Barrels", "2013-09-04", "PC", 19.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 5, 4);

       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Black Desert Online", "MMORPG", "Pearl Abyss", "2015-12-17", "PC", 9.99);
       INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
       VALUES (last_insert_rowid(), 18, 11);
       
        INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Call of Duty: Modern Warfare", "Shooter", "Infinity Ward", "2019-10-25", "PC", 59.99);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "First Person", 1, "Yes", "Campaign, Multiplayer");
   
   
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("The Elder Scrolls V: Skyrim", "RPG", "Bethesda Game Studios", "2011-11-11", "PC", 39.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 18, 10);
   
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Dead Space", "Horror", "Visceral Games", "2008-10-14", "PC", 19.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 5, 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('Star Wars: The Old Republic', 'MMORPG', 'BioWare', '2011-12-20', 'PC', 0);
       INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
       VALUES (last_insert_rowid(), 28, 8);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('Mortal Kombat 11', 'Fighting', 'NetherRealm Studios', '2019-04-23', 'PS4', 39.99);
       INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance)
       VALUES (last_insert_rowid(), 'Single Player, Multiplayer', 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('WRC 9', 'Racing', 'KT Racing', '2020-09-03', 'PC', 49.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 1, 52, 14);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('NBA 2K21', 'Sports', 'Visual Concepts', '2020-09-04', 'PS4', 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), 'Basketball', 1);
   
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('The Witcher 2: Assassins of Kings', 'RPG', 'CD Projekt', '2011-05-17', 'PC', 19.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 18, 3);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('Apex Legends', 'Shooter', 'Respawn Entertainment', '2019-02-04', 'PC', 0);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), 'First Person', 0, 'Yes', 'Battle Royale, Arena');
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('Until Dawn', 'Horror', 'Supermassive Games', '2015-08-25', 'PS4', 19.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 3, 4);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('World of Warcraft: Battle for Azeroth', 'MMORPG', 'Blizzard Entertainment', '2018-08-14', 'PC', 39.99);
       INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
       VALUES (last_insert_rowid(), 28, 12);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('Dragon Ball FighterZ', 'Fighting', 'Arc System Works', '2018-01-26', 'Xbox One', 39.99);
       INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance)
       VALUES (last_insert_rowid(), 'Single Player, Multiplayer', 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('WRC 10', 'Racing', 'KT Racing', '2021-09-02', 'PC', 49.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 1, 52, 20);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ('Madden NFL 22', 'Sports', 'EA Tiburon', '2021-08-20', 'PS5', 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), 'American Football', 1);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Super Mario Odyssey", "Platformer", "Nintendo", "2017-10-27", "Switch", 59.99);
       INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments)
       VALUES (last_insert_rowid(), "Yes", 12, 6);
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Ori and the Will of the Wisps", "Platformer", "Moon Studios", "2020-03-11", "Xbox One", 29.99);
       INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments)
       VALUES (last_insert_rowid(), "Yes", 10, 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Little Nightmares", "Horror", "Tarsier Studios", "2017-04-28", "PC", 19.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 3, 4);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Yoshi's Crafted World", "Platformer", "Good-Feel", "2019-03-29", "Switch", 59.99);
       INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments)
       VALUES (last_insert_rowid(), "Yes", 8, 4);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Destiny 2", "Shooter", "Bungie", "2017-09-06", "PC", 0);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "First Person", 0, "Yes", "Multiplayer");
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Need for Speed Heat", "Racing", "Ghost Games", "2019-11-08", "PC", 59.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 0, 127, 18);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Pokémon Sword and Shield", "RPG", "Game Freak", "2019-11-15", "Switch", 59.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 15, 3);
       
   
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("FIFA 22", "Sports", "EA Sports", "2021-09-27", "PS5", 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "Football", 1);
      
   
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Fall Guys: Ultimate Knockout", "Platformer", "Mediatonic", "2020-08-04", "PC", 19.99);
       INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments)
       VALUES (last_insert_rowid(), "Yes", 25, 10);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Cyberpunk 2077", "RPG", "CD Projekt", "2020-12-10", "PC", 59.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 25, 8);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Resident Evil 8: Village", "Horror", "Capcom", "2021-05-07", "PS5", 59.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 5, 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Valorant", "Shooter", "Riot Games", "2020-06-02", "PC", 0);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "First Person", 0, "Yes", "Multiplayer");
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("F1 2021", "Racing", "Codemasters", "2021-07-16", "PS4", 59.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 1, 20, 23);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("PGA Tour 2K21", "Sports", "HB Studios", "2020-08-21", "PC", 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "Golf", 1);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Resident Evil Village", "Horror", "Capcom", "2021-05-07", "PC", 59.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 5, 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Tekken 7", "Fighting", "Bandai Namco Entertainment", "2015-02-18", "PS4", 49.99);
       INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance)
       VALUES (last_insert_rowid(), "Single Player, Multiplayer", 5);
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("The Elder Scrolls VI", "RPG", "Bethesda Game Studios", "TBD", "PC", 59.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 20, 6);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Gears of War 5", "Shooter", "The Coalition", "2019-09-10", "Xbox One", 59.99);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "Third Person", 0, "Yes", "Multiplayer");
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("NHL 23", "Sports", "EA Sports", "2022-09-30", "PS5", 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "Ice Hockey", 1);
     
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Outlast 2", "Horror", "Red Barrels", "2017-04-25", "PC", 29.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 4, 5);
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Black Desert Remastered", "MMORPG", "Pearl Abyss", "2018-08-22", "PC", 9.99);
       INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
       VALUES (last_insert_rowid(), 34, 14);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Call of Duty: Black Ops Cold War", "Shooter", "Treyarch", "2020-11-13", "PC", 59.99);
       INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes)
       VALUES (last_insert_rowid(), "First Person", 0, "Yes", "Multiplayer");
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("FIFA 23", "Sports", "EA Sports", "2022-09-30", "PS5", 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "Football", 1);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Mortal Kombat 12", "Fighting", "NetherRealm Studios", "TBD", "Xbox Series X", 59.99);
       INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance)
       VALUES (last_insert_rowid(), "Single Player, Multiplayer", 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Rocket League", "Sports", "Psyonix", "2015-07-07", "PC", 0);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "Soccer", 0);
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Dead Space Remake", "Horror", "EA Motive", "TBD", "PC", 59.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 4, 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Star Wars: Knights of the Old Republic Remake", "RPG", "Aspyr", "TBD", "PS5", 59.99);
       INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes)
       VALUES (last_insert_rowid(), 25, 8);
      
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Until Dawn: Rush of Blood", "Horror", "Supermassive Games", "2016-10-13", "PS4", 19.99);
       INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level)
       VALUES (last_insert_rowid(), 4, 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("World of Warcraft: The Burning Crusade Classic", "MMORPG", "Blizzard Entertainment", "2021-06-01", "PC", 0);
       INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes)
       VALUES (last_insert_rowid(), 30, 10);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Dragon Ball Xenoverse 3", "Fighting", "Bandai Namco Entertainment", "TBD", "Xbox Series X", 59.99);
       INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance)
       VALUES (last_insert_rowid(), "Single Player, Multiplayer", 5);
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("WRC 11", "Racing", "KT Racing", "TBD", "PS5", 59.99);
       INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks)
       VALUES (last_insert_rowid(), 1, 60, 15);
       
       
       INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price)
       VALUES ("Madden NFL 23", "Sports", "EA Tiburon", "2022-08-19", "Xbox Series X", 59.99);
       INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic)
       VALUES (last_insert_rowid(), "American Football", 1);

   """)

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer,Game_Release_Date, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?,?)",
       ("Soulcalibur VI", "Fighting", "Bandai Namco Entertainment", "2010-10-25", "Xbox Series X", 49.99))

   game_id = cursor_obj.lastrowid  # Retrieve the last inserted GameID

   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (game_id, "Versus", 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Doom", "Shooter", "id Software", "PC", 19.99))

   doom_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (doom_game_id, "First-person", 1, "Yes", "Single-player, Multiplayer"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Animal Crossing", "MMORPG", "Nintendo", "Switch", 59.99))

   animal_crossing_game_id = cursor_obj.lastrowid

   cursor_obj.execute("INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
                      (animal_crossing_game_id, 0, 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("The Witcher 3", "MMORPG", "CD Projekt Red", "PC", 29.99))

   the_witcher_game_id = cursor_obj.lastrowid

   cursor_obj.execute("INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
                      (the_witcher_game_id, 1, '3'))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Doom", "Shooter", "id Software", "PC", 19.99))

   doom_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (doom_game_id, "First-person", "Yes", "Yes", "Single-player, Multiplayer"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("FIFA 22", "Sports", "EA Sports", "PS5", 59.99))

   fifa_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic) VALUES (?, ?, ?)",
       (fifa_game_id, "Football", 1))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Forza Horizon 5", "Racing", "Playground Games", "Xbox Series X", 69.99))

   forza_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks) VALUES (?, ?, ?, ?)",
       (forza_game_id, 1, 500, 100))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Super Mario Odyssey", "Platformer", "Nintendo", "Switch", 59.99))

   mario_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (mario_game_id, "Yes", 60, 5))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Tekken 7", "Fighting", "Bandai Namco Entertainment", "PS4", 39.99))

   tekken_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (tekken_game_id, "Versus", 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Resident Evil 2", "Horror", "Capcom", "PC", 39.99))

   re2_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level) VALUES (?, ?, ?)",
       (re2_game_id, 9, 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Silent Hill 2", "Horror", "Konami", "PS2", 19.99))

   silent_hill_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level) VALUES (?, ?, ?)",
       (silent_hill_game_id, 7, 9))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Elder Scrolls Online", "MMORPG", "Zenimax Online Studios", "PC", 29.99))

   elder_scrolls_game_id = cursor_obj.lastrowid

   cursor_obj.execute("INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
                      (elder_scrolls_game_id, 0, '4'))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Guild Wars 2", "MMORPG", "ArenaNet", "PC", 19.99))

   guild_wars_game_id = cursor_obj.lastrowid

   cursor_obj.execute("INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
                      (guild_wars_game_id, 0, '2'))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Final Fantasy XIV", "MMORPG", "Square Enix", "PC", 39.99))

   final_fantasy_game_id = cursor_obj.lastrowid

   cursor_obj.execute("INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
                      (final_fantasy_game_id, 0, '5'))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Battlefield 2042", "Shooter", "DICE", "PC", 59.99))

   battlefield_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (battlefield_game_id, "First-person", "Yes", "Yes", "Multiplayer"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Rainbow Six Siege", "Shooter", "Ubisoft", "PC", 19.99))

   rainbow_six_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (rainbow_six_game_id, "First-person", "Yes", "Yes", "Multiplayer"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Borderlands 3", "Shooter", "Gearbox Software", "PC", 49.99))

   borderlands_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (borderlands_game_id, "First-person", "No", "No", "Single-player, Multiplayer"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Madden NFL 22", "Sports", "Electronic Arts", "PS5", 59.99))

   madden_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic) VALUES (?, ?, ?)",
       (madden_game_id, "American Football", 1))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("WWE 2K22", "Sports", "Visual Concepts", "Xbox Series X", 59.99))

   wwe_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic) VALUES (?, ?, ?)",
       (wwe_game_id, "Wrestling", 0))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("PGA Tour 2K21", "Sports", "HB Studios", "PC", 49.99))

   pga_tour_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic) VALUES (?, ?, ?)",
       (pga_tour_game_id, "Golf", 1))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Dirt 5", "Racing", "Codemasters", "PS5", 59.99))

   dirt_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks) VALUES (?, ?, ?, ?)",
       (dirt_game_id, 1, 100, 70))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Crash Team Racing Nitro-Fueled", "Racing", "Beenox", "Switch", 39.99))

   crash_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks) VALUES (?, ?, ?, ?)",
       (crash_game_id, 0, 40, 21))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("F1 2021", "Racing", "Codemasters", "PC", 49.99))

   f1_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks) VALUES (?, ?, ?, ?)",
       (f1_game_id, 1, 20, 23))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Ori and the Will of the Wisps", "Platformer", "Moon Studios", "Xbox Series X", 29.99))

   ori_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (ori_game_id, "Yes", 50, 5))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Little Nightmares II", "Platformer", "Tarsier Studios", "PC", 29.99))

   nightmares_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (nightmares_game_id, "No", 30, 3))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Yooka-Laylee and the Impossible Lair", "Platformer", "Playtonic Games", "Switch", 39.99))

   yooka_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (yooka_game_id, "Yes", 40, 4))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Dragon Ball FighterZ", "Fighting", "Arc System Works", "PS4", 39.99))

   dragon_ball_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (dragon_ball_game_id, "Versus", 9))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Street Fighter V", "Fighting", "Capcom", "PC", 19.99))

   street_fighter_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (street_fighter_game_id, "Versus", 7))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Soulcalibur VI", "Fighting", "Bandai Namco Entertainment", "Xbox Series X", 49.99))

   soulcalibur_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (soulcalibur_game_id, "Versus", 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Amnesia: Rebirth", "Horror", "Frictional Games", "PC", 29.99))

   amnesia_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level) VALUES (?, ?, ?)",
       (amnesia_game_id, 8, 9))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Alien: Isolation", "Horror", "Creative Assembly", "PS4", 19.99))

   alien_game_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level) VALUES (?, ?, ?)",
       (alien_game_id, 9, 9))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Dead by Daylight", "Horror", "Behaviour Interactive", "PC", 19.99))

   dead_by_daylight_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level) VALUES (?, ?, ?)",
       (dead_by_daylight_id, 7, 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Red Dead Redemption 2", "Action Adventure", "Rockstar Games", "PS4", 39.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Call of Duty: Modern Warfare", "First-person shooter", "Infinity Ward", "PC", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Among Us", "Party game", "InnerSloth", "PC", 4.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Grand Theft Auto V", "Action Adventure", "Rockstar Games", "PS4", 29.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Minecraft", "Sandbox", "Mojang Studios", "PC", 26.95))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("The Legend of Zelda: Breath of the Wild", "Action Adventure", "Nintendo", "Switch", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Super Smash Bros. Ultimate", "Fighting", "Nintendo", "Switch", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("God of War", "Action Adventure", "Santa Monica Studio", "PS4", 19.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Fortnite", "Battle Royale", "Epic Games", "PC", 0.00))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("PlayerUnknown's Battlegrounds", "Battle Royale", "PUBG Corporation", "PC", 29.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Overwatch", "First-person shooter", "Blizzard Entertainment", "PC", 39.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Cyberpunk 2077", "Role-playing", "CD Projekt", "PC", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Horizon Zero Dawn", "Action role-playing", "Guerrilla Games", "PS4", 19.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("The Last of Us Part II", "Action-adventure", "Naughty Dog", "PS4", 39.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Final Fantasy VII Remake", "Role-playing", "Square Enix", "PS4", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Super Mario Odyssey", "Platform", "Nintendo", "Switch", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Animal Crossing: New Horizons", "Social simulation", "Nintendo", "Switch", 59.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Death Stranding", "Action", "Kojima Productions", "PS4", 39.99))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Apex Legends", "Battle Royale", "Respawn Entertainment", "PC", 0.00))
   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?)",
       ("Fall Guys: Ultimate Knockout", "Platform", "Mediatonic", "PC", 19.99))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?, ?)",
       ("Mortal Kombat 11", "Fighting", "NetherRealm Studios", "2019 - 4 - 23", "Xbox Series X", 59.99))

   mk11_game_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (mk11_game_id, "Versus", 10))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Marvel's Spider-Man: Miles Morales", "Fighting", "Insomniac Games", "2020-11-12", "PlayStation 5", 49.99))

   spiderman_miles_morales_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (spiderman_miles_morales_id, 7, 8))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Kingdom Hearts III", "RPG", "Square Enix", "2019-01-29", "PlayStation 4", 59.99))

   kingdom_hearts_III_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (kingdom_hearts_III_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("The Elder Scrolls V: Skyrim", "RPG", "Bethesda Game Studios", "2011-11-11", "Various", 39.99))

   skyrim_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (skyrim_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Resident Evil Village", "Horror", "Capcom", "2021-05-07", "PlayStation 4", 59.99))

   resident_evil_village_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Horror (Horror_GameID, Horror_Jump_Scare_Rating, Horror_Suspense_Level) VALUES (?, ?, ?)",
       (resident_evil_village_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Super Mario 3D World + Bowser's Fury", "Platform", "Nintendo", "2021-02-12", "Nintendo Switch", 59.99))

   mario_3d_world_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (mario_3d_world_id, "7", "8", "50"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Hades", "MMORPG", "Supergiant Games", "2020-09-17", "PlayStation 4", 24.99))

   hades_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
       (hades_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Ghost of Tsushima", "Fighting", "Sucker Punch Productions", "2020-07-17", "PlayStation 4", 59.99))

   ghost_of_tsushima_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (ghost_of_tsushima_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Halo", "Shooter", "Bungie, 343 Industries", "2001-11-15", "Xbox, Xbox 360, Xbox One", 59.99))

   halo_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (halo_id, "1", "7", "Yes", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("World of Warcraft", "MMORPG", "Blizzard Entertainment", "2004-11-23", "PC", 14.99))

   world_of_warcraft_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
       (world_of_warcraft_id, "15", "Azeroth"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Destiny 2", "Shooter", "Bungie", "2017-09-06", "PlayStation 4, Xbox One, PC", 0.00))

   destiny_2_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (destiny_2_id, "1", "2", "Yes", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Stardew Valley", "MMORPG", "ConcernedApe", "2016-02-26", "Switch", 14.99))

   stardew_valley_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
       (stardew_valley_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("League of Legends", "MMORPG", "Riot Games", "2009-10-27", "PC", 0.00))

   league_of_legends_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO MMORPG (MMORPG_GameID, MMORPG_Total_Attributes, MMORPG_Classes) VALUES (?, ?, ?)",
       (league_of_legends_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Counter-Strike: Global Offensive", "Shooter", "Valve Corporation, Hidden Path Entertainment", "2012-08-21",
        "PC", 0.00))

   counter_strike_go_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (counter_strike_go_id, "1", "8", "Yes", "1"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("The Sims 4", "Life simulation", "Maxis, The Sims Studio", "2014-9-2", "PC, Mac, PlayStation 4, Xbox One",
        39.99))

   the_sims_4_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (the_sims_4_id, "3", "12"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Dark Souls III", "RPG", "FromSoftware", "2016-03-24", "PlayStation 4, Xbox One, PC", 59.99))

   dark_souls_III_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (dark_souls_III_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Fire Emblem: Engage", "RPG", "Intelligent Systems, Nintendo EPD", "2023-1-20", "Nintendo Switch", 59.99))

   fire_emblem_engage_id = cursor_obj.lastrowid

   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (fire_emblem_engage_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Super Mario Maker 2", "Platform", "Nintendo", "2019-06-28", "Nintendo Switch", 59.99))

   super_mario_maker_2_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (super_mario_maker_2_id, "7", "120", "10"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Fire Emblem: Three Houses", "RPG", "Intelligent Systems, Koei Tecmo Games", "2019-07-26", "Nintendo Switch",
        59.99))

   fire_emblem_three_houses_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",

       (fire_emblem_three_houses_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Ultimate Marvel vs Capcom 3", "Fighting", "Capcom", "2011-11-15", "PlayStation 4", 24.99))

   marvel_vs_capcom_3_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (marvel_vs_capcom_3_id, "3", "9"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Xenoblade Chronicles 2", "RPG", "Monolith Soft", "2017-1-12", "Nintendo Switch", 59.99))

   xenoblade_chronicles_2_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (xenoblade_chronicles_2_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Dragon Quest XI", "RPG", "Square Enix", "2017-7-29", "Nintendo Switch", 59.99))

   dragon_quest_XI_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (dragon_quest_XI_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Marvel vs Capcom: Infinite", "Fighting", "Capcom", "2017-9-19", "PlayStation 4", 39.99))

   marvel_vs_capcom_infinite_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (marvel_vs_capcom_infinite_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Injustice 2", "Fighting", "NetherRealm Studios", "2017-5-11", "PlayStation 4", 19.99))

   injustice_2_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (injustice_2_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Bloodborne", "RPG", "FromSoftware Inc", "2015–3-24", "PlayStation 4", 19.99))

   bloodborne_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (bloodborne_id, "5", "6"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Arms", "Fighting", "Nintendo", "2017-6-16", "Nintendo Switch", 59.99))

   arms_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (arms_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Hyrule Warriors: Age of Calamity", "Fighting", "Omega Force", "2020-11-20", "Nintendo Switch", 59.99))

   hyrule_warriors_age_of_calamity_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (hyrule_warriors_age_of_calamity_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Metroid Dread", "Shooter", "Nintendo", "2021–10-8", "Nintendo Switch", 59.99))

   metroid_dread_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (metroid_dread_id, "1", "2", "No", "1"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Kirby and the Forgotten Land", "Platform", "HAL Laboratory", "2022–3-25", "Nintendo Switch", 59.99))

   kirby_and_the_forgotten_land_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (kirby_and_the_forgotten_land_id, "5", "100", "5"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Bayonetta 3", "Fighting", "PlatinumGames", "2022-10-28", "Nintendo Switch", 59.99))

   bayonetta_3_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (bayonetta_3_id, "5", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Metroid Prime Remastered", "Shooter", "Nintendo", "2023–2-8", "Nintendo Switch", 59.99))

   metroid_prime_remastered_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (metroid_prime_remastered_id, "1", "2", "No", "1"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Just Dance 2022", "Sport", "Ubisoft Paris", "2021–11-4", "Nintendo Switch", 49.99))

   just_dance_2022_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic) VALUES (?, ?, ?)",
       (just_dance_2022_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Octopath Traveler", "RPG", "Square Enix", "2018–7-13", "Nintendo Switch", 59.99))

   octopath_traveler_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (octopath_traveler_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Monster Hunter Rise", "RPG", "Capcom", "2021–3-26", "Nintendo Switch", 39.99))

   monster_hunter_rise_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (monster_hunter_rise_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Kirby Fighters 2", "Fighting", "HAL Laboratory", "2020-9-23", "Nintendo Switch", 19.99))

   kirby_fighters_2_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (kirby_fighters_2_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Luigi’s Mansion 3", "Shooter", "Next Level Games", "2019–10-31", "Nintendo Switch", 59.99))

   luigi_mansion_3_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Shooter (Shooter_GameID, Shooter_Perspective, Shooter_Realistic, Shooter_Ranked, Shooter_Game_Modes) VALUES (?, ?, ?, ?, ?)",
       (luigi_mansion_3_id, "3", "1", "No", "1"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Captain Toad: Treasure Tracker", "Platform", "Nintendo", "2014-11-13", "Nintendo Switch", 39.99))

   captain_toad_treasure_tracker_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (captain_toad_treasure_tracker_id, "8", "50", "5"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Yoshi’s Crafted World", "Platform", "Good-Feel", "2019-3-29", "Nintendo Switch", 59.99))

   yoshi_crafted_world_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (yoshi_crafted_world_id, "6", "80", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Donkey Kong Country: Tropical Freeze", "Platform", "Retro Studios", "2014–2-13", "Nintendo Switch", 59.99))

   donkey_kong_country_tropical_freeze_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Platformer (Platformer_GameID, Platformer_Momentum_Based, Platformer_Total_Levels, Platformer_Total_Environments) VALUES (?, ?, ?, ?)",
       (donkey_kong_country_tropical_freeze_id, "10", "60", "6"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Mario Strikers: Battle League", "Sport", "Next Level Games", "2022–6-10", "Nintendo Switch", 59.99))

   mario_strikers_battle_league_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Sports (Sports_GameID, Sports_Sport, Sports_Realistic) VALUES (?, ?, ?)",
       (mario_strikers_battle_league_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Mario + Rabbits Sparks of Hope", "RPG", "Ubisoft Milan", "2022–10-20", "Nintendo Switch", 59.99))

   mario_rabbits_sparks_of_hope_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (mario_rabbits_sparks_of_hope_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Pokémon Legends: Arceus", "RPG", "Game Freak", "2022–1-28", "Nintendo Switch", 59.99))

   pokémon_legends_arceus_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (pokémon_legends_arceus_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Legend of Zelda: Skyward Sword", "Fighting", "Nintendo", "2011-11-18", "Nintendo Switch", 59.99))

   legend_of_zelda_skyward_sword_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Fighting (Fighting_GameID, Fighting_Game_Modes, Fighting_Combo_Importance) VALUES (?, ?, ?)",
       (legend_of_zelda_skyward_sword_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?,?,?,?,?,?)",
       ("Legend of Zelda: Link’s Awakening", "RPG", "Nintendo", "2019–9-20", "Nintendo Switch", 59.99))

   legend_of_zelda_link_awakening_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO RPG (RPG_GameID, RPG_Total_Attributes, RPG_Classes) VALUES (?, ?, ?)",
       (legend_of_zelda_link_awakening_id, "7", "8"))

   cursor_obj.execute(
       "INSERT INTO Game (Game_Name, Game_Genre, Game_Developer, Game_Release_Date, Game_Platform, Game_Price) VALUES (?, ?, ?, ?, ?, ?)",
       ("Kirby’s Dream Buffet", "Racing", "HAL Laboratory", "2022–8-17", "Switch", 14.99))

   kirbys_dream_buffet_id = cursor_obj.lastrowid
   cursor_obj.execute(
       "INSERT INTO Racing (Racing_GameID, Racing_Realistic, Racing_Num_Vehicles, Racing_Num_Tracks) VALUES (?, ?, ?, ?)",
       (kirbys_dream_buffet_id, 0, 40, 21))


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

@app.route("/top-rated-games")
def top_rated_games():
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
        c.execute("SELECT * FROM UserGame WHERE UG_GameID = ?", (form.game.data,))
        game = c.fetchone()

        if game:
            error = 'This game is already in your library!'
        else:
            # insert the new game into the UserGame table
            c.execute("INSERT INTO UserGame (UG_GameID, Difficulty, Playtime, Achievements, Rating, Date_Added) VALUES (?, ?, ?, ?, ?, date('now'))",
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
   c.execute("SELECT UGID, Game.Game_Name FROM UserGame JOIN Game ON UserGame.UG_GameID = Game.GameID WHERE UGID = ?",
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







