# import json
# from pymongo import MongoClient

# def upload_to_mongodb(filename):
#     try:
#         # Connect to MongoDB
#         client = MongoClient("mongodb://localhost:27017/")
#         db = client['test']
#         collection = db['test']

#         # Read data from JSON file
#         with open(filename, 'r') as file:
#             for line in file:
#                 data = json.loads(line)
#                 # Insert each entry into MongoDB collection
#                 collection.insert_one(data)
        
#         print("Data uploaded to MongoDB successfully")
#     except Exception as e:
#         print(f"Error uploading data to MongoDB: {str(e)}")

# if __name__ == '__main__':
#     filename = 'financial_data.json'
#     upload_to_mongodb(filename)

import json
from pymongo import MongoClient 


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["test"]

# Created or Switched to collection 
# names: GeeksForGeeks
Collection = db["test"]

# Loading or Opening the json file
with open('financial_data.json') as file:
	file_data = json.load(file)
	
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
	Collection.insert_many(file_data) 
else:
	Collection.insert_one(file_data)

