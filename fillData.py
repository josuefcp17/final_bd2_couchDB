import couchdb
import csv

print('Conectando a la bd')
couch = couchdb.Server('http://admin:password@127.0.0.1:5984')

print('Conectado')

#Solo al inicio
db = couch.create('movie')
#print('BD crerada')

import csv
with open('moviesDB.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        doc = {
            "name": row[1],
            "genres": row[2],
            'year': row[3]
        }
        db.save(doc)
        print("Agregando pelicula")

print("terminado")        

