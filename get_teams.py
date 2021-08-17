
def RemoveRepetidosLista(l):
    # cria um dicionario em branco
    dict = {}
    # para cada valor na lista l
    for word in l:
        # adiciona ao dicionario: valor:1
        # note que se for repetido o valor somente sobrescreve ele :)
        dict[word] = 1
    # retorna uma copia das 'keys'
    l[:] = dict.keys()
    return l

def get_teams(team):

    
    from pymongo import MongoClient
    from pprint import pprint
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient("mongodb://rodrigofs08:diguinho@cyberbaska-shard-00-00.8wjee.mongodb.net:27017,cyberbaska-shard-00-01.8wjee.mongodb.net:27017,cyberbaska-shard-00-02.8wjee.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-iriu8k-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client.cyberbaska
    mycol = db["players"]

    myquery = { "team": team }

    mydoc = mycol.find(myquery)

    lista=[]

    for x in mydoc:
        
        lista.append(x)
    print('>>>>>>>>>>> foi')    
    return lista

def get_team_list():
    
    from pymongo import MongoClient
    from pprint import pprint
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient("mongodb://rodrigofs08:diguinho@cyberbaska-shard-00-00.8wjee.mongodb.net:27017,cyberbaska-shard-00-01.8wjee.mongodb.net:27017,cyberbaska-shard-00-02.8wjee.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-iriu8k-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client.cyberbaska
    mycol = db["players"]

    

    mydoc = mycol.find({})

    lista=[]

    for x in mydoc:
        
        lista.append(x['team'])
    print('>>>>>>>>>>> foi',RemoveRepetidosLista(lista))
    return RemoveRepetidosLista(lista)
