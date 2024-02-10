class Diagnosis:
    def __init__(self, photo = -1, originHosp=""):
        self.photo = photo
        self.originHosp = originHosp
    
    def deletePhoto(self):
        self.photo = -1

# @app.route('/decrement_supply', methods=['POST'])
# def decrement_supply():
#     data = request.form
#     supply_name = data.get('supplyName')
#     count = int(data.get('count'))

#     # Retrieve the supply from MongoDB
#     supply = mongo.db.supplies.find_one({'item': supply_name})

#     if supply:
#         current_quantity = supply.get('quantity', 0)
#         new_quantity = max(current_quantity - count, 0)  # Ensure quantity doesn't go below 0

#         # Update the quantity in MongoDB
#         mongo.db.supplies.update_one({'item': supply_name}, {'$set': {'quantity': new_quantity}})

#         return jsonify({'message': 'Quantity decremented successfully'}), 200
#     else:
#         return jsonify({'error': 'Supply not found'}), 404
