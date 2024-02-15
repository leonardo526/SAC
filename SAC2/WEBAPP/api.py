from flask import Blueprint, request
from sys import path
path.append(r'C:\Users\Utente\PycharmProjects\pythonProjectSql\SAC\SAC2\create db')
from SAC.SAC2.MongoDB.dbUtils import *



apiBlueprint = Blueprint("apiBlueprint", __name__)

# --FILM--
@apiBlueprint.route('/api/getFilm', methods=['GET'])
def getMovies():

    page = int(request.args.get('page', default=1))
    items_per_page = 20
    offset = (page - 1) * items_per_page
    c = create_db_connection("daitv12")
    q = f"SELECT * FROM film LIMIT {items_per_page} OFFSET {offset};"
    res = read_query(c, q)
    c.close()
    return res

@apiBlueprint.route('/api/get_evaluation', methods=['GET'])
def get_evaluation():
    c = create_db_connection("daitv12")
    q = "SELECT * FROM film WHERE Average_rating > 4"
    res = read_query(c, q)
    c.close()
    return res

@apiBlueprint.route('/api/getFilmTop10', methods=['GET'])
def Top10Film():
    c = create_db_connection("daitv12")
    q = "SELECT * FROM film ORDER BY Average_rating DESC LIMIT 10"
    res = read_query(c, q)
    c.close()
    return res

@apiBlueprint.route('/api/getMovieByGenre', methods=['GET'])
def getMovieByGenre():
    genere = request.args.get('genere')
    c = create_db_connection("daitv12")
    q = f"""SELECT * FROM film JOIN generirel JOIN generi ON film.FilmID = generirel.FilmID AND generirel.GenreID = generi.GenreID WHERE generi.Genere = "{genere}"; """

# --GENERI--
@apiBlueprint.route('/api/getGeneri', methods=['GET'])
def getGeneri():
    page = int(request.args.get('page', default=1))
    items_per_page = 10
    offset = (page - 1) * items_per_page
    c = create_db_connection("daitv12")
    q = f"SELECT * FROM generi LIMIT {items_per_page} OFFSET {offset};"
    res = read_query(c, q)
    c.close()
    return res

# --OPERE--
@apiBlueprint.route('/api/getOpere', methods=['GET'])
def getWorks():
    # l = request.args.get("limit", default="20")
    # if type(l) != int:
    #     try:
    #         l = int(l)
    #     except:
    #         raise ValueError("Limit must be an integer")
    page = int(request.args.get('page', default=1))
    items_per_page = 20
    offset = (page - 1) * items_per_page
    c = create_db_connection(dbname)
    q = f"SELECT * FROM opere LIMIT {items_per_page} OFFSET {offset};"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getOpereByArtist', methods=['GET'])
def getOpereByArtist(n):
    if not n:
        n = request.args.get("name", type=str)
    print(n, type(n), "in api")
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    # q = f"SELECT * FROM artisti WHERE autore = '{n}';" #join creazione
    q = f"""
        - id_opera
    SELECT * FROM opere JOIN creazione JOIN artisti 
    ON artisti.id_artista = creazione.id_artista
    WHERE nome = '{n}';"""
    res = read_query(c, q)
    # print("in api",res)
    c.close()
    return res


@apiBlueprint.route('/api/getOpereByDate', methods=['GET'])
def getOpereByDate():
    y = request.args.get("year")
    if type(y) != int or type(y) != str or len(str(y)) < 3:
        raise ValueError("Year must be a 3/4-digit integer/string")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM opere WHERE YEAR(data_pubblicazione) = '{y}';"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getOpereByTimeSpan', methods=['GET'])
def getOpereByTimeSpan():
    s = request.args.get("start", type=str)
    e = request.args.get("end", type=str)
    if type(s) != int or type(s) != str or len(str(s)) < 3:
        raise ValueError("Year[start] must be a 3/4-digit integer/string")
    if type(e) != int or type(e) != str or len(str(e)) < 3:
        raise ValueError("Year[end] must be a 3/4-digit integer/string")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM opere WHERE YEAR(data_pubblicazione) BETWEEN '{s}' AND '{e}';"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getOpereUrl', methods=['GET'])
def getOpereUrl():
    t = request.args.get("limit", default="20")
    if type(t) != int:
        try:
            t = int(t)
        except:
            raise ValueError("Limit must be an integer")
    c = create_db_connection(dbname)
    q = f"SELECT url_immagine FROM opere LIMIT {t};"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getOpereUrl_byName', methods=['GET'])
def getOpereUrl_byName():
    n = request.args.get("name", type=str)
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    q = f"SELECT url_immagine FROM opere WHERE titolo = '{n}';"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getOpereUrl_byAuthor', methods=['GET'])
def getOpereUrl_byAuthor():
    n = request.args.get("name", type=str)
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    q = f"""SELECT url_immagine FROM opere JOIN creazione JOIN artisti 
		ON artisti.id_artista = creazione.id_artista AND creazione.id_opera = opere.id_opera
		WHERE nome = '{n}';"""
    res = read_query(c, q)
    c.close()
    return res


# --ARTISTI--
@apiBlueprint.route('/api/getArtisti', methods=['GET'])
def getArtisti():
    # l = request.args.get("limit", default="20")
    # if type(l) != int:
    #     try:
    #         l = int(l)
    #     except:
    #         raise ValueError("Limit must be an integer")
    page = int(request.args.get('page', default=1))
    items_per_page = 20
    offset = (page - 1) * items_per_page
    c = create_db_connection(dbname)
    q = f"SELECT * FROM artisti LIMIT {items_per_page} OFFSET {offset};"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getArtistaByName', methods=['GET'])
