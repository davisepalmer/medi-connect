from src.Supply import Supply
from src.Diagnosis import Diagnosis

class Hospital:
    def __init__(self, hospName, beds = 0, supplies=[]):
        self.hospName = hospName
        self.beds = beds
        self.supplies = supplies
    
    ### DATA MEMBER EDITORS ###
    def addSupply(self, supply):
        self.supplies.append(supply)
    
    def changeBeds(self, count):
        ```Change the number of beds in the hospital: should be negative to decrement```
        self.beds += count

    def makeSupply(self, isNeeded, item = "", quantity=0, originHosp="")
        supply = Supply(isNeeded, item, quantity, originHosp)
        self.addSupply(supply)
    
    def giveSupply(self, supply, destinationHosp): #i dont know if we need this functionality
        supply.changeOriginHosp(destinationHosp)
        destinationHosp.addSupply(supply)
        self.supplies.remove(supply)
    
    def deleteSupply(self, supply):
        supply.deleteSupple()
        self.supplies.remove(supply)
    
    # SEND DIAGNOSIS
    # etc etc

    
    
    
    
     