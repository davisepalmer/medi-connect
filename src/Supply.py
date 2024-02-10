class Supply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_needed = db.Column(db.Boolean, nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    origin_hosp = db.Column(db.String(100), nullable=False)

    def __init__(self, is_needed, item, quantity, origin_hosp):
        self.is_needed = is_needed
        self.item = item
        self.quantity = quantity
        self.origin_hosp = origin_hosp

