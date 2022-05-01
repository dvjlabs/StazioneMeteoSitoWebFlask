import mysql.connector

pydb = mysql.connector.connect(
    host="10.10.1.27",
    user="utente",
    passwd="password",
    database="meteo_station"
)


def stazioni():
    pycur = pydb.cursor()
    sql = "SELECT DISTINCT station FROM DataTable"

    pycur.execute(sql)
    results = pycur.fetchall()

    data1 = []
    for data in results:
        data1.append(data[0])
        
    return data1

# -----------------------------------------------------------

def valoreAlle(stationName, hour, valueType):
    pycur = pydb.cursor()
    
    sql = "SELECT " + valueType + ",dateTime FROM DataTable WHERE HOUR(dateTime) = '" + hour + "' AND station = '" + stationName + "'"
    print(sql)
    pycur.execute(sql)
    results = pycur.fetchall()
    
    data1 = []
    data2 = []
    for data in results:
        data1.append(data[0])
        data2.append(data[1])
        
    return data1,data2

# -----------------------------------------------------------

def coppie(value1,value2,station):
    pycur = pydb.cursor()
    
    sql = "SELECT " + value1 + ", " + value2 + " FROM DataTable WHERE HOUR(dateTime) > 6 AND HOUR(dateTime) < 18 AND station = '" + station + "'"
    # print(sql)
    pycur.execute(sql)
    results = pycur.fetchall()
    
    data1 = []
    data2 = []
    for data in results:
        data1.append(data[0])
        data2.append(data[1])
        
    return data1,data2

# -----------------------------------------------------------

def coppieOra(value1,value2,station,hour):
    pycur = pydb.cursor()
    
    sql = "SELECT " + value1 + ", " + value2 + ",dateTime FROM DataTable WHERE HOUR(dateTime) = " + hour + " AND station = '" + station + "'"
    # print(sql)
    pycur.execute(sql)
    results = pycur.fetchall()
    
    data1 = []
    data2 = []
    data3 = []
    for data in results:
        data1.append(data[0])
        data2.append(data[1])
        data3.append(data[2])
        
    return data1,data2,data3

# -----------------------------------------------------------
if __name__ == "__main__":
    print("ELENCO STAZIONI")
    print( stazioni() )
    print("--------------------")
    print("VALORE temperature DELLA STAZIONE Elisa ALLE ORE 15") 
    print( valoreAlle("Elisa", "15", "temperature") )
    print("VALORE pressure DELLA STAZIONE 'Stazione07' ALLE ORE 16") 
    print( valoreAlle("Stazione07", "16", "pressure") )
    print("--------------------")
    print("COPPIE DI VALORI")
    print( coppie("temperature","pressure","Elisa") )
    print( coppie("humidity","pressure","Elisa") )
    print( coppie("temperature","humidity","Elisa") )
    