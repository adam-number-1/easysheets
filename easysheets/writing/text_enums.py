"""This module just reflects the formatting Enumerations from Google Sheets API,
which are used to popuate some values of the sheets requests."""
from enum import Enum

class HorizontalAlign(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"

class VerticalAlign(Enum):
    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"

class WrapStrategy(Enum):
    OVERFLOW_CELL = "OVERFLOW_CELL"
    LEGACY_WRAP = "LEGACY_WRAP"
    CLIP = "CLIP"
    WRAP = "WRAP"

class TextDirection(Enum): 
    TEXT_DIRECTION_UNSPECIFIED = "TEXT_DIRECTION_UNSPECIFIED"
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"