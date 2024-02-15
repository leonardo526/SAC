from flask import Flask, render_template, request
from api import *
from SAC2.dbUtils import create_db_connection, read_query

app = Flask(__name__)
app.register_blueprint(apiBlueprint)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/data/film', methods=['GET'])
def get_data_film():
    query = "SELECT title,Avg_rating FROM film"
    items = execute_query(query)
    return items
@app.route('/film')
def show_film():
    books = get_data_film()
    return render_template('film.html', books=books)


@app.route('/data/film', methods=['GET'])
def get_data_film():
    query = "SELECT title,Avg_rating FROM film"
    items = execute_query(query)
    return items
@app.route('/film')
def show_film():
    books = get_data_film()
    return render_template('film.html', books=books)









@app.route('/movie')
def artisti():
   page = int(request.args.get('page', default=1))
   items_per_page = 20
   print(dbname, "dbname in api???")
   c = create_db_connection(dbname)
   query = "SELECT title FROM film"
   conteggio = read_query(c, query)[0]['num_artisti']
   totale = (conteggio // items_per_page) + 1
   artisti = getArtisti()
   return render_template('pittori.html', artisti=artisti, page=page, total_pages=totale)

@app.route('/aggiungi_pittore_opera')
def aggiungiArtista():
   return render_template('aggiungi_pittore_opera.html')

@app.route('/quadri')
def opere():
   page = int(request.args.get('page', default=1))
   items_per_page = 20
   c = create_db_connection(dbname)
   query = "SELECT COUNT(*) AS num_opere FROM opere"
   conteggio = read_query(c,query)[0]['num_opere']
   totale = (conteggio // items_per_page) + 1
   n = request.args.get("nome", default=None)
   print(n, type(n))
   print("vivo ")
   if n:
      if isinstance(n, str):
         opere = getOpereByArtist(n)
         #print(opere)
      else:
         raise TypeError("Il nome deve essere una stringa")
   else:
      opere = getWorks()
   return render_template('quadri.html', opere=opere, page=page, total_pages=totale)

@app.route('/update&delete_artistaLeo')
def update_delete_artista():
   return render_template('update&delete_artistaLeo.html')

@app.route('/update&delete_opereLeo')
def update_delete_opere():
   return render_template('update&delete_opereLeo.html')

if __name__ == '__main__':
   app.run(debug=True)
