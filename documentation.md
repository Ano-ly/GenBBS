# GenBBS Application Documentation

This document explains the core functionalities and backend workings of the GenBBS application.

## 1. Project Management (`src/main.py`)

The `src/main.py` file handles the core application flow, UI screens, and the management of the project data in memory.

*   **Application Structure:** The application uses a `QStackedWidget` to switch between different screens: `LoadingScreenWidget`, `MainMenuScreen`, `NewProjectScreen`, `Category1Screen`, and `ReinforcementScreen`.
*   **Loading/Creating Projects:**
    *   **New Project:** When a user creates a new project via the `NewProjectScreen`, a new `Project` object (defined in `src/logic/data_models.py`, not provided in the context but inferred) is instantiated in memory with the given name. This `Project` object becomes `self.app_window.current_project`.
    *   **Existing Project:** Users can open existing projects through a `QFileDialog`. The selected `.gbbs` file (which is a JSON file) is read, and its content is parsed using `json.load()`. The `Project.from_dict()` method (inferred from `main.py` line 57) is then used to reconstruct the `Project` object and its nested `CategoryHigher`, `CategoryLower`, `Element`, and `Bar` objects from the JSON data.
*   **Saving Projects:** The `Category1Screen.save_current_project` method is responsible for saving the current project. It serializes the `self.app_window.current_project` object into a JSON format using `json.dumps()` and writes it to a `.gbbs` file. If `self.app_window.current_project_file_path` is `None` (for a new project), a `QFileDialog` prompts the user to choose a save location.
*   **Hierarchical Structure Management (`Category1Screen`):
    *   The `Category1Screen` displays the project's hierarchical structure (Project -> CategoryHigher -> CategoryLower -> Element) using a `QTreeWidget`.
    *   **Adding Items:**
        *   `Category1Screen.add_new_category`: Creates new `CategoryHigher` objects and adds them as children to the currently selected `Project` or `CategoryHigher` object in the data model.
        *   `Category1Screen.add_new_element`: Creates new `Element` objects with a specified quantity and adds them as children to the currently selected `CategoryLower` or `CategoryHigher` (if it has no children) object.
    *   **Deleting Items (`Category1Screen.delete_selected_item`):** When an item is selected in the `QTreeWidget` and the delete button is clicked, the corresponding object is removed from its parent's `children` or `elements` list in the in-memory data model. The `QTreeWidget` is then repopulated to reflect this change.
*   **Bar Management (`ReinforcementScreen`):
    *   The `ReinforcementScreen` is dedicated to managing `Bar` objects associated with a specific `Element`.
    *   It uses a `QTableWidget` to display the properties of each bar (shape code, dimensions, etc.).
    *   **Creating/Editing Bars:** Users can add new bars or modify existing ones. The `handle_add_bar_button_clicked` and `handle_bar_table_item_changed` methods (inferred from the code) are responsible for updating the `Bar` objects within the `self.element.bars` list. This involves validating input (e.g., shape code, dimensions) and updating the `Bar` object's properties.

## 2. Bar Image Generation (`src/utils/bar_image_generator.py`)

The `src/utils/bar_image_generator.py` module is responsible for creating visual representations of reinforcement bars based on their shape code and dimensions.

*   **`generate_bar_image` function:** This is the core function.
    *   **Inputs:** It takes `shape_code` (a string representing the bar's shape, e.g., "00", "11"), `dimensions` (a dictionary mapping labels like 'A', 'B', 'C' to numeric values), a unique `bar_id`, and an `output_dir` for saving the image.
    *   **Matplotlib Usage:** It uses the `matplotlib.pyplot` library to draw the bar shapes.
        *   A figure and axes are created, and the aspect ratio is set to 'equal' to prevent distortion. The axes are turned off to hide numerical scales.
        *   A helper function `draw_segment` is used to draw straight line segments with optional labels.
        *   `matplotlib.patches.Arc` is used to draw curved sections of the bar.
        *   `ax.text` is used to add dimension labels (e.g., "A:1000") to the drawing.
    *   **Shape Code Logic:** The function contains a series of `if/elif` statements that check the `shape_code` and draw the corresponding bar geometry using combinations of `draw_segment` and `Arc` patches.
    *   **Output:** The generated plot is saved as a PNG image file in the specified `output_dir` with a filename incorporating the `shape_code` and `bar_id`. The path to this saved image is returned.

## 3. Excel Export (`src/excel_exporter.py`)

The `src/excel_exporter.py` module handles the export of the entire project data, including bar images, to an Excel spreadsheet.

*   **`export_project_bars_to_excel` function:** This is the main entry point for exporting.
    *   **Element Quantities Collection (`ExcelExporter._collect_element_quantities`):** It first traverses the project structure to collect the quantities of all `Element` objects. This is crucial for adjusting bar quantities later.
    *   **Hierarchical Data Collection (`ExcelExporter._collect_hierarchical_data_recursive`):** This recursive function traverses the entire project hierarchy (Project, CategoryHigher, CategoryLower, Element, Bar).
        *   For each `Bar` object encountered, it calls `generate_bar_image` to create a temporary image file of the bar shape. The path to this image is stored in the `image_path` field of the row data.
        *   It also calls `ExcelExporter._compute_adjusted_bar_properties` to calculate `total_no_of_bars`, `total_length`, and `total_weight` by multiplying the bar's properties by the quantity of its parent `Element`.
        *   The collected data for each item (Project, Category, Element, Bar) is appended as a dictionary to `hierarchical_rows`.
    *   **DataFrame Creation:** The `hierarchical_rows` are converted into a `pandas.DataFrame` with a predefined order of columns.
    *   **Excel Writing (using `openpyxl`):
        *   The DataFrame is written to an Excel sheet named "Project Data".
        *   **Styling and Formatting:** `openpyxl` is used to apply extensive formatting:
            *   Fonts (bold, size, underline) for headers, categories, elements, and bars.
            *   Fill colors for project rows.
            *   Thin borders for all cells.
            *   Alignment (center for bar data, left for hierarchical names).
            *   Row heights are adjusted.
            *   Column widths are adjusted based on content length and predefined headers.
            *   Column headers are renamed to more appropriate names (e.g., "bar_mark" to "Bar Mark").
        *   **Image Embedding:** For rows corresponding to `Bar` objects that have an `image_path`:
            *   An `openpyxl.drawing.image.Image` object is created from the temporary image file.
            *   The image's width and height are adjusted.
            *   The image is embedded into the "Shape" column of the Excel sheet using `worksheet.add_image(img, anchor)`. The `anchor` is created using `OneCellAnchor` and `AnchorMarker` to specify the exact cell and any `x_offset` or `y_offset` for precise positioning.
        *   **Column Deletion:** Irrelevant columns like "Type", "Level", "Path", "image_path", etc., are deleted from the final Excel output.
        *   **Grouping:** Outline levels are set for rows to enable grouping/collapsing in Excel, reflecting the project's hierarchy.
        *   **Sub-header Names and Quantities:** Logic is in place to merge cells and display the names and quantities of categories and elements as sub-headers within the Excel sheet.
    *   **Temporary File Cleanup:** After embedding, the temporary bar image files are deleted from the file system.
    *   **User Feedback:** A `QMessageBox` informs the user about the success or failure of the export operation.