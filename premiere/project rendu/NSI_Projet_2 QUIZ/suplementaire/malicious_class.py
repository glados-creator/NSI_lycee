import dataclasses
import typing

@dataclasses.dataclass
class lbin : list[typing.Union[int,bool]]
"""
juste une wrapper pour le binnaire python qui commence par 0bxxx
donc on l'enleve et du coup on fait une list
"""

@dataclasses.dataclass
class __base:
    name : str
    base : int
    Nsignificand : int 
    bias : int
    Nmantissa : int 

"""
on peut remplacer toute les property par une dataclass
"""