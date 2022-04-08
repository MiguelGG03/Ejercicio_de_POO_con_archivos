from clases.lectura_csv import *

def main():
    l=lectura('calificaciones.csv')
    notas=l.crear_lista()
    print(notas[0][1])

if __name__=='__main__':
    main()