def connect_mongo(uri, db, collection):
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import certifi
    import pymongo.errors
    import ssl
    
    try:
        client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
            
        db_mongo = client[db]
        collection_mongo = db_mongo[collection]
        print(f"Successfully accessed the collection : {collection_mongo} from database: {db_mongo}")
        
        return client
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(f"Server selection timeout error: {err}")
    except pymongo.errors.ConnectionFailure as err:
        print(f"Connection failure: {err}")
    except ssl.SSLError as err:
            print(f"SSL error: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")