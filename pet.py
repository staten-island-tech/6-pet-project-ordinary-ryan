


class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    
Ixia = Hero("Ixia", 500, ["Boots"])
Ixia.buy({"title": "Sword", "atk": 34})
print(Ixia.__dict__)