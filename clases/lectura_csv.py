import csv

class lectura:
    def __init__(self):
        f=open('calificaciones.csv','r',encoding='utf-8')
        datos=[]
        lista_datos=[]
        diccionario=[]
        self.f=f
        self.datos=datos
        self.lista_datos=lista_datos
        self.diccionario=diccionario

    def leer_csv(self):
        with open(self.ubi, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)

    def crear_lista(self):
        for i in self.f