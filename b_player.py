
from a_die import Die

class Player():
    def __init__(self):
        self.DICE = [Die(), Die(), Die(), Die(), Die()]
        self.HELD = []
        self.ROLLED = []
        self.SHIP = False
        self.CAPTAIN = False
        self.CREW = False
        self.ROLL = 0
        self.POINTS = 0
        self.TURNS = 3
        self.DOUBLES = False


    # ---METHODS--- #
    def rollDice(self):
        """Roll all dice in DICE"""

        for die in self.DICE:
            die.rollDie()
            DIE_NUM = die.DIE_NUM
            self.ROLLED.append(DIE_NUM)
    
    def setDice(self, NUM):
        self.DICE = []
        for i in range (NUM):
            self.DICE.append(Die())

    def resetDice(self):
        """reset dice in held
        """
        self.DICE += self.HELD
        self.HELD = []

    def reRoll(self):
        """clear rolled dice 
        """
        self.ROLLED = []

    def findDoubles(self):
        self.ROLLED.sort()

        for i in range (len(self.ROLLED) -1, -1, -1):
            if i != len(self.ROLLED) - 1:
                if self.ROLLED[i] == self.ROLLED[i+1]:
                    self.DOUBLES = True

    def turn(self):
        """players turn finding ship, captain, crew, then loot
        """
        # --- INPUT -- #
        
        if self.SHIP == True and self.CREW == True and self.CAPTAIN == True:
            REROLL = input("Would you like to reroll to try and get a higher loot? (Y/n)")
            #----_#
            if REROLL.upper() == "Y" or REROLL == "":
                self.reRoll()
                self.DICE = [Die(), Die()]
                self.rollDice()
                self.POINTS = sum(self.ROLLED)

                print(self.ROLLED)
                print(f"Loot collected: {self.POINTS}")
        
        else:
            NEXT_ROUND = input("Roll Dice?(Y/n) ")
            if NEXT_ROUND.upper() == "Y" or NEXT_ROUND == "":
                self.reRoll()
            else:
                pass
            
            # --- PROCESS -- #
            self.rollDice()
            self.findDoubles()


            print(f"Rolled Dice: {str(self.ROLLED)[1:-1]}")

            ## checking if ship, captain, and crew is found
            if 6 in self.ROLLED and self.SHIP == False:
                self.SHIP = True
                print("Ship is found!")

            if 5 in self.ROLLED and self.SHIP == True and self.CAPTAIN == False:
                self.CAPTAIN = True
                print("Captain is found!")

            if 4 in self.ROLLED and self.SHIP == True and self.CAPTAIN == True and self.CREW == False:
                self.CREW = True
                print("Crew is found!")


                # if all are found, remove based on how long the list is 
                if len(self.DICE) == 5:
                    self.ROLLED.remove(6)
                    self.ROLLED.remove(5)
                    self.ROLLED.remove(4)

                if len(self.DICE) == 4:
                    self.ROLLED.remove(5)
                    self.ROLLED.remove(4)
                
                if len(self.DICE) == 3:
                    self.ROLLED.remove(4)

                #get the sum of remaining dice if ship, captain, crew found
                self.POINTS = sum(self.ROLLED)
                
                # --- OUTPUT --- #
                print(f"Loot collected: {self.POINTS}")

            if self.SHIP == True:
                self.DICE = [Die(), Die(), Die(), Die()]
            if self.CAPTAIN == True:
                self.DICE = [Die(), Die(), Die()]
            if self.CREW == True:
                self.DICE = [Die(), Die()]

        self.ROLL += 1


if __name__ == "__main__":
    PLAYER = Player()
