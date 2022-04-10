from clases.lectura_csv import *

def main():
    l=lectura('calificaciones.csv')
    lista_con_todo=l.crear_lista()
    lista_nna=l.lista_con_nna()
    lista_con_medias=l.medias()
    print(lista_con_medias)
    for i in  range(0,16):
        print('Nombre:{}\nApellidos:{}\nMedia:{}\n\n'.format(lista_con_medias[i][0],
                                                        lista_con_medias[i][1],
                                                        lista_con_medias[i][2]))
    imprimir_resultados=l.aprobados_suspensos()
    for i in imprimir_resultados:
        print(i)
if __name__=='__main__':
    main()