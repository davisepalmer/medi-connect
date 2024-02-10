class Diagnosis:
    def __init__(self, photo = -1, originHosp=""):
        self.photo = photo
        self.originHosp = originHosp
    
    def deletePhoto(self):
        self.photo = -1
