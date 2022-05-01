from flask import Flask,render_template, request

import funzioni_matplotlib as mpl
import funzioni_sql as fsql


app = Flask(__name__)

# ---------------------------------------------------------------------------------

def creaTabella(dizionario):
    table = ""
    table += "<table class='w3-table w3-striped w3-bordered w3-hoverable'>"
    
    lista = []
    table += "<tr>"
    for key in dizionario:
        table += "<th>"
        table += key
        table += "</th>"
        lista.append( dizionario[key] )
    table += "</tr>"
    
    listaPiuLunga = max(lista,key=len)
    for n in range( len(listaPiuLunga) ):
        table += "<tr>"
        for value in lista:
            v = "NULL"
            if n < len(value) and value[n]:
                v = str(value[n])
            table += "<td>"
            table += v
            table += "</td>"
        table += "</tr>"

    table += "</table>"
    return table

# ---------------------------------------------------------------------------------

@app.route("/")
def index():
    dati = fsql.valoreAlle("Elisa", "15", "temperature")
    mpl.creaGraficoTemperaturaAlle12(dati[1],dati[0])
    dati = fsql.coppie("temperature","pressure","Elisa")
    mpl.creaGraficoTemperaturaPressione(dati[0],dati[1])
    dati = fsql.coppie("temperature","humidity","Elisa")
    mpl.creaGraficoTemperaturaUmidita(dati[0],dati[1])
    return render_template("index.html")


@app.route("/tabelle", methods=["GET"])
def tabella():
    args = request.args
    diz = args.to_dict()
    
    value1 = diz.get("value1", None)
    value2 = diz.get("value2", None)
    station = diz.get("station", None)
    hour = diz.get("hour", None)
    
    print("value1:", value1)
    print("value2:", value2)
    print("station:", station)
    print("hour:", hour)
    
    table = ""
    title = ""
    if value1:
        dizionario = {}
        if value2:
            title += value1 + " e " + value2 + " da " + station + ", ore " + hour
            dati = fsql.coppieOra(value1, value2, station, hour)
            dizionario[value1] = dati[0]
            dizionario[value2] = dati[1]
            dizionario["dateTime"] = dati[2]
        else:
            title += value1 + " da " + station + ", ore " + hour
            dati = fsql.valoreAlle(station, hour, value1)
            dizionario[value1] = dati[0]
            dizionario["dateTime"] = dati[1]
            
        table = creaTabella(dizionario)

    return render_template("tabella.html", TITOLO=title, TABELLA=table)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = False)
