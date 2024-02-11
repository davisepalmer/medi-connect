from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo
from pymongo import MongoClient



app.config["MONGO_URI"] = "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/decrement', methods=['POST'])
def decrement():
    data = request.json
    supply_name = data.get('supplyName')
    count = int(data.get('decrementCount'))

    if supply_name and count > 0:
        # Find the document with the specified supply name
        supply = mongo.db.giving.find_one({'item': supply_name})
        if supply:
            current_quantity = supply.get('quantity')
            new_quantity = current_quantity - count
            if new_quantity >= 0:
                # Update the quantity in the document
                mongo.db.giving.update_one({'item': supply_name}, {'$set': {'quantity': new_quantity}})
                return jsonify({'message': 'Claimed successfully'}), 200
            else:
                return jsonify({'error': 'Error: Not enough supply available'}), 400
        else:
            return jsonify({'error': 'Supply not found'}), 404
    else:
        return jsonify({'error': 'Invalid data provided'}), 400
    
    # if supply_name and count > 0:
    #     supply = mongo.db.giving.find_one
    #     for i in mongo.db.giving:
    #         if i["name"] == supply_name:
    #             current_quantity = i["quantity"]
    #         else:
    #             return jsonify({'error': 'Supply not found'}), 404
    #     new_quantity = current_quantity - count
    #     if new_quantity < 0:
    #         return jsonify({'message': 'Error: Not enough supply available'}), 400
    #     else:
    #         for i in mongo.db.giving:
    #             if i["name"] == supply_name:
    #                 i["quantity"] = new_quantity
    #                 return jsonify({'message': 'Claimed successfully'}), 200
    # else: 
    #     return jsonify({'error': 'Invalid data provided'}), 400




    #     supply = mongo.db.supplies.find({"item": supply_name})
    #     if supply:
    #         current_quantity = supply.get('quantity')
    # return jsonify({'message': 'Request created successfully'}), 200

    # if supply_name and count > 0:
    #     # Find the supply in the database
    #     supply = giving.find_one({'item': supply_name})
    #     if supply:
    #         current_quantity = supply.get('quantity', 0)
    #         new_quantity = current_quantity - count
    #         if new_quantity < 0:
    #             return jsonify({'message': 'Error: Not enough supply available'}), 400
            
    #         # Update the supply quantity in the database
    #         giving.update_one({'item': supply_name}, {'$set': {'quantity': new_quantity}})
    #         return jsonify({'message': 'Claimed successfully'}), 200
    #     else:
    #         return jsonify({'error': 'Supply not found'}), 404
    # else:
    #     return jsonify({'error': 'Invalid data provided'}), 400