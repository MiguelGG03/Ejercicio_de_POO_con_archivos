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

    def lista_con_nna(self):   #Nombres,notas y asistencias
        for i in range(1,17):
            temp=[self.datos[i][0],
                  self.datos[i][2],
                  self.datos[i][3],
                  self.datos[i][4],
                  self.datos[i][5],
                  self.datos[i][6],
                  self.datos[i][7],
                  self.datos[i][8]]
                  
            self.lista_datos.append(temp)
        print(self.lista_datos)

    def 
    