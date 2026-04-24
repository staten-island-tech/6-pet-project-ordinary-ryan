class Classpet:
    def __init__(self, name, happiness, hunger, energy):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy

Boomy = Classpet("Boomy", 100, 100, 100)
print(Boomy.__dict__) 

def happy(self):
    action = input("what do you want to do: compliment, feed, attack, pet, sleep")
    cont = True
    joy = 0
    hungry = 0
    energize = 0
    while cont == True:
        if action == "compliment":
            joy += 50
            hungry += -20
            energize -= 20
            print('Boomy is delighted by your compliment: happiness + 50, hunger -20, energy -20')
        elif action == "feed":
            joy += 20
            hungry += 35
            energize += 20
            print('Boomy is stuffed: happiness +20, hunger +35, energy +20')
        elif action == "attack":
            joy += -100
            hungry += -50
            energize -= 50
            print('Boomy is mad: happiness -100, hunger -50, energy -50')
        elif action == "pet":
            joy += 30
            hungry += -20
            energize -= 20
            print("Boomy is happier: happiness +10, hunger -20, energy -20")
        elif action == "sleep":
            joy += 0
            hungry -= 20
            energize += 50
            print("Boomy feels energetic: happiness +0, hunger -20, energy +50")
        self.happiness += joy
        self.hunger += hungry
        self.energy += energize

        cont_ = input("do you want to continue: yes or no")
        if cont_ == "yes":
            cont = True
            action = input("what do you want to do: compliment, feed, attack, pet, sleep")
        elif cont_ == "no":
            cont = False
            break 
        
        
    print(f"Boomy's happiness is now", {self.happiness})
    print(f"Boomy's hunger is now", {self.hunger})
    if self.happiness <= 0 or self.hunger <= 0 or self.energy <= 0:
        print(self.name, "is dead")
    elif self.happiness >= 0 and self.happiness <= 50: 
        print(self.name, "is sad")
    else:
        print(self.name, "is happy")
    
    if self.hunger >= 0 and self.hunger <= 50: 
        print(self.name, "is hungry")
    else:
        print(self.name, "is full")
    
    if self.energy >= 0 and self.energy <= 50:
        print(self.name, "is tired")
    else:
        print(self.name, " is refreshed")


    print("Thank you for playing")
happy(Boomy)


    
""" Boomy.buy({"title": "Sword", "atk": 34}) """
""" def buy(self, item):
    self.inventory.append(item)
    print(self.name, self.money, self.inventory) """
