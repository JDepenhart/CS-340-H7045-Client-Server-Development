#Jeremy Depenhart
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        # initializes the MongoClient. This helps
        # access the databases and collections.
        # This is hard-wired to use the aac database and
        # the animal collection (user and pass are input)
        #
        # Conecction Variables
        #
        #USER = 'aacuser'
        #PASS = 'AACPass'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32268
        DB = 'AAC'
        COL = 'animals'
        #
        # Init Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    # Create operation
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary  
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
    # Read operation
    def read(self, query):
        result = self.database.animals.find(query)
        if result is None:    
            raise Exception("Nothing was found in query") # query comes back empty
        return list(result)
    
    # Update operation
    def update(self, original, updated):
        if original is not None:
            result = self.database.animals.find(original)
            if result.count() > 1:
                updatedResult = self.database.animals.update_many(original, updated) # updates multiple if result come back as multiple
            else:
                updatedResult = self.database.animals.update_one(original, updated) # updates one if result come back as one
            return  updatedResult.modified_count
        else:
            raise Exception("Parameter empty, nothing was updated") # original comes back empty
    
    # Delete operation
    def delete(self, query):
        if query is not None:
            result = self.database.animals.find(query)
            if result.count() > 1:
                deleteResult = self.database.animals.delete_many(query) # deletes multiple if result come back as multiple
            else:
                deleteResult = self.database.animals.delete_one(query) # deletes one if result come back as one
            return deleteResult.deleted_count
        else:
            raise Exception("Parameter empty, nothing was deleted") # query comes back empty
            
            
        

