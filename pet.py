class Classpet:
    def __init__(self, name, happiness, hunger):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger

Boomy = Classpet("Boomy", 100, 100)
print(Boomy.__dict__) 

def happy(self):
    action = input("what do you want to do: compliment, feed, attack, pet")
    cont = True
    joy = 0
    hungry = 0
    while cont == True:
        if action == "compliment":
            joy = 50
            hungry = -10
        elif action == "feed":
            joy = 20
            hungry = 35
        elif action == "attack":
            joy = -100
            hungry = -50
        elif action == "pet":
            joy= 30
            hungry =-10
    
        self.happiness += joy
        self.hunger += hungry

        cont_ = input("do you want to continue: yes or no")
        if cont_ == "yes":
            cont = True
            action = input("what do you want to do: compliment, feed, attack, pet")
        elif cont_ == "no":
            cont = False
            break 
        
        

    if self.happiness <= 0 or self.hunger <= 0:
        print(self.name, "is dead")
    elif self.happiness >= 0 and self.happiness <= 50: 
        print(self.name, "is sad")
    else:
        print(self.name, "is happy")
    
    if self.hunger >= 0 and self.hunger <= 50: 
        print(self.name, "is hungry")
    else:
        print(self.name, "is full")


    print("Thank you for playing")
happy(Boomy)


    
""" Boomy.buy({"title": "Sword", "atk": 34}) """
""" def buy(self, item):
    self.inventory.append(item)
    print(self.name, self.money, self.inventory) """
