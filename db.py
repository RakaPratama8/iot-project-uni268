def connect_mongo(uri, db, collection):
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import certifi

    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
        
    db_mongo = client[db]
    collection_mongo = db_mongo[collection]
    print(f"Successfully accessed the collection : {collection_mongo} from database: {db_mongo}")
        
    return client