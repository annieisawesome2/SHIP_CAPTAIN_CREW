from b_player import Player

class Game:
    """Provide the structure for the turns and win condition of the game"""

    def __init__(self, NAME1, NAME2):
        self.PLAYER1 = Player()
        self.PLAYER2 = Player()
        self.NAME1 = NAME1
        self.NAME2 = NAME2
        self.TURNS = 3

    def run(self):
        while self.TURNS != 0:
        # --- PLAYER 1 TURN --- #
            print(f"{self.NAME1}'s Turn!")
            self.player_1_turn()
            print("-------------")

            if self.PLAYER1.DOUBLES == True:
                if self.PLAYER2.CREW == True:
                    self.PLAYER2.CREW = False
                    self.PLAYER1.CREW = True
                    print(f"{NAME1} kidnapped {NAME2}'s crew and stole ALL the loot")
                    self.PLAYER2.setDice(3)
                    self.PLAYER1.POINTS = self.PLAYER1.POINTS + self.PLAYER2.POINTS
                    self.PLAYER2.POINTS = 0
                    print(f"{NAME1}'s points: {self.PLAYER1.POINTS}")
                
                elif self.PLAYER2.CAPTAIN == True:
                    self.PLAYER2.CAPTAIN = False
                    self.PLAYER1.CAPTAIN = True
                    self.PLAYER2.setDice(4)
                    print(f"{NAME1} kidnapped {NAME2}'s captain")

                elif self.PLAYER2.SHIP == True:
                    self.PLAYER2.SHIP = False
                    self.PLAYER1.SHIP = True
                    print(f"{NAME1} stole {NAME2}'s ship")
                    self.PLAYER2.setDice(5)
                self.PLAYER1.DOUBLES = False
            
            # --- PLAYER 2 TURN --- #
            print(f"{self.NAME2}'s Turn!")
            self.player_2_turn()
            print("-------------")

            if self.PLAYER2.DOUBLES == True:
                if self.PLAYER1.CREW == True:
                    self.PLAYER1.CREW = False
                    self.PLAYER2.CREW = True
                    print(f"{NAME2} kidnapped {NAME1}'s crew and stole ALL their loot")
                
                    self.PLAYER1.setDice(3)
                    self.PLAYER2.POINTS = self.PLAYER1.POINTS + self.PLAYER2.POINTS
                    self.PLAYER1.POINTS = 0
                    print(f"{NAME2}'s points: {self.PLAYER2.POINTS}")

                elif self.PLAYER1.CAPTAIN == True:
                    self.PLAYER1.CAPTAIN = False
                    self.PLAYER2.CAPTAIN = True
                    print(f"{NAME2} kidnapped {NAME1}'s captian")
                    self.PLAYER1.setDice(4)

                elif self.PLAYER1.SHIP == True:
                    self.PLAYER1.SHIP = False
                    self.PLAYER2.SHIP = True
                    print(f"{NAME2} stole {NAME1}'s ship")
                    self.PLAYER1.setDice(5)
                self.PLAYER2.DOUBLES = False

            self.TURNS -= 1
            if self.TURNS == 0:
                print(self.PLAYER1.POINTS)
                print(self.PLAYER2.POINTS)
                if self.PLAYER1.POINTS > self.PLAYER2.POINTS:
                    print(f"{NAME1} Wins")
                    exit()
                elif self.PLAYER2.POINTS > self.PLAYER1.POINTS:
                    print(f"{NAME2} Wins")
                    exit()
                else:
                    print("It's a tie")
                    exit()
    
    def player_1_turn(self):
        self.PLAYER1.turn()
    
    def player_2_turn(self):
        self.PLAYER2.turn()
   

if __name__ == "__main__":
    NAME1 = input("Player 1 name: ")
    NAME2 = input("Player 2 name: ")
    GAME = Game(NAME1, NAME2)
    PLAYER1 = Player()
    PLAYER2 = Player()
    GAME.run()

