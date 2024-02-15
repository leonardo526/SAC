from flask import Flask, render_template, request
from api import *


app = Flask(__name__)
app.register_blueprint(apiBlueprint)


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/film')
def show_film():
    page = int(request.args.get('page', default=1))
    items_per_page = 20
    c = create_db_connection("daitv12")
    query = "SELECT COUNT(*) AS num_film FROM film"
    conteggio = read_query(c, query)[0]['num_film']
    totale = (conteggio // items_per_page) + 1
    data = getMovies()
    top_diesci = Top10Film()
    return render_template('Film.html', films=data, topdieci=top_diesci, page=page, total_pages=totale)


@app.route('/generi')
def show_generi():
    page = int(request.args.get('page', default=1))
    items_per_page = 10
    c = create_db_connection("daitv12")
    query = "SELECT COUNT(*) AS num_generi FROM generi"
    conteggio = read_query(c, query)[0]['num_generi']
    totale = (conteggio // items_per_page) + 1
    data = getGeneri()
    return render_template('Generi.html', generi=data, page=page, total_pages=totale)

@app.route('/grafici')
def showGrafici():
    return render_template('Grafici.html')








if __name__ == '__main__':
   app.run(debug=True)
