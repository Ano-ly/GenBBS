import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.cell_range import CellRange
from src.logic.data_models import Project, CategoryHigher, CategoryLower, Element, Bar
from PySide6.QtWidgets import QFileDialog, QMessageBox
from typing import List, Dict, Any, Union

class ExcelExporter:

    @staticmethod
    def _collect_hierarchical_data_recursive(item: Union[Project, CategoryHigher, CategoryLower, Element, Bar],
                                            level: int,
                                            parent_path: List[str],
                                            hierarchical_rows: List[Dict[str, Any]]):
        item_type = type(item).__name__
        item_name = getattr(item, 'name', '') if hasattr(item, 'name') else ''
        current_path = parent_path + [item_name]

        row_data = {
            "Type": item_type,
            "Level": level,
            "Name": item_name,
            "Path": " > ".join(current_path)
        }

        if isinstance(item, Bar):
            row_data.update(item.to_dict())

        hierarchical_rows.append(row_data)

        if isinstance(item, Project):
            for category in item.categories:
                ExcelExporter._collect_hierarchical_data_recursive(category, level + 1, current_path, hierarchical_rows)
        elif isinstance(item, CategoryHigher):
            for child in item.children:
                ExcelExporter._collect_hierarchical_data_recursive(child, level + 1, current_path, hierarchical_rows)
        elif isinstance(item, CategoryLower):
            for element in item.elements:
                ExcelExporter._collect_hierarchical_data_recursive(element, level + 1, current_path, hierarchical_rows)
        elif isinstance(item, Element):
            for bar in item.bars:
                ExcelExporter._collect_hierarchical_data_recursive(bar, level + 1, current_path, hierarchical_rows)

    @staticmethod
    def export_project_bars_to_excel(project: Project, file_path: str):
        if not project:
            QMessageBox.warning(None, "Export Error", "No project loaded to export.")
            return

        hierarchical_rows = []
        ExcelExporter._collect_hierarchical_data_recursive(project, 0, [], hierarchical_rows)

        # Determine all possible column headers
        # all_headers = set()
        # for row in hierarchical_rows:
        #     all_headers.update(row.keys())
        ordered_headers = ["Type", "Level", "Name", "Path", "bar_mark", "diameter", "number_of_bars", "cut_length", "unit_weight", "total_weight", "shape_code", "lengths"]
        df = pd.DataFrame(hierarchical_rows, columns=ordered_headers)

        try:
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Project Data', index=False)
                workbook = writer.book
                worksheet = writer.sheets['Project Data']

                #styles
                header_font = Font(bold=True)
                category_font = Font(bold=True, size=16, underline="single")
                element_font = Font(size=12, underline="single")
                bar_font = Font(size=10)
                project_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid") #
                normal_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

                thin_border = Border(left=Side(style='thin'),
                                    right=Side(style='thin'),
                                    top=Side(style='thin'),
                                    bottom=Side(style='thin'))

                header_row_idx = 1
                header_row = next (worksheet.iter_rows(min_row=1, max_row=1, values_only=True))
                col_map = {name: idx for idx, name in enumerate(header_row)}
                #Headers of columns to be deleted
                target_headers = ["Type", "Level", "Path", "bar_id", "parent_tree", "Name"]
                #Current cell headers and their corresponding proper cell headers for Bar Bending Schedule
                proper_cell_headers = {"bar_mark": "Bar Mark", "bar_id": "Bar ID", "shape_code": "Shape Code", "number_of_bars":"No. in Each", "cut_length" : "Cut Length", "unit_weight": "Unit Weight", "total_weight": "Total Weight", "diameter" : "Type and Bar Size"}
                list_of_names = dict()
                max_widths_of_columns = dict()

                for row in worksheet.iter_rows():
                    row_index = row[0].row

                    # Header row formatting
                    if row_index == 1:
                        for cell in row:
                            cell.font = header_font
                            cell.border = thin_border                       
                    #Height formatting
                    worksheet.row_dimensions[row_index].height = 60               
                    #color, font and alignment formatting
                    center_align = Alignment(horizontal="center", vertical="center")
                    row_type = row[col_map["Type"]].value
                    row_level = row[col_map["Level"]].value
                    #Store the names of sub headers
                    if row_type != "Bar":
                        row_name = row[col_map["Name"]].value
                        list_of_names[row_index] = row_name.upper()
                    fill = normal_fill
                    font = None
                    # row_name = row[col_map["Name"]].value
                    if row_type == "Project":
                        fill = project_fill
                        font = category_font
                    elif row_type == "CategoryHigher" or row_type == "CategoryLower":
                        font = category_font
                    elif row_type == "Element":
                        font = element_font
                    elif row_type == "Bar":
                        font = bar_font
                    for cell in row:
                        #Set alignment
                        column_name = next((k for k, v in col_map.items() if v == cell.column - 1), None)
                        max_widths_of_columns[column_name] = max(max_widths_of_columns.get(column_name, 0), len(str(cell.value)))
                        print(cell.value)
                        print(max_widths_of_columns)
                        cell.alignment = center_align
                        if row_index != header_row_idx:
                            if fill:
                                cell.fill = fill
                            if font:
                                cell.font = font
                            cell.border = thin_border        
                    # Set outline level for grouping
                    if row_index != header_row_idx:
                        worksheet.row_dimensions[row_index].outlineLevel = int(row_level)
                        worksheet.row_dimensions[row_index].hidden = False
                        
                for col in range(worksheet.max_column, 0, -1):
                    cell_value = worksheet.cell(row=header_row_idx, column=col).value
                    #Delete irrelevant columns
                    if cell_value in target_headers:
                        worksheet.delete_cols(col)
                        continue
                for col in range(worksheet.max_column, 0, -1):
                    print(col)
                    cell_value = worksheet.cell(row=header_row_idx, column=col).value
                    #Adjust column width
                    column = get_column_letter(col)
                    adjusted_width = max((max_widths_of_columns.get(cell_value, 0), len(proper_cell_headers.get(cell_value, cell_value)))) + 2
                    print(f"Adej: {adjusted_width}, {cell_value}")
                    worksheet.column_dimensions[column].width = adjusted_width    
                    #Change column or header names to appropriate ones
                    if cell_value in proper_cell_headers.keys():
                        worksheet.cell(row=header_row_idx, column=col, value=proper_cell_headers[cell_value])

                #Add names of sub-headers to the first row of each sub-header group
                header_row_trimmed = next (worksheet.iter_rows(min_row=1, max_row=1, values_only=True))
                col_map_trimmed = {name: idx for idx, name in enumerate(header_row_trimmed)}
                for row in worksheet.iter_rows():
                    row_index = row[0].row
                    if row_index != 1:
                        row_bar_mark = row[col_map_trimmed["Bar Mark"]].value
                        if row_bar_mark == "" or row_bar_mark is None:
                            worksheet.merge_cells(start_row=row_index, start_column=1, end_row=row_index, end_column=worksheet.max_column)
                            worksheet.cell(row=row_index, column=1, value=list_of_names[row_index])
                
                QMessageBox.information(None, "Export Successful", f"Project data exported to {file_path}")
        except Exception as e:
            QMessageBox.critical(None, "Export Error", f"Failed to export data: {e}")
