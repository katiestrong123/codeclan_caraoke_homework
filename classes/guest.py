
class Guest:
    def __init__(self, name, age, favourite_song, cash):
        self.name = name 
        self.age = age
        self.favourite_song = favourite_song
        self.cash = cash 

    def guest_can_afford(self, amount):
        return self.cash >= amount

    def can_buy_drink(self, guest_to_check):
        if guest_to_check.age >= 18:
            return "Yas Kween, get krunk"

    def reduce_wallet(self, amount):
        self.cash -= amount
        return self.cash



    
        