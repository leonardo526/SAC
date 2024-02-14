from dbUtils import *

connection = create_server_connection()
create_database(connection, "CREATE DATABASE Daitv12")
connection = create_db_connection("Daitv12")

utenti = """CREATE TABLE utenti(
            UserID int PRIMARY KEY AUTO_INCREMENT,
            Gender varchar(15) CHECK (Gender = 'male' OR Gender = 'female' OR Gender = 'other'),
            Age int CHECK (Age > 0 AND Age < 120),
            CAP varchar(6) NOT NULL,
            Province VARCHAR(50),
            Work varchar(255) NOT NULL,
            Age_groups varchar(45)
            );"""
film = """CREATE TABLE film(
            FilmID int PRIMARY KEY AUTO_INCREMENT,
            Title varchar(255) NOT NULL,
            OriginalTitle varchar(255),
            Year int NOT NULL,
            Average_rating DECIMAL(10,2)
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
            FOREIGN KEY (UserID) REFERENCES utenti(UserID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (FilmID) REFERENCES film(FilmID) ON DELETE CASCADE ON UPDATE CASCADE
            );"""

execute_query(connection, utenti)
execute_query(connection, film)
execute_query(connection, generi)
execute_query(connection, rating)
execute_query(connection, generiRel)

trigger1 = """
CREATE TRIGGER utenti_after_insert
BEFORE INSERT ON utenti
FOR EACH ROW
BEGIN
    IF NEW.Age < 18 THEN 
        SET NEW.Age_groups = 'under 18';
    ELSEIF NEW.Age >= 18 AND NEW.Age < 25 THEN
        SET NEW.Age_groups = '18-24';
    ELSEIF NEW.Age >= 25 AND NEW.Age < 35 THEN 
        SET NEW.Age_groups = '25-34';
    ELSEIF NEW.Age >= 35 AND NEW.Age < 45 THEN
        SET NEW.Age_groups = '35-44';
    ELSEIF NEW.Age >= 45 AND NEW.Age < 55 THEN
        SET NEW.Age_groups = '45-54';
    ELSE
        SET NEW.Age_groups = 'over 55';
    END IF;
END;
"""

trigger2= """
CREATE TRIGGER Average_rating
AFTER INSERT 
ON rating
FOR EACH ROW
BEGIN
DECLARE num_valutazioni INT;
DECLARE somma_valutazioni FLOAT;
     -- Calcola il numero totale delle valutazioni e la somma dei punteggi
    SELECT COUNT(*), SUM(Rating)
    INTO num_valutazioni, somma_valutazioni
    FROM rating
    WHERE FilmID = NEW.FilmID;

    -- Calcola la nuova media delle valutazioni
    SET @nuova_media = IF(num_valutazioni > 0, somma_valutazioni / num_valutazioni, 0);

    -- Aggiorna la colonna media_valutazione nella tabella film
    UPDATE film
    SET film.Average_rating = @nuova_media
    WHERE FilmID = NEW.FilmID;
END;
"""


execute_query(connection, trigger1)
execute_query(connection, trigger2)
