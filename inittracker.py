import random
class Character:
    def __init__(self,name,reaction,intuition,initiative):
        self.name = name
        self.reaction = reaction
        self.intuition = intuition
        self.initiative = initiative
    def set_reaction(self):
        print("What is your reaction?")
        self.reaction = int(input())
    def set_intuition(self):
        print("What is your intuition?")
        self.intuition = int(input())
    def set_initiative(self):
        print("What is your initiaive?")
        self.initiative = int(input())
    def roll_initiative(self):
        self.initiative = self.reaction + self.intuition
        dice = 0
        while True:
            print('Number of dice used? 1-5')
            dice = input()
            if (int(dice) > 0) and (int(dice) < 6):
                break
            else:
                print('Incorrect Number of dice inputted, number input is ', dice)
        for i in range(int(dice)):
            roll = random.randint(1,6)
            self.initiative = self.initiative + roll
            print(roll)
        print(self.initiative)

Donny = Character('Donny',3,2,12)

Donny.roll_initiative()
