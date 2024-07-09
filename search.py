import couchdb

print('Conectando a la bd')
couch = couchdb.Server('http://admin:password@127.0.0.1:5984')

print('Conectado')

#Solo al inicio
#db = couch.create('company')
#print('BD crerada')

db = couch['movie']

results = db.query()

list(results[['Lawn Dogs']])