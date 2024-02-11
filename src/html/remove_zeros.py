# Connection URI
uri = "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority"

# Database Name
db_name = "<database>"

# Collection Names
collection_names = ["giving", "profile", "profile2", "supplies"]


@app.route('/remove_zeros', methods=['POST'])
def remove_zeros():
    try:
        # Create a MongoClient
        client = MongoClient(uri)
        db = client[db_name]

        # Loop through collection names
        for collection_name in collection_names:
            collection = db[collection_name]

            # Find documents with quantity equal to 0
            documents_to_remove = collection.find({"quantity": 0})

            # Loop through the documents to remove
            for document in documents_to_remove:
                # Remove the document
                collection.delete_one({"_id": document["_id"]})
                print(f"Document with _id {document['_id']} removed from {collection_name}.")

        return "Zero quantity documents removed successfully."
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        client.close()

    return render_template('settings.html')