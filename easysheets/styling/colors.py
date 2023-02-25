"""This module contains some of the calsses and functionality, that contributes on setting style
Of various spreadsheets objects"""
from enum import Enum
class RGBPreset(Enum):
    RED: tuple[float,float,float] = (1.0,0.0,0.0)
    GREEN: tuple[float,float,float] = (0.0,1.0,0.0)
    BLUE: tuple[float,float,float] = (0.0,0.0,1.0)

class ColorStyleRGB(dict):
    def __init__(self, red: float, green: float, blue: float, *, alpha: float = 0.0):
        self['red'] = red
        self['green'] = green
        self['blue'] = blue
        self['alpha'] = alpha

    @classmethod
    def from_integer_rgb(cls, red: int, green: int, blue: int, *, alpha: float = 0.0):
        """Alternative constructor for colorstyle object, which allows choosing a color by providing its RGB values
        and the optional aplha channel float value."""
        new_color_style = cls(red/255, green/255, blue/255, alpha)
        return new_color_style     

    @classmethod
    def from_enum(cls, color_preset: RGBPreset, *, alpha: float = 0.0):
        """Alternative constructor for colorstyle object, which allows choosing a color from enum,
        rather than figuring out the numerical values."""
        new_color_style = cls(*(color_preset.value), alpha)
        return new_color_style