import json

from UnitConstants import UnitName, UnitType

class UnitTemplate:
    can_be_damaged=False
    can_bombard=False
    can_strategic_bomb=False

    
class InfantryTemplate(UnitTemplate):

    attack=1
    defense=2
    movement=1
    cost=3
    unit_type=UnitType.Land
    supported_by=UnitName.Artillery

    
class ArtilleryTemplate(UnitTemplate):

    attack=2
    defense=2
    movement=1
    cost=4
    unit_type=UnitType.Land
    supported_by=UnitName.NoUnit


class TankTemplate(UnitTemplate):

    attack=3
    defense=3
    movement=2
    cost=6
    unit_type=UnitType.Land
    supported_by=UnitName.NoUnit

class MechanizedInfantry(UnitTemplate):

    attack=1
    defense=2
    movement=2
    cost=4
    unit_type=UnitType.Land
    supported_by=UnitName.Artillery
    
class FighterTemplate(UnitTemplate):

    attack=3
    defense=4
    movement=4
    cost=10
    unit_type=UnitType.Air
    supported_by=UnitName.Artillery
    
class TacticalBomberTemplate(UnitTemplate):

    attack=3
    defense=3
    movement=4
    cost=11
    unit_type=UnitType.Air
    supported_by=[UnitName.Fighter, UnitName.Tank]
    
class StrategicBomberTemplate(UnitTemplate):

    attack=4
    defense=1
    movement=6
    cost=12
    supported_by=UnitName.NoUnit
    can_strategic_bomb=True
