class Classpet:
    def __init__(self, name, money, inventory, happiness):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happiness
Boomy = Classpet("Boomy", 500, ["Boots"], 100)
print(Boomy.__dict__) 
"""     def buy(self, item):
        self.inventory.append(item)
        print(self.name, self.money, self.inventory) """
action = input("what do you want to do: compliment, make a joke, laugh at, attack ")
def happy(self, joy):
    if action == "compliment":
        joy = 50
    elif action == "make a joke":
        joy = 25
    elif action == "attack":
        joy = -100
    elif happiness == "laugh at":
        joy = -50

    happiness += joy
    if happiness >= 100:
        self.happiness = 'happy'
    else:
        self.happiness = 'sad'
    print("Boomy's is now", self.happiness,)

""" Boomy.buy({"title": "Sword", "atk": 34}) """
