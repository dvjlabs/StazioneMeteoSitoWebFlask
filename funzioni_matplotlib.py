import matplotlib.pyplot as plt

def creaGraficoTemperaturaAlle12(dati1, dati2):
    #dati = prendiDatiTemperatura()
    #ascisse = asse temporale
    x = dati1
    temperature = dati2
    plt.plot(x, temperature)
    plt.title("Temperatura Alle 12:00")
    #plt.xlabel("Asse X")
    #plt.ylabel("Asse Y")
    plt.grid(axis = "y")
    plt.savefig("static/grafico1.jpg")
    return

def creaGraficoTemperaturaPressione(dati1, dati2):
    #dati = prendiDatiTemperatura()
    temperatura = dati1
    pressione = dati2
    plt.bar(temperatura,pressione)
    plt.title("Temperatura-Pressione")
    plt.xlabel("Temperatura °C")
    plt.ylabel("Pressione (atm)")
    #plt.grid(axis = "y")
    plt.savefig("static/grafico2.jpg")
    #plt.show()
    return

def creaGraficoTemperaturaUmidita(dati1, dati2):
    #dati = prendiDatiTemperatura()
    temperatura = dati1
    umidita = dati2
    plt.plot(temperatura,umidita)
    plt.title("Temperatura-Umidita")
    plt.xlabel("Temperatura °C")
    plt.ylabel("Umidità g/m³")
    #plt.grid(axis = "y")
    plt.savefig("static/grafico3.jpg")
    #plt.show()
    return

def creaGraficoPressioneUmidita(dati1, dati2):
    #dati = prendiDatiTemperatura()
    temperatura = dati1
    umidita = dati2
    plt.plot(temperatura,umidita)
    plt.title("Pressione-Umidita")
    plt.xlabel("Pressione atm")
    plt.ylabel("Umidità g/m³")
    #plt.grid(axis = "y")
    plt.savefig("static/grafico4.jpg")
    #plt.show()
    return

#pressione istogramma verticale
#umidita pallini? stem?
#temperatura linea

if __name__ == "__main__":
    lista = [45,67]
    creaGraficoTemperaturaAlle12(lista,lista)
    creaGraficoTemperaturaPressione(lista,lista)
    creaGraficoTemperaturaUmidita(lista,lista)
    creaGraficoPressioneUmidita(lista,lista)
    