from dbUtils import *
connection = create_db_connection("daitv12")
def film_for_year(connection):
    q = """SELECT COUNT(*), Year FROM `film` GROUP BY Year;"""
    result = read_query(connection, q)
    return result

def film_for_genre(connection):
    q = """SELECT generi.Genere, COUNT(generirel.FilmID) FROM `generi`
        JOIN generirel ON generi.GenreID = generirel.GenreID
        GROUP BY generirel.GenreID;"""
    result = read_query(connection, q)
    return result

def user_for_province(connection):
    q = """SELECT COUNT(*), Province FROM `utenti`
        GROUP BY Province
        ORDER BY COUNT(*) DESC
        LIMIT 20;"""
    result = read_query(connection, q)
    return result

def user_for_work(connection):
    q = """SELECT COUNT(*), Work FROM `utenti`
        GROUP BY Work
        ORDER BY COUNT(*) DESC;"""
    result = read_query(connection, q)
    return result


def film_3(connection):
    q = """SELECT Title, COUNT(Rating) FROM film 
    JOIN rating ON film.FilmID = rating.FilmID 
    WHERE Rating < 3 GROUP BY Title HAVING COUNT(Rating) > 250;"""
    result = read_query(connection, q)
    return result


def film_age_gender(connection):
    q = """SELECT film.Title, utenti.Age_groups, utenti.Gender FROM film 
        JOIN rating ON rating.FilmID = film.FilmID 
        JOIN utenti ON utenti.UserID = rating.UserID
        GROUP BY film.Title, utenti.Age_groups, utenti.Gender 
        ORDER BY SUM(rating.Rating);"""
    result = read_query(connection, q)
    return result


def film_age_groups(connection):
    q = """SELECT film.Title, utenti.Age_groups, SUM(rating.Rating) FROM film 
        JOIN rating ON film.FilmID = rating.FilmID
        JOIN utenti ON utenti.UserID = rating.UserID
        GROUP BY film.Title, utenti.Age_groups
        ORDER BY SUM(rating.Rating)  """
    result = read_query(connection, q)
    return result