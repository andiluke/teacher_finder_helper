from pymongo import MongoClient

def get_database():
     
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
   CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['teachers']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   print(dbname)
   collection_name = dbname["teachers"]
   print(f"collection name: {collection_name}")

   item_1 = {
    "name": "test item 1",
    "description": "this is the first test item",
    "list": [
        {
            "list_item_name": "list item 1",
            "list_item_desc": "first list item"
        },
        {
            "list_item_name": "list item 2",
            "list_item_desc": "second list item"
        }
    ]
   }

   item_2 = {
    "name": "test item 2",
    "description": "this is the second test item"
   }

   #collection_name.insert_many([item_1,item_2])

   item_details = collection_name.find({"name" : "test item 1"})
   for item in item_details:
       # This does not give a very readable output
       print(item)