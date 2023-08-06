# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import sys
import os

# Custom Packages
from AthenaColor.Data.General import EscCodes

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "AthenaColorInitClass", "init"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Init Classes -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaColorInitClass:
    _esc=EscCodes.hex
    _roundUp = True
    _transparentDefault = ("ff",255)
    _decimalPlaces = 3
    _stringSeparation = ";"

    def __init__(self):
        # prep the console for colors
        if sys.platform == 'win32':
            os.system("color")

    @property
    def esc(self):
        return self._esc
    @esc.setter
    def esc(self,value):
        if value in (EscCodes.hex,EscCodes.uni,EscCodes.octal):
            self._esc = value
        else:
            raise ValueError

    @property
    def transparentDefault(self):
        return self._transparentDefault
    @transparentDefault.setter
    def transparentDefault(self,value:int|str):
        if isinstance(value, float|int) and 0 <= value <= 255:
            self._transparentDefault = ("%02x" % round(value), value)
        elif isinstance(value, str) and len(value) == 2:
            value_int = int(value[0:2], 16)
            if not value_int in range(256):
                raise ValueError
            self._transparentDefault = (value,value_int)
        else:
            raise ValueError

    @property
    def decimalPlaces(self) -> int:
        return self._decimalPlaces
    @decimalPlaces.setter
    def decimalPlaces(self,value):
        if isinstance(value,int) and value >= 0:
            self._decimalPlaces = value
        else:
            raise ValueError

    @property
    def stringSeparation(self) -> str:
        return self._stringSeparation

    @stringSeparation.setter
    def stringSeparation(self, value:str):
        if isinstance(value,str):
            self._stringSeparation = value
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f"""
AthenaColorInitClass(
roundUp={self._roundUp}, 
esc={self._esc.encode()}, 
transparentDefault={self.transparentDefault}, 
decimalPlaces={self.decimalPlaces}, 
stringSeparation='{self.stringSeparation}'
)""".replace("\n","")

# ----------------------------------------------------------------------------------------------------------------------
# - Init Object -
# ----------------------------------------------------------------------------------------------------------------------
init = AthenaColorInitClass()