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

    def crear_lista(self):
        for i in self.f:
            i=i.rstrip('\n')