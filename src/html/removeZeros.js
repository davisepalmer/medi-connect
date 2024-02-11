// import the required modules
const { MongoClient } = require("mongodb");

// Connection URI
const uri =
  "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority";

// Database Name
const dbName = "<database>";

// Collection Names
const collectionNames = ["giving", "profile", "profile2", "supplies"];

// Define the function to remove zero quantity documents
async function removeZeros() {
  // Create a new MongoClient
  const client = new MongoClient(uri, { useUnifiedTopology: true });
  console.log("Removing zero quantity documents...");
  try {
    // Connect to the MongoDB server
    await client.connect();

    const db = client.db(dbName);

    // Loop through collection names
    for (const collectionName of collectionNames) {
      const collection = db.collection(collectionName);

      // Find documents with quantity equal to 0
      const documentsToRemove = await collection
        .find({ quantity: 0 })
        .toArray();

      // Loop through the documents to remove
      for (const document of documentsToRemove) {
        // Remove the document
        await collection.deleteOne({ _id: document._id });
        console.log(
          `Document with _id ${document._id} removed from ${collectionName}.`
        );
      }
    }
  } catch (error) {
    console.error(`An error occurred: ${error}`);
  } finally {
    // Close the MongoClient
    await client.close();
  }
}
