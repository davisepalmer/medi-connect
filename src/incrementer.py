from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority')
db = client['<database>']
collection = db['supplies']

# Function to add quantity to each document
def add_quantity_to_documents(quantity):
    documents = collection.find()  # Fetch all documents in the collection
    for document in documents:
        # Update each document with the given quantity
        updated_document = {'$set': {'quantity': quantity}}
        collection.update_one({'_id': document['_id']}, updated_document)

# Call the function with the desired quantity
add_quantity_to_documents(10)  # Change the quantity value as needed

print("Quantity added to documents successfully!")
