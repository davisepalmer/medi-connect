from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo


@app.route('/create_supply', methods=['POST'])
def create_supply():
    data = request.get_json()
    supply_name = data.get('supplyName')
    quantity = data.get('quantity')
    requested_by = data.get('requestedBy')
    giving_name = data.get('givingName') #added
    quantityb = data.get('quantityb') #added
    given_by = data.get('givenBy') #added

    if supply_name and quantity and requested_by:
        mongo.db.supplies.insert_one({
            "isNeeded": True,
            "item": supply_name,
            "quantity": quantity,
            "originHosp": requested_by
        })
        return jsonify({'message': 'Request created successfully'}), 200
    if giving_name and quantityb and given_by: #changed
        mongo.db.giving.insert_one({
            "isNeeded": False,
            "item": giving_name, #changed
            "quantity": quantityb, #changed
            "originHosp": given_by
        })
        return jsonify({'message':'Supply created successfully'}), 200
    else:
        return jsonify({'error': 'Invalid supply data provided'}), 400