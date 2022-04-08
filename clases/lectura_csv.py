import csv

class lectura:
    def __init__(self):
        f = open('calificaciones.csv', 'r',encoding='utf-8')
        datos=[]
        lista_datos=[]