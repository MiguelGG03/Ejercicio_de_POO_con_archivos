import csv

class lectura:
    def lectura_2pac(self):    
        with open('calificaciones.csv', newline='') as csvfile:
            lector = csv.reader(csvfile, delimiter=',')
            for row in lector:
                print(row)