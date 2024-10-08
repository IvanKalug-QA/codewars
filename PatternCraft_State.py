# DESCRIPTION:
# The State Design Pattern can be used, for example, to manage the state of a tank in the StarCraft game.
#
# The pattern consists in isolating the state logic in different classes rather than having multiple ifs to determine what should happen.
#
# Your Task
# Complete the code so that when a Tank goes into SiegeMode it cannot move and its damage goes to 20. When it goes to TankMode it should be able to move and the damage should be set to 5.
#
# You have 3 classes:
#
# Tank: has a state, canMove and damage properties
# SiegeState and TankState: has canMove and damage properties
# Note: The tank initial state should be TankState.
#
# Resources

class SiegeState:
    def __init__(self):
        self.canMove = False
        self.damage = 20


class TankState:
    def __init__(self):
        self.canMove = True
        self.damage = 5


class Tank:
    def __init__(self):
        self.state = TankState()

    def can_move(self):
        return self.state.canMove

    def damage(self):
        return self.state.damage