def getArtista():
    n = request.args.get("name", type=str)
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM artisti WHERE nome = '{n}';"
    res = read_query(c, q)
    c.close()
    return res


@apiBlueprint.route('/api/getArtistiByDate', methods=['GET'])
def getOpereByType():
    bod = request.args.get("bornOrDeath", default="born", type=str)
    d = request.args.get("date", type=str)
    if type(d) != int or type(d) != str or len(str(d)) < 3:
        raise ValueError("Year must be a 3/4-digit integer/string")
    if bod != "born" and bod != "death":
        raise ValueError("bornOrDeath must be 'born' or 'death'")
    c = create_db_connection(dbname)
    if bod == "born":
        q = f"SELECT * FROM artisti WHERE YEAR(data_nascita) = '{d}';"
    else:
        q = f"SELECT * FROM artisti WHERE YEAR(data_morte) = '{d}';"
    res = read_query(c, q)
    c.close()
    return res


# --CRUD--
# datetime formato pe date: 'YYYY-MM-DD HH:MM:SS'

@apiBlueprint.route('/api/addArtista', methods=['POST'])
def addArtista():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"INSERT INTO artisti (nome,movimento,data_nascita,data_morte) VALUES ('{data['autore']}','{data['movimento']}','{data['data_di_nascita']}','{data['data_di_morte']}');"
    r = execute_query(c, q)
    c.close()
    if r:
        return {"res": True}
    else:
        return {"res": False}


@apiBlueprint.route('/api/addOpera', methods=['POST'])
def addOpera():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"INSERT INTO opere (titolo,data_pubblicazione) VALUES ('{data['quadro']}','{data['data_pubblicazione']}');"
    execute_query(c, q)
    q2 = f"SELECT id_artista FROM artisti WHERE nome = '{data['autore']}';"
    id_artista = read_query(c, q2)[0][0]
    q3 = "SELECT id_opera FROM opere ORDER BY id_opera DESC LIMIT 1;"
    id_opera = read_query(c, q3)[0][0]
    q4 = f"INSERT INTO creazione(id_artista, id_opera) VALUES ('{id_artista}', '{id_opera}';"
    r = execute_query(c, q4)
    c.close()
    if r:
        return {"res": True}
    else:
        return {"res": False}


# TODO: add creazione


@apiBlueprint.route('/api/updateArtista', methods=['PUT'])
def updateArtista():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"UPDATE artisti SET nome = '{data['nome']}', data_nascita = '{data['data_nascita']}', data_morte = '{data['data_morte']}' WHERE nome = '{data['nome_orig']}';"
    r = execute_query(c, q)
    c.close()
    if r:
        return {"res": True}
    else:
        return {"res": False}


@apiBlueprint.route('/api/updateOpera', methods=['PUT'])
def updateOpera():
    data = request.get_json()
    c = create_db_connection(dbname)
    print("data?????????", data)
    q = f"UPDATE opere SET titolo='{data['titolo']}', data_pubblicazione = '{data['data_pubblicazione']}', url_immagine = '{data['url_immagine']}' WHERE titolo = '{data['originalName']}';"
    r = execute_query(c, q)
    c.close()
    if r:
        return {"res": True}
    else:
        return {"res": False}


@apiBlueprint.route('/api/deleteArtista', methods=['DELETE'])
def deleteArtista():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"DELETE FROM artisti WHERE nome = '{data['nome']}';"

    r = execute_query(c, q)
    c.close()
    if r:
        return {"res": True}
    else:
        return {"res": False}


@apiBlueprint.route('/api/deleteOpera', methods=['DELETE'])
def deleteOpera():
    data = request.get_json()
    print("in delete", data)
    c = create_db_connection(dbname)
    q = f"DELETE FROM opere WHERE titolo = '{data['titolo']}';"

    r = execute_query(c, q)
    c.close()
    if r:
        return {"res": True}
    else:
        return {"res": False}


# --CREAZIONE DB--
@apiBlueprint.route('/api/createDB', methods=['POST'])
def createDB():
    connection = create_server_connection()
    create_database(connection, "CREATE DATABASE museo")
    connection = create_db_connection("museo")

    artisti = """CREATE TABLE artisti(
                id_artista int PRIMARY KEY AUTO_INCREMENT,
                nome varchar(255) UNIQUE NOT NULL,
                movimento varchar(255),
                data_nascita datetime,
                data_morte datetime);"""
    opere = """CREATE TABLE opere(
                id_opera int PRIMARY KEY AUTO_INCREMENT,
                titolo varchar(255) NOT NULL,
                data_pubblicazione datetime,
                url_immagine varchar(255));"""
    creazione = """CREATE TABLE creazione(
                    id int PRIMARY KEY AUTO_INCREMENT,
                    id_artista int NOT NULL,
                    id_opera int NOT NULL,
                    FOREIGN KEY (id_artista) REFERENCES artisti(id_artista) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (id_opera) REFERENCES opere(id_opera) ON DELETE CASCADE ON UPDATE CASCADE);"""

    execute_query(connection, artisti)
    execute_query(connection, opere)
    execute_query(connection, creazione)

    connection.close()
    return {"todo:": "implementare"}


@apiBlueprint.route('/api/dropDB', methods=['DELETE'])
def dropDB():
    connection = create_server_connection()
    q = "DROP DATABASE museo;"
    execute_query(connection, q)
    connection.close()
    return {"todo:": "implementare"}


@apiBlueprint.route('/api/fillDb', methods=['POST'])
def fillDb():
    mainInsert()
    return {"todo:": "implementare"}


