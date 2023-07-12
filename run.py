


from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, IntegerField, FloatField, SubmitField
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


   connection_obj.commit()


   connection_obj.close()


   return render_template("create_db.html")





class GameAddForm(FlaskForm):
   game = SelectField('Game', coerce=int, validators=[DataRequired()])
   difficulty = SelectField('Difficulty', choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Normal', 'Normal'),
                                                   ('Hard', 'Hard'), ('Very Hard', 'Very Hard')])
   playtime = IntegerField('Playtime (in hours)')
   achievements = IntegerField('Achievements (in %)', validators=[
       NumberRange(min=0, max=100, message="Achievements should be between 0 and 100%")])
   rating = IntegerField('Rating (0-10)',
                         validators=[NumberRange(min=0, max=10, message="Rating should be between 0 and 10")])
   submit = SubmitField('Add Game')




class GameEditForm(FlaskForm):
   difficulty = SelectField('Difficulty', choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Normal', 'Normal'),
                                                   ('Hard', 'Hard'), ('Very Hard', 'Very Hard')])
   playtime = IntegerField('Playtime (in hours)')
   achievements = IntegerField('Achievements (in %)', validators=[
       NumberRange(min=0, max=100, message="Achievements should be between 0 and 100%")])
   rating = IntegerField('Rating (0-10)',
                         validators=[NumberRange(min=0, max=10, message="Rating should be between 0 and 10")])
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


   # handle form submission
   if form.validate_on_submit():
       # insert the new game into the UserGame table
       c.execute(
           "INSERT INTO UserGame (UG_GameID, Difficulty, Playtime, Achievements, Rating, Date_Added) VALUES (?, ?, ?, ?, ?, date('now'))",
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







