class Classpet:
    def __init__(self, name, happiness):
        self.name = name
        self.happiness = happiness

 


action = input("what do you want to do: compliment, make a joke, laugh at, attack ")
def happy(self):
    if action == "compliment":
        self.happiness += 50
    elif action == "make a joke":
        self.happiness += 25
    elif action == "attack":
        self.happiness += -100
    elif action == "laugh at":
        self.happiness += -50

    if self.happiness >= 100:
        print(self.name, "is now happy")
    else:
        print(self.name, "is now sad")


def show_balance(self):
    print(f"{self.name} happiness is now ${self.__happiness}")

Boomy = Classpet("Boomy", 100 )
print(Boomy.__dict__)


""" Boomy.buy({"title": "Sword", "atk": 34}) """
""" def buy(self, item):
    self.inventory.append(item)
    print(self.name, self.money, self.inventory) """
