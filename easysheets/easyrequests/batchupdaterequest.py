"""Module for BatchUpdate class and other functionality."""
from typing import Optional
from easysheets.styling.colors import ColorStyleRGB

class BatchUpdate(dict):
    """Class for batch update requests as in the Google sheet API. """
    # consider getting a spreadsheet dump first, before creating some request / this could also be an optional choice
    def __init__(
        self, 
        *,
        include_spreadsheet_in_response: Optional[bool] = False,
        response_ranges: Optional[list[str]] = None,
        response_include_grid_data: bool = False
    ) -> None:
        self["includeSpreadsheetInResponse"] = include_spreadsheet_in_response
        if response_ranges and include_spreadsheet_in_response:
            self["responseRanges"] = response_ranges
        self['requests'] = []
        self["responseIncludeGridData"] = response_include_grid_data
        self.sheet_dict = dict()
        
    def append_easy_add_sheet_request(
        self, 
        *, 
        sheet_id: Optional[int] = None,
        title: Optional[str] = None,
        index: Optional[int]= None,
        row_count: int = 1000,
        column_count: int = 26,
        frozen_row_count: int = 0,
        frozen_col_count: int = 0,
        tab_color: Optional[tuple[int,int,int]] = None
        ) -> None:
        """Appends a create sheet request to the batch update object. The method
        purposely allows to add only some of the most used attributes of a newly created sheet.\n
        Updates the self.sheet_dict {SHEET_NAME: SHEET_ID}. The sheet_id is a often used value, 
        this can help to refer to this sheet later on."""
        if tab_color_style:
            tab_color_style = ColorStyleRGB.from_integer_rgb(*tab_color)

        easy_grid_properties = {
            "rowCount": row_count,
            "columnCount": column_count,
            "frozenRowCount": frozen_row_count,
            "frozenColumnCount": frozen_col_count,
        }
        properties = {
            "sheetId": sheet_id,
            "title": title,
            "index": index,
            "gridProperties": easy_grid_properties,
            "tabColorStyle": tab_color_style
        }

        request = {
            "properties": {
                properties
            }
        }
        self.requests.append(request)
        self.sheet_dict[title] = sheet_id

    def delete_sheet(self): ...
        
    def udpateCells(self): ...