from enum import Enum

class UnitType(Enum):

    NoType=0
    Land=1
    Air=2
    Sea=3


class UnitName(Enum):

    NoUnit=0
    Infantry=1
    Artillery=2
    MechanizedInfantry=3
    Tank=4
    Fighter=5
    TacticalBomber=6
    StrategicBomber=7
    Transport=8
    Destroyer=9
    Submarine=10
    Cruiser=11
    Carrier=12
    Battleship=13

class Stance(Enum):
    NoStance = 0
    Attacking = 1
    Defending = 2
