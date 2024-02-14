import pandas as pd
from dbUtils import *


# utenti = """CREATE TABLE utenti(
#             UsersID int PRIMARY KEY AUTO_INCREMENT,
#             Gender varchar(15) CHECK (Gender = 'male' OR Gender = 'female' OR Gender = 'other'),
#             Age int CHECK (Age > 0),
#             CAP varchar(6) NOT NULL,
#             Work varchar(255) NOT NULL
#             );"""
# film = """CREATE TABLE film(
#             FilmID int PRIMARY KEY AUTO_INCREMENT,
#             Title varchar(255) NOT NULL,
#             OriginalTitle varchar(255),
#             Year int NOT NULL
#             );"""
# generi = """CREATE TABLE generi(
#             GenreID int PRIMARY KEY AUTO_INCREMENT,
#             Genere varchar(255) NOT NULL
#             );"""
# generiRel = """CREATE TABLE generiRel(
#             RelID int PRIMARY KEY AUTO_INCREMENT,
#             FilmID int,
#             GenreID int,
#             FOREIGN KEY (FilmID) REFERENCES film(FilmID),
#             FOREIGN KEY (GenreID) REFERENCES generi(GenreID)
#             );"""   
# rating = """CREATE TABLE rating(
#             RatingID int PRIMARY KEY AUTO_INCREMENT,
#             UserID int,
#             FilmID int,
#             Rating int,
#             FOREIGN KEY (UserID) REFERENCES utenti(UsersID),
#             FOREIGN KEY (FilmID) REFERENCES film(FilmID)
#             );"""
df = pd.read_csv("New_Elenco_Movies_Pulito.csv")
#ADD TO DB


for x in df.to_dict(orient="records"):
    c = create_db_connection('utenti')
    q = f"""INSERT INTO film (Title,OriginalTitle,Year) VALUES ("{x['Title']}","{x['Original Title']}",'{x['Year']}')"""
    execute_query(c,q)
    q = f"""SELECT FilmID FROM film WHERE Title = "{x['Title']}";"""
    resF = read_query(c,q)
    #print(resF)
    for y in x['Genres'].split("|"):
        q = f"""SELECT GenreID FROM generi WHERE Genere = "{y}";"""
        resG = read_query(c,q)
        if len(resG) == 0:
            q = f"""INSERT INTO generi (Genere) VALUES ("{y}")"""
            execute_query(c,q)
            q = f"""SELECT GenreID FROM generi WHERE Genere = "{y}";"""
            resG = read_query(c,q)
        q = f"INSERT INTO generiRel (FilmID,GenreID) VALUES ('{resF[0]['FilmID']}','{resG[0]['GenreID']}')"
        execute_query(c,q)
        
    c.close()
        
    
        


    




    c.close()

