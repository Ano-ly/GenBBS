GenBBS User Guide

![GenBBS Logo](assets/images/GenBBS%20Logo.png)

Welcome to GenBBS! This application generates a bar bending schedule in Excel format, using bar information (bar diameter and type, lengths, etc). The application uses shape code formulas from BS 8666:2020 to calculate bar cut lengths.

This guide will walk you through how to use the application to manage your reinforcement bar projects and export them to Excel.


1. Getting Started


When you launch GenBBS, you'll be presented with the Main Menu Screen.

Create New Project: Click the "+" button to start a fresh project. You'll be prompted to enter a project name.

Open Existing Project: Click the "Open Existing File" button to load a previously saved project. A file dialog will appear, allowing you to navigate to your `.gbbs` project file.


2. Project Management

After creating or opening a project, you'll be taken to the Category Screen, which displays your project's hierarchical structure.


2.1 Project Structure

Your project is organized in a tree-like structure:

Project: The top-level container for your entire work.
Category (Higher): Major sections within your project, i.e first floor
Category (Lower): Sub-sections within a Higher Category, containing elements, i.e, first floor beams
Element: Specific components or parts that contain reinforcement bars, i.e, Beam 01

2.2 Navigating the Project Tree

The right panel displays your project's hierarchy. Click on any item (Project, Category, Element) to select it. Double-clicking an Element will take you to the Reinforcement Screen for that specific element.


2.3 Adding Items

1. Select a Parent: Click on the item in the tree where you want to add a new sub-item.

    *   To add a Category, select the Project or another Category (Higher).
    *   To add an Element, select a Category that does not contain any sub-categories

2. Enter Name/Quantity:

    *   For Categories: Type the name of the new category into the "Add Sub-Category" input field.
    *   For Elements: Type the name of the new element into the "Add Element" input field and its quantity into the "Quantity" field. Note: you can later edit the quantity in the reinforcement screen for that element.

3. Click Create: Click the corresponding "Create" button (e.g., "Create Sub-Category" or "Create Element").

4. Note: Once a category contains an element, another category cannot be created within it, and vice versa. After deleting all elements from a category, attempting to add a new category is not allowed. A new category must be created with the intention to  contain only sub-categories. 

This is because once an element is created in a category, it is automatically converted into a lower-type category which can contain only elements.

2.4 Renaming Items

Click on the item in the tree which you wish to rename. In the left panel, click on the edit button at the top right. Rename as desired 


2.5 Deleting Items

1.  Select Item: Click on the item you wish to delete in the project tree.

2. Click Delete: Click the button with a Waste Basket Icon. A confirmation dialog will appear.

3.  Confirm: Click "Yes" to permanently delete the item and all its contents. (Note: You cannot delete the root Project item).


2.6 Saving Your Project

Save Button: Click the "Save" button on the Category Screen to save your current project progress. If it's a new project, you'll be prompted to choose a file name and location.

Automatic Prompt: If you try to go back to the Main Menu or close the application with unsaved changes, you will be prompted to save your project.


3. Reinforcement Bar Details

When you double-click an Element in the Category Screen, you'll enter the Reinforcement Screen for that element.

3.1 Adding and Editing Bars

Add New Bar: Click the "Done" button to add a new reinforcement bar to the current element. A new row will appear in the table.

Edit Bar Properties: Click on any cell in the table to edit its value. This includes:
    * Shape Code: Enter the BS8666 shape code (e.g., "00", "11", "21").
    * Dimensions: Input the required dimensions (e.g., A, B, C, R) based on the selected shape code. The application will automatically generate a visual representation of the bar.
    * Other properties like diameter, number of bars, cut length, etc.

Bar Image Preview: As you enter the shape code and dimensions, a visual representation of the bar will be displayed, helping you verify the shape.


3.2 Deleting Bars

Select Row: Click on any cell in the row of the bar you wish to delete.

Click Delete: Click the Delete button on the bottom left. The selected bar will be removed from the element.

3.3 Sorting Bars

Click on the header of any column to sort bars in ascending or descending order based on that column.


4. Exporting to Excel

From the Category Screen, you can export your entire project data, including all reinforcement bar details and their visual shapes, to an Excel spreadsheet.


1. Click Export: Click the "Export" button.

2. Summaries: Select the categories for which you want summaries generated in the bar bending schedule.

3. Choose Save Location: A file dialog will appear, allowing you to choose the name and location for your Excel file (`.xlsx`).

4. Export Process: The application will generate all bar images, collect all project data, and format it into a comprehensive Excel report. This report will include:
    * Project hierarchy.
    * Quantities of elements.
    * Detailed bar bending schedule information.
    * Visual representations of each bar shape embedded directly into the spreadsheet.

5. Confirmation: Once the export is complete, a message will confirm the successful creation of the Excel file.

5. Settings
- Enable auto-generation of bar mark
- Enable warnings for bar dimensions
- Disable bar creation where warnings exist, i.e, bar will not be     created when a warning exists for any dimension in that bar.
- Enable keyboard shortcuts: 
  * Press Enter to create bar or complete bar edit
  * Press Delete to delete bar 
- Automatically input shape code dimensions and other bar information

6. More Information
- Minimum radii for bent bars as obtained from BS 8666 - 2020 Table 2
- Density of steel (7850 kg/m³)
- Values of q as obtained from BS 8666 - 2020

This guide should help you get started with GenBBS. If you have any further questions, please contact developer:

Aamrachi Catherine Uvere 
LinkedIn
Mail: amarachiuvere@gmail.com

© 2025 Amarachi Uvere. All rights reserved.
