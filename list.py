import couchdb

print('Conectando a la bd')
couch = couchdb.Server('http://admin:password@127.0.0.1:5984')

print('Conectado')

#Solo al inicio
#db = couch.create('company')
#print('BD crerada')

db = couch['movie']
print('Elegido')

#doc = {'name': 'Apple Inc', 'country': 'US'}
#print('Guardado')

#doc = db.save(doc)
#print('Impreso')


#print('Guardado')

for id in db:
    print(db[id])


