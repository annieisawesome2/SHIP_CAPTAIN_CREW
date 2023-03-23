from random import randint

class Die():
    def __init__(self):
        #constructor for the object
        self.DIE_MAX = 6
        self.DIE_NUM = None

    # Mutator Methods
    def rollDie(self):
        """update die with new number"""
        self.DIE_NUM = randint(1, self.DIE_MAX)
     
    def displayDie(self):
        """Print the number"""
        print(self.DIE_NUM)