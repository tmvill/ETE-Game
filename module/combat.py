from classes import Player, NPC
from healthbar import HealthBar

class Combat:
    def __init__(self, player = Player, target = NPC, inCombat:bool = False):
        self.player = Player
        self.target = NPC
        self.inCombat = inCombat