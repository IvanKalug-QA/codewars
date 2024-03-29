# Something is wrong with our Warrior class. The strike method does not work correctly. The following shows an example of this code being used:
#
# ninja = Warrior('Ninja')
# samurai = Warrior('Samurai')
#
# samurai.strike(ninja, 3)
# # ninja.health should == 70
# Can you figure out what is wrong?

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        # health cannot go below zero
        enemy.health -= swings * 10
        if enemy.health < 0:
            enemy.health = 0