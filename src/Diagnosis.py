class Diagnosis:
    def __init__(self, photo, originHosp=""):
        self.photo = -1
        self.originHosp = originHosp
    
    def deletePhoto(self):
        self.photo = -1
