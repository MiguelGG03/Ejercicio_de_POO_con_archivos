import pandas as pd

class lectura:
    def __init__(self,ubi):
        lector=open(ubi,'r',encoding='utf-8')
        datos=[]
        lista_datos=[]
        self.lector=lector
        self.datos=datos
        self.lista_datos=lista_datos
        self.diccionario=datos

    def crear_lista(self):
        for i in self.lector:
            i=i.rstrip('\n')
            colm= i.split(';')
            self.datos.append(colm)
        print(self.datos)
        return self.datos

    