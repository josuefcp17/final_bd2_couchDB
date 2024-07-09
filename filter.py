import couchdb

print('Conectando a la bd')
couch = couchdb.Server('http://admin:password@127.0.0.1:5984')

print('Conectado')

#Solo al inicio
#db = couch.create('company')
#print('BD crerada')

db = couch['movie']

db['dogs'] = dict(type='name', name='Lawn Dogs')

for row in db.view('_all_docs'):
    print(row.id)