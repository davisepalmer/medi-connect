
class Supply:
    def __init__(self, isNeeded, item = "", quantity=0, originHosp=""):
        self.isNeeded = isNeeded 
        self.item = item
        self.quantity = quantity
        self.originHosp = originHosp

    ### DATA MEMBER EDITORS ###
    def decQuantity(self, quantity, count=1):
        self.quantity -= count
    
    def changeOriginHosp(self, originHosp):
        self.originHosp = originHosp
    
    def changeIsNeeded(self, isNeeded):
        self.isNeeded = isNeeded
    
    def deleteSupple(self):
        self.isNeeded = False
        self.quantity = -1
        self.originHosp = ""
    
    

    

