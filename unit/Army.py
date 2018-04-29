import random

import Unit
from UnitConstants import UnitName, UnitType, Stance

class Army:

    units = []
    retreat = False
    

    def __init__(self):
        self.stance = Stance.NoStance


    def get_num_units(self):
        return len(units)
        
    def add_unit(self, unit_enum):
        new_unit = None
        if unit_enum == UnitName.Infantry:
            new_unit = Unit.Infantry()
        elif unit_enum == UnitName.Artillery:
            new_unit = Unit.Artillery()
        elif unit_enum == UnitName.MechanizedInfantry:
            new_unit = Unit.MechanizedInfantry()
        elif unit_enum == UnitName.Tank:
            new_unit = Unit.Tank()
        elif unit_enum == UnitName.Fighter:
            new_unit = Unit.Fighter()
        elif unit_enum == UnitName.TacticalBomber:
            new_unit = Unit.TacticalBomber()
        elif unit_enum == UnitName.StrategicBomber:
            new_unit = Unit.StrategicBomber()

        if (new_unit):
            self.units.append(new_unit)


    def update_supports(self):
        for u in self.units:
            u.is_supported = False
        units_to_check = list(units)
        while len(units_to_check > 0):
            potential_supports = [x for x in units_to_check if (x.supported_by != UnitName.NoUnit)]
            if len(potential_supports == 0):
                break

            for unit in potential_supports:
                supported_by = unit.supported_by
                potential_supporters = [u for u in units_to_check if u.unit_name == supported_by]
                if len(potential_supporters==0):
                    units_to_check.remove(unit)
                else:
                    unit.is_supported = True
                    supporter = potential_supporters[0]
                    units_to_check.remove(supporter)
                    units_to_check.remove(unit)
                    break
        
            
    def attack(self):
        num_hits = 0
        self.update_supports()
        for u in self.units:
            roll = int(self.random.random()*6.0)
            attack = u.attack
            if u.is_supported:
                attack += 1
            if (roll <= attack):
                num_hits += 1

        if self.get_num_units() == 0:
            self.retreat = True
        return num_hits


    def defend(self):
        num_hits = 0
        for u in self.units:
            roll = int(self.random.random()*6.0)
            defense = u.defense
            if (roll <= defense):
                num_hits += 1

        if self.get_num_units() == 0:
            self.retreat = True
	return num_hits

    
    def remove_casualties(self, num_casualties, method = "simple"):
        if method = "simple":
            if self.stance=Stance.Attacking:
                self.units.sort(key=lambda x: x.attack)
            elif self.stance=Stance.Defending:
                self.units.sort(key=lambda x: x.defense)

            for i in range(num_casualties):
                self.units.pop(0)
                    
