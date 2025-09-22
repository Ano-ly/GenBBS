import uuid
from datetime import datetime

class Bar:   
    """
    This class will hold all the details for a single bar mark.
    """
    def __init__(self, bar_mark: int, shape_code: str, diameter: str, lengths: dict, number_of_bars: int):
        self.bar_id = str(uuid.uuid4()) # Unique ID for each bar
        self.bar_mark = bar_mark
        self.shape_code = shape_code
        self.diameter = diameter # Now a string, e.g., 'Y10'
        self.lengths = lengths
        self.number_of_bars = number_of_bars
        self.cut_length = self.calculate_cut_length()
        self.unit_weight, self.total_weight = self.calculate_weight()

    def calculate_cut_length(self) -> float:
        """
        Implements the logic for each shape code to determine the developed length.
        This method will be crucial for BS 8660:2020 compliance, handling bend allowances and deductions.
        (Implementation details for specific shape codes will go here)
        """
        # Placeholder for actual BS 8660:2020 calculation logic
        # For now, a simple sum of lengths for demonstration
        return sum(self.lengths.values()) / 1000.0 # Convert mm to meters

    def calculate_weight(self) -> tuple[float, float]:
        """
        Calculates unit_weight and total_weight based on diameter, cut_length, and number_of_bars.
        Standard steel density ~7850 kg/m³
        """
        # Extract numeric diameter from string (e.g., 'Y10' -> 10)
        numeric_diameter = float(''.join(filter(str.isdigit, self.diameter)))

        # Convert diameter from mm to meters for calculation
        diameter_m = numeric_diameter / 1000.0
        area = 3.14159 * (diameter_m / 2)**2
        unit_weight = area * 7850 # kg/m
        total_weight = self.cut_length * unit_weight * self.number_of_bars
        return unit_weight, total_weight

    def to_dict(self) -> dict:
        """
        Converts the bar object to a dictionary, useful for Pandas DataFrames and JSON serialization.
        """
        return {
            "bar_id": self.bar_id,
            "bar_mark": self.bar_mark,
            "shape_code": self.shape_code,
            "diameter": self.diameter, # Stored as string
            "lengths": self.lengths,
            "number_of_bars": self.number_of_bars,
            "cut_length": self.cut_length,
            "unit_weight": self.unit_weight,
            "total_weight": self.total_weight,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Bar':
        """
        Reconstructs a Bar object from a dictionary.
        """
        bar = cls(
            bar_mark=data["bar_mark"],
            shape_code=data["shape_code"],
            diameter=data["diameter"], # Loaded as string
            lengths=data["lengths"],
            number_of_bars=data["number_of_bars"],
        )
        bar.bar_id = data.get("bar_id", str(uuid.uuid4())) # Ensure bar_id is set, generate if missing
        # Recalculate cut_length and weights to ensure consistency, or load directly if trusted
        bar.cut_length = data.get("cut_length", bar.calculate_cut_length())
        bar.unit_weight = data.get("unit_weight", bar.calculate_weight()[0])
        bar.total_weight = data.get("total_weight", bar.calculate_weight()[1])
        return bar


class Element:
    """
    Represents a structural element containing multiple Bar objects.
    """
    def __init__(self, name: str):
        self.element_id = str(uuid.uuid4()) # Unique ID for each element
        self.name = name
        self.bars: list[Bar] = []

    def add_bar(self, bar: Bar):
        # Ensure the bar has a unique ID within this element
        existing_bar_ids = {b.bar_id for b in self.bars}
        while bar.bar_id in existing_bar_ids:
            bar.bar_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        self.bars.append(bar)

    def remove_bar(self, bar_id: str) -> bool:
        initial_len = len(self.bars)
        self.bars = [bar for bar in self.bars if bar.bar_id != bar_id]
        return len(self.bars) < initial_len

    def to_dict(self) -> dict:
        return {
            "element_id": self.element_id,
            "name": self.name,
            "bars": [bar.to_dict() for bar in self.bars]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Element':
        element = cls(name=data["name"])
        element.element_id = data.get("element_id", str(uuid.uuid4())) # Ensure element_id is set, generate if missing
        element.bars = [Bar.from_dict(bar_data) for bar_data in data.get("bars", [])]
        return element


class CategoryLower:
    """
    Represents a category containing multiple Element objects.
    """
    def __init__(self, name: str):
        self.category_lower_id = str(uuid.uuid4()) # Unique ID for each subcategory
        self.name = name
        self.elements: list[Element] = []

    def add_element(self, element: Element):
        # Ensure the element has a unique ID within this subcategory
        existing_element_ids = {e.element_id for e in self.elements}
        while element.element_id in existing_element_ids:
            element.element_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        self.elements.append(element)

    def remove_element(self, element_id: str) -> bool:
        initial_len = len(self.elements)
        self.elements = [e for e in self.elements if e.element_id != element_id]
        return len(self.elements) < initial_len

    def to_dict(self) -> dict:
        return {
            "type": "CategoryLower",
            "category_lower_id": self.category_lower_id,
            "name": self.name,
            "elements": [element.to_dict() for element in self.elements]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CategoryLower':
        category_lower = cls(name=data["name"])
        category_lower.category_lower_id = data.get("category_lower_id", str(uuid.uuid4())) # Ensure category_lower_id is set, generate if missing
        category_lower.elements = [Element.from_dict(element_data) for element_data in data.get("elements", [])]
        return category_lower


class CategoryHigher:
    """
    Represents a category containing multiple CategoryLower or CategoryHigher objects.
    """
    def __init__(self, name: str):
        self.category_higher_id = str(uuid.uuid4()) # Unique ID for each category
        self.name = name
        self.children: list[Union['CategoryLower', 'CategoryHigher']] = []

    def add_child(self, child: Union['CategoryLower', 'CategoryHigher']):
        # Ensure the child has a unique ID within this category
        existing_child_ids = {c.category_lower_id if isinstance(c, CategoryLower) else c.category_higher_id for c in self.children}
        if isinstance(child, CategoryLower):
            while child.category_lower_id in existing_child_ids:
                child.category_lower_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        elif isinstance(child, CategoryHigher):
            while child.category_higher_id in existing_child_ids:
                child.category_higher_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        self.children.append(child)

    def remove_child(self, child_id: str) -> bool:
        initial_len = len(self.children)
        self.children = [c for c in self.children if (isinstance(c, CategoryLower) and c.category_lower_id != child_id) or (isinstance(c, CategoryHigher) and c.category_higher_id != child_id)]
        return len(self.children) < initial_len

    def to_dict(self) -> dict:
        return {
            "type": "CategoryHigher",
            "category_higher_id": self.category_higher_id,
            "name": self.name,
            "children": [child.to_dict() for child in self.children]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CategoryHigher':
        category_higher = cls(name=data["name"])
        category_higher.category_higher_id = data.get("category_higher_id", str(uuid.uuid4())) # Ensure category_higher_id is set, generate if missing
        children_data = data.get("children", [])
        for child_data in children_data:
            if child_data["type"] == "CategoryLower":
                category_higher.children.append(CategoryLower.from_dict(child_data))
            elif child_data["type"] == "CategoryHigher":
                category_higher.children.append(CategoryHigher.from_dict(child_data))
        return category_higher


class Project:
    """
    Represents a project containing multiple CategoryHigher or CategoryLower objects.
    """
    def __init__(self, name: str):
        self.project_id = str(uuid.uuid4()) # Unique ID for each project
        self.name = name
        self.categories: list[Union['CategoryLower', 'CategoryHigher']] = []

    def add_category(self, category: Union['CategoryLower', 'CategoryHigher']):
        # Ensure the category has a unique ID within this project
        existing_category_ids = {c.category_lower_id if isinstance(c, CategoryLower) else c.category_higher_id for c in self.categories}
        if isinstance(category, CategoryLower):
            while category.category_lower_id in existing_category_ids:
                category.category_lower_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        elif isinstance(category, CategoryHigher):
            while category.category_higher_id in existing_category_ids:
                category.category_higher_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        self.categories.append(category)

    def remove_category(self, category_id: str) -> bool:
        initial_len = len(self.categories)
        self.categories = [c for c in self.categories if (isinstance(c, CategoryLower) and c.category_lower_id != category_id) or (isinstance(c, CategoryHigher) and c.category_higher_id != category_id)]
        return len(self.categories) < initial_len

    def to_dict(self) -> dict:
        return {
            "project_id": self.project_id,
            "name": self.name,
            "categories": [category.to_dict() for category in self.categories]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Project':
        project = cls(name=data["name"])
        project.project_id = data.get("project_id", str(uuid.uuid4())) # Ensure project_id is set, generate if missing
        categories_data = data.get("categories", [])
        for category_data in categories_data:
            if category_data["type"] == "CategoryLower":
                project.categories.append(CategoryLower.from_dict(category_data))
            elif category_data["type"] == "CategoryHigher":
                project.categories.append(CategoryHigher.from_dict(category_data))
        return project