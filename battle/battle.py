from Army import Army

class Battle:

    attacker=Army()
    defender=Army()

    def __init__(self, attacker_, defender_):
        self.attacker=attacker_
        self.defender=defender_

    def run_round(self):
        attack_hits = self.attacker.attack()
        defense_hits = self.defender.defend()
        self.attacker.remove_casualties(defense_hits)
        self.defender.remove_casualties(attack_hits)


    def run_battle(self):
        while (attacker.retreat==False and defender.retreat==False):
            self.run_round()
