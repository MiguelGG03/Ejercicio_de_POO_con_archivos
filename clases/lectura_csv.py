import pandas as pd

class lectura:
    def lectura(slef):
        df= pd.read_cvs('calificaciones.csv')
        print(df)