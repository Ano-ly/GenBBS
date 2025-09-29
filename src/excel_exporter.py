import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side
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
        all_headers = set()
        for row in hierarchical_rows:
            all_headers.update(row.keys())
        
        # Define a consistent order for common headers
        ordered_headers = ["Type", "Level", "Name", "Path"]
        # Add other headers, ensuring no duplicates and maintaining order
        for header in sorted(list(all_headers - set(ordered_headers))):
            ordered_headers.append(header)

        df = pd.DataFrame(hierarchical_rows, columns=ordered_headers)

        try:
            writer = pd.ExcelWriter(file_path, engine='openpyxl')
            df.to_excel(writer, sheet_name='Project Data', index=False)
            workbook = writer.book
            worksheet = writer.sheets['Project Data']

            # Apply formatting
            header_font = Font(bold=True)
            project_fill = PatternFill(start_color="DDEBF7", end_color="DDEBF7", fill_type="solid") # Light Blue
            category_higher_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid") # Light Green
            category_lower_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid") # Light Orange
            element_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # Light Peach
            bar_fill = PatternFill(start_color="F8F8F8", end_color="F8F8F8", fill_type="solid") # Light Gray

            thin_border = Border(left=Side(style='thin'),
                                 right=Side(style='thin'),
                                 top=Side(style='thin'),
                                 bottom=Side(style='thin'))

            # Apply header formatting
            for col_num, value in enumerate(df.columns.values):
                worksheet.cell(row=1, column=col_num + 1).font = header_font
                worksheet.cell(row=1, column=col_num + 1).border = thin_border

            # Apply row formatting and grouping
            for r_idx, row_data in df.iterrows():
                row_type = row_data["Type"]
                row_level = row_data["Level"]
                
                fill = None
                if row_type == "Project":
                    fill = project_fill
                elif row_type == "CategoryHigher":
                    fill = category_higher_fill
                elif row_type == "CategoryLower":
                    fill = category_lower_fill
                elif row_type == "Element":
                    fill = element_fill
                elif row_type == "Bar":
                    fill = bar_fill

                for col_num in range(1, len(df.columns) + 1):
                    cell = worksheet.cell(row=r_idx + 2, column=col_num)
                    if fill:
                        cell.fill = fill
                    cell.border = thin_border
                
                # Set outline level for grouping
                worksheet.row_dimensions[r_idx + 2].outlineLevel = row_level
                worksheet.row_dimensions[r_idx + 2].hidden = False # Ensure rows are visible by default

            # Auto-fit columns
            for col in df.columns:
                max_length = 0
                column = get_column_letter(df.columns.get_loc(col) + 1)
                for cell in worksheet[column]:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[column].width = adjusted_width

            writer.close()
            QMessageBox.information(None, "Export Successful", f"Project data exported to {file_path}")
        except Exception as e:
            QMessageBox.critical(None, "Export Error", f"Failed to export data: {e}")