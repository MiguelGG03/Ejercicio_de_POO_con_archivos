class lectura:
    def __init__(self,ubi):
        lector=open(ubi,'r',encoding='utf-8')
        datos=[]
        lista_datos=[]
        lista_notas=[]
        self.lista_notas=lista_notas
        self.lector=lector
        self.datos=datos
        self.lista_datos=lista_datos
        self.diccionario=datos

    def crear_lista(self):
        for i in self.lector:
            i=i.rstrip('\n')
            colm= i.split(';')
            self.datos.append(colm)
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

    def medias(self):
        for i in range(1,17):
            x=0
            if(self.datos[i][3]==''):
                if(self.datos[i][5]==''):
                    examen_1=0
                else:
                    examen_1=float(self.datos[i][5].replace(',','.'))
            else:
                    if(float(self.datos[i][3].replace(',','.'))>4):
                        examen_1=float(self.datos[i][3].replace(',','.'))
                    else:
                        if(self.datos[i][5]==''):
                            examen_1=0
                        else:
                            examen_1=float(self.datos[i][5].replace(',','.'))


            if(self.datos[i][4]==''):
                if(self.datos[i][6]==''):
                    examen_2=0
                else:
                    examen_2=float(self.datos[i][6].replace(',','.'))
            else:
                    if(float(self.datos[i][4].replace(',','.'))>4):
                        examen_2=float(self.datos[i][4].replace(',','.'))
                    else:
                        if(self.datos[i][6]==''):
                            examen_2=0
                        else:
                            examen_2=float(self.datos[i][6].replace(',','.'))


            if(self.datos[i][7]==''):
                if(self.datos[i][8]==''):
                    examen_3=0
                else:
                    examen_3=float(self.datos[i][8].replace(',','.'))
            else:
                    if(float(self.datos[i][7].replace(',','.'))>4):
                        examen_3=float(self.datos[i][7].replace(',','.'))
                    else:
                        if(self.datos[i][8]==''):
                            examen_3=0
                        else:
                            examen_3=float(self.datos[i][8].replace(',','.'))

            x=((examen_1 + examen_2)*0.3)+(examen_3*0.4)                



            temp=[self.datos[i][1],self.datos[i][0],x]
            self.lista_notas.append(temp)
        
        return self.lista_notas