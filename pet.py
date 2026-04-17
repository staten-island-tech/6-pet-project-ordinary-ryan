class Classpet:
    def __init__(self, name, happiness):
        self.name = name
        self.happiness = happiness

Boomy = Classpet("Boomy", 100 )
print(Boomy.__dict__) 

def show_balance(self):
    print(f"{self.name} happiness is now{self.happiness}")

def happy(self):
    action = input("what do you want to do: compliment, make a joke, laugh at, attack ")
    cont = True
    joy = 0
    while cont == True:
        if action == "compliment":
            joy = 50
        elif action == "make a joke":
            joy = 25
        elif action == "attack":
            joy = -100
        elif action == "laugh at":
            joy= -50
    
        self.happiness += joy

        if self.happiness >= 100:
            print(self.name, "is happy")
        else:
            print(self.name, "is sad")

        cont_ = input("do you want to continue: yes or no")
        if cont_ == "yes":
            cont = True
        elif cont_ == "no":
            cont = False
            break
    print("Thank you for playing")
happy(Boomy)


    
""" Boomy.buy({"title": "Sword", "atk": 34}) """
""" def buy(self, item):
    self.inventory.append(item)
    print(self.name, self.money, self.inventory) """
