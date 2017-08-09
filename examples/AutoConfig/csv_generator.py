from config_list import *
import os
import codecs
import csv

class CsvGenerator(object):
    def __init__(self, excel2csv_desc, **kwargs):
        self.excel2csv_desc = excel2csv_desc
        self.csv_content = None
        return super().__init__(**kwargs)
    
    def gen(self, log=None):
        out_csv_file_path = self.excel2csv_desc.out_csv_file_path
        if os.path.exists(out_csv_file_path) and os.path.isfile(out_csv_file_path):
            os.remove(out_csv_file_path)
        if not os.path.exists(os.path.dirname(out_csv_file_path)):
            os.makedirs(os.path.dirname(out_csv_file_path))
        with open(out_csv_file_path, 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            excel_desc = self.excel2csv_desc.excel_desc
            if csv_writer:
                csv_row = [field_desc.name_desc.name for field_desc in excel_desc.field_descs]
                csv_writer.writerow(csv_row)
                csv_row = [field_desc.type_desc.type for field_desc in excel_desc.field_descs]
                csv_writer.writerow(csv_row)
                for row in excel_desc.sheet_data.iter_rows(
                    min_col=excel_desc.min_column, 
                    max_col=excel_desc.max_column, 
                    min_row=excel_desc.start_row + 2
                    ):
                    csv_row = [x.value for x in row]
                    csv_writer.writerow(csv_row)
        return True
