from clases.lectura_csv import *

def main():
    l=lectura('calificaciones.csv')
    lista_con_todo=l.crear_lista()
    lista_nna=l.lista_con_nna()
    lista_con_medias=l.medias()
    print(lista_con_medias)

if __name__=='__main__':
    main()