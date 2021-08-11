def insert_stats():


    from pymongo import MongoClient
    from pprint import pprint
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient("mongodb://rodrigofs08:diguinho@cyberbaska-shard-00-00.8wjee.mongodb.net:27017,cyberbaska-shard-00-01.8wjee.mongodb.net:27017,cyberbaska-shard-00-02.8wjee.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-iriu8k-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client.cyberbaska

    Consulta =db.players.find_one({})

    result = db.players.update({'_id' : Consulta.get('_id') }
                            
                            , {'$push': {'games': [{'STATS': {'assists': 19, 'points': 2},
                'camp': 'Teste',
                'game_id': 'JV3ANO#GRUPOA1'}]}})



    UpdatedDocument = db.players.find_one({'_id':Consulta.get('_id')})
    print('The updated document:')
    pprint(UpdatedDocument)

    return ('Stats adicionado com sucesso!')
