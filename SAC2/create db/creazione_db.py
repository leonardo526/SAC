from dbUtils import *

connection = create_server_connection()
create_database(connection, "CREATE DATABASE utenti")
connection = create_db_connection("utenti")

utenti = """CREATE TABLE utenti(
            UserID int PRIMARY KEY AUTO_INCREMENT,
            Gender varchar(15) CHECK (Gender = 'male' OR Gender = 'female' OR Gender = 'other'),
            Age int CHECK (Age > 0 AND Age < 120),
            CAP varchar(6) NOT NULL,
            Work varchar(255) NOT NULL
            );"""
film = """CREATE TABLE film(
            FilmID int PRIMARY KEY AUTO_INCREMENT,
            Title varchar(255) NOT NULL,
            OriginalTitle varchar(255),
            Year int NOT NULL
            );"""
generi = """CREATE TABLE generi(
            GenreID int PRIMARY KEY AUTO_INCREMENT,
            Genere varchar(255) NOT NULL
            );"""
generiRel = """CREATE TABLE generiRel(
            RelID int PRIMARY KEY AUTO_INCREMENT,
            FilmID int,
            GenreID int,
            FOREIGN KEY (FilmID) REFERENCES film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (GenreID) REFERENCES generi(GenreID) ON DELETE CASCADE ON UPDATE CASCADE
            );"""   
rating = """CREATE TABLE rating(
            RatingID int PRIMARY KEY AUTO_INCREMENT,
            UserID int,
            FilmID int,
            Rating int,
            Timestamp int,
            FOREIGN KEY (UserID) REFERENCES utenti(UsersID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (FilmID) REFERENCES film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE
            );"""


execute_query(connection, utenti)
execute_query(connection, film)
execute_query(connection, rating)
execute_query(connection, generi)
execute_query(connection, generiRel)




