import csv

class lectura:
    def __init__(self):
        f = open('calificaciones.csv', 'r',encoding='utf-8')
        datos=[]
        lista_datos=[]
        self.f=f
        self.datos=datos
        self.lista_datos=lista_datos

    def leer_csv(self):
        with open('calificaciones.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])