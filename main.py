from clases.lectura_csv import *

def main():
    l=lectura('calificaciones.csv')
    lista_con_todo=l.crear_lista()
    lista_nna=l.lista_con_nna()

if __name__=='__main__':
    main()