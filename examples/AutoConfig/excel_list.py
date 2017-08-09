import os
import openpyxl
from define import STRING_EMPTY, excel_column, excel_coordinate


class ExcelFiledNameDescript(object):
    def __init__(self, **kwargs):
        self.field_desc = None
        self.name = STRING_EMPTY
        return super().__init__(**kwargs)

    def init(self, excel_desc):
        pass


class ExcelFieldTypeDescript(object):
    def __init__(self, **kwargs):
        self.field_desc = None
        self.type = STRING_EMPTY
        return super().__init__(**kwargs)

    def init(self, excel_desc):
        pass


class ExcelFieldDescript(object):
    def __init__(self, **kwargs):
        self.excel_desc = None
        self.column = ""
        self.name_desc = None
        self.type_desc = None
        return super().__init__(**kwargs)

    def init(self, excel_desc, column, name_str, type_str):
        pass


class ExcelDescript(object):
    def __init__(self, **kwargs):
        self.start_row = -1
        self.min_column = -1
        self.max_column = -2
        self.field_descs = []
        self.sheet_data = None
        return super().__init__(**kwargs)

    def init(self, sheet_data):
        self.sheet_data = sheet_data
        self.start_row = int(sheet_data[excel_coordinate(1, 1)].value)
        if self.start_row <= 0: 
            return False
        for name_cell, type_cell in self.sheet_data.iter_cols(min_row=self.start_row, max_row=self.start_row+1):
            if not name_cell.value or not type_cell.value:
                if self.min_column < 0: continue
                else: break
            if self.min_column < 0: 
                self.min_column = name_cell.col_idx
            self.max_column = name_cell.col_idx
            field_desc = ExcelFieldDescript()
            if field_desc.init(self, name_cell.col_idx, name_cell.value, type_cell.value):
                self.field_descs.append(field_desc)
            
    @staticmethod
    def load(file_path, sheet_name):
        excel_desc = None
        if os.path.exists(file_path) and os.path.isfile(file_path):
            xls_data = openpyxl.load_workbook(file_path)
            if xls_data and sheet_name in xls_data.sheetnames:
                excel_desc = ExcelDescript()
                if not excel_desc.init(xls_data[sheet_name]):
                    excel_desc = None
        return excel_desc