from UnitConstants import UnitName
from UnitTemplate import UnitTemplate

class Unit(object):

    # constants
    attack=0
    defense=0
    movement=0
    cost=0
    unit_name=UnitName.NoUnit
    unit_type=UnitType.NoType
    supported_by = UnitName.NoUnit

    # dynamics
    can_be_damaged=False
    is_damaged=False
    movement_remaining=0
    is_supported = False
    is_casualty = False

    def __init__(self, unit_enum):
        template = None
        if unit_enum == UnitName.Infantry:
            template = UnitTemplate.InfantryTemplate
        elif unit_enum == UnitName.Artillery:
            template = UnitTemplate.ArtilleryTemplate
        elif unit_enum == UnitName.MechanizedInfantry:
            template = UnitTemplate.MechanizedInfantryTemplate
        elif unit_enum == UnitName.Tank:
            template = UnitTemplate.TankTemplate
        elif unit_enum == UnitName.Fighter:
            template = UnitTemplate.FighterTemplate
        elif unit_enum == UnitName.TacticalBomber:
            template = UnitTemplate.TacticalBomberTemplate
        elif unit_enum == UnitName.StrategicBomber:
            template = UnitTemplate.StrategicBomberTemplate

        if(template):
            self.attack = template.attack
            self.defense = template.defense
            self.movement = template.movement
            self.cost = template.cost
            self.unit_name = unit_enum
            self.unit_type = template.unit_type
            self.can_be_damaged=template.can_be_damaged
            self.can_strategic_bomb=template.can_strategic_bomb
            self.supported_by = template.supported_by
        

class Infantry(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.Infantry)

        
class Artillery(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.Artillery)

        
class MechanizedInfantry(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.MechanizedInfantry)
        
class Tank(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.Tank)
        
class Fighter(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.Fighter)
        
class TacticalBomber(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.TacticalBomber)
        
class StrategicBomber(Unit):

    def __init__(self):
        Unit.__init__(self, UnitName.StrategicBomber)
