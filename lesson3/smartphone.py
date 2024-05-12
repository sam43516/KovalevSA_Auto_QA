class Smartphone:
    brand: str = "iPhone"
    model: str = "13 Pro"
    numder: str = "+79999999999"

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number
        
    def infoDevice(self):
        print(f"{self.brand} - {self.model}. {self.number}")    
       
        
        
        
        
        
        