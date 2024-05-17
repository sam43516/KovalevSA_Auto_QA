from address import Address

class Mailing:
    
    def __init__(
            self, 
            to_address: Address,
            from_address: Address,
            cost: int,
            track: str
            ):
        
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def dispatch(self):
        print(f"Отправление {self.track} из {self.to_address.index}, {self.to_address.city}, {self.to_address.street}, {self.to_address.building} - {self.to_address.flat} "  
              f"в {self.from_address.index}, {self.from_address.city}, {self.from_address.street}, {self.from_address.building} - {self.from_address.flat}. Стоимость {self.cost} рублей.")     
       