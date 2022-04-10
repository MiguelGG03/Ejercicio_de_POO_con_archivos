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



            temp=[self.datos[i][1],self.datos[i][0],examen_1,examen_2,examen_3,x]
            self.lista_notas.append(temp)
        
        return self.lista_notas

    def aprobados_suspensos(self):
        lista_previa=[]
        lista_aprobados=['Aprobados:']
        lista_suspensos=['Suspensos:']
        for i in range(1,17):
            s2=int(self.datos[i][2].replace('%',''))        #presencialidad
            
            s3=float(self.lista_notas[i-1][2])               #ordinaria 1
            s4=float(self.lista_notas[i-1][3])               #ordinaria 2
            s5=float(self.lista_notas[i-1][4])               #practica
            
            """
            s3=float(self.datos[i][3].replace(',','.'))     #ordinaria 1
            s4=float(self.datos[i][4].replace(',','.'))     #ordinaria 2
            s5=float(self.datos[i][5].replace(',','.'))     #extraordinaria 1
            s6=float(self.datos[i][6].replace(',','.'))     #extraordinaria 2
            s7=float(self.datos[i][7].replace(',','.'))     #practica
            s8=float(self.datos[i][8].replace(',','.'))     #practica extra
            
            """
            
            s6=self.lista_notas[i-1][5]                     #medias
            h=[s2,s3,s4,s5,s6]
            lista_previa.append(h)
        


        """
        for i in range(1,17):
            if(lista_previa[i][0]>=75):

                if(self.datos[i][3].replace(',','.'))>=4 or self.datos[i][5].replace(',','.')>=4):

                    if(self.datos[i][4].replace(',','.')>=4 or self.datos[i][6].replace(',','.')>=4):

                        if(self.datos[i][7].replace(',','.')>=4 or self.datos[i][8].replace(',','.')>=4):

                             if(self.lista_notas[i][2]>=5):

                                 lista_aprobados.append(self.datos[i][1]+' '+self.datos[i][0])
                        else:
                            lista_suspensos.append(self.datos[i][1]+' '+self.datos[i][0])
                    else:
                        lista_suspensos.append(self.datos[i][1]+' '+self.datos[i][0])
                else:
                    lista_suspensos.append(self.datos[i][1]+' '+self.datos[i][0])
            else:
                lista_suspensos.append(self.datos[i][1]+' '+self.datos[i][0])

        """


        for i in range(0,16):
            if(lista_previa[i][0]>=75):

                if(self.datos[i][1]>=4):

                    if(self.datos[i][2].replace(',','.')>=4):

                        if(self.datos[i][3].replace(',','.')>=4):

                             if(self.lista_notas[i][4]>=5):

                                 lista_aprobados.append(self.datos[i+1][1]+' '+self.datos[i+1][0])
                        else:
                            lista_suspensos.append(self.datos[i+1][1]+' '+self.datos[i+1][0])
                    else:
                        lista_suspensos.append(self.datos[i+1][1]+' '+self.datos[i+1][0])
                else:
                    lista_suspensos.append(self.datos[i+1][1]+' '+self.datos[i+1][0])
            else:
                lista_suspensos.append(self.datos[i+1][1]+' '+self.datos[i+1][0])
        
        
        lista_final=[lista_aprobados,' ',lista_suspensos]
        return lista_final
