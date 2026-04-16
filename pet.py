class Classpet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness

Boomy = Classpet("Boomy", 100 )
print(Boomy.__dict__) 


action = input("what do you want to do: compliment, make a joke, laugh at, attack ")
def happy(self, joy):
    joy = 0
    if action == "compliment":
        joy = 50
    elif action == "make a joke":
        joy = 25
    elif action == "attack":
        joy = -100
    elif action == "laugh at":
        joy= -50
    
    self.__happiness += joy

    if self.__happiness >= 100:
        print(self.name, "is happy")
    else:
        print(self.name, "is sad")

def show_balance(self):
    print(f"{self.name} happiness is now{self.__happiness}")


    
""" Boomy.buy({"title": "Sword", "atk": 34}) """
""" def buy(self, item):
    self.inventory.append(item)
    print(self.name, self.money, self.inventory) """
