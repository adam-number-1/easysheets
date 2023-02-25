"""This modules containes convencience classes for formatting with the userEnteredFormat,
when writing a formated input into a spreadsheet with the updateCells request
of the batchUpdate request following the Google Sheet API logic."""
from easysheets.styling.colors import ColorStyleRGB
from easysheets.writing.text_enums import (
    HorizontalAlign,
    TextDirection,
    VerticalAlign,
    WrapStrategy
)

class Writer(dict):
    def __init__(self) -> None:
        super().__init__()

    def background_color(self, color: tuple) -> None:
        """Adds a background color to the writer. Anything writen using the writer
        afetr caling this method will reside in a cell with the background color given
        this method."""
        background_color_style = ColorStyleRGB.from_integer_rgb(*color)
        self["backgroundColorStyle"] = background_color_style

    def text_color(self, color: tuple) -> None:
        """This method sets the text color of the writer. Anything you write into the cells
        after setting the color will have this foreground color."""
        foreground_color_style = ColorStyleRGB.from_integer_rgb(*color)
        if not self["textFormat"]:
            self["textFormat"] = {
                "foregroundColorStyle": {
                    foreground_color_style
                }
            }
            return
        self["textFormat"]["foregroundColorStyle"] = foreground_color_style

    def horizontal_alingment(self, alignment_value: HorizontalAlign)-> None:
        """Sets a horizontal alignment to a writer object. As a parameter, put some
        of the HorizontalAlign enum class values - LEFT,CENTER,RIGHT\n
        Example: 
        writer.horizontal_alingment( HorizontalAlign.RIGHT )"""
        self["horizontalAlignment"] = alignment_value.value

    def vertical_alingment(self, alignment_value: VerticalAlign)-> None:
        """Sets a vertical alignment alignment to a writer object. As a parameter, put some
        of the VerticalAlign enum class values - TOP,MIDDLE,BOTTOM\n
        Example: 
        writer.vertical_alingment( VerticalAlign.TOP )"""
        self["verticalAlignment"] = alignment_value.value    

    def wrap_strategy(self, strategy_value: WrapStrategy)-> None:
        """Sets a wrap strategy to a writer object. As a parameter, put some
        of the WrapStrategy enum class values - OVERFLOW_CELL,LEGACY_WRAP,CLIP,WRAP
        Example: 
        writer.wrap_strategy( WrapStrategy.OVERFLOW_CELL )"""
        self["wrapStrategy"] = strategy_value.value

    def text_direction(self, direction_value: TextDirection) -> None:
        """Sets a test orientation to a writer object. As a parameter, put some
        of the TextDirection enum class values - LEFT_TO_RIGHT,RIGHT_TO_LEFT
        Example: 
        writer.text_direction( WrapStrategy.OVERFLOW_CELL )"""
        self["textDirection"] = direction_value.value   

class BooleanWriter(Writer): ...

class FormulaWriter(Writer): ...

class LinkWriter(Writer): ... 

class NumberWriter(Writer):
    def number_format(self): ...

class TextWriter(Writer): ...

    