import couchdb

print('Conectando a la bd')
couch = couchdb.Server('http://admin:password@127.0.0.1:5984')

print('Conectado')

#Solo al inicio
#db = couch.create('company')
#print('BD crerada')

db = couch['movie']

def createView( dbConn, designDoc, viewName, mapFunction ):
    data = {
            "_id": f"_design/{designDoc}",
            "views": {
                viewName: {
                    "map": mapFunction
                    }
            },
            "language": "javascript",
            "options": {"partitioned": False }
            }
    dbConn.save( data )

mapFunction = '''function (doc) {
                      if( doc.type == 'word')
                      emit(doc.word, doc);
                    }'''

createView( db, "name", "search_view", mapFunction )