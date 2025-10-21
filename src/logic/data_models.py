import uuid
from datetime import datetime
import math
from src.logic.cut_length_calculator import CUT_LENGTH_FORMULAS
from src.config.config import MIN_BEND_RADII
from typing import Union

class Bar:   
    """
    This class will hold all the details for a single bar mark.
    """
    def __init__(self, bar_mark: int, shape_code: str, diameter: str, lengths: dict, number_of_bars: int, parent_tree: list[dict] = None):
        self.bar_id = str(uuid.uuid4()) # Unique ID for each bar
        self.bar_mark = bar_mark
        self.shape_code = shape_code
        self.diameter = diameter # Now a string, e.g., 'Y10'
        self.lengths = lengths
        self.number_of_bars = number_of_bars
        self.cut_length = self.calculate_cut_length()
        self.unit_weight, self.total_weight = self.calculate_weight()
        self.parent_tree = parent_tree if parent_tree is not None else []
    def recalculate_properties(self):
        self.cut_length = self.calculate_cut_length()
        self.unit_weight, self.total_weight = self.calculate_weight()
    def _get_bend_radius(self) -> float:
        """
        Determines the bend radius based on the bar's diameter and assumed steel type,
        using MIN_BEND_RADII from config.py. If the diameter is not found, it falls back
        to a default calculation (e.g., 4 times the diameter for smaller bars, 5 or 6 for larger).
        """
        numeric_diameter = float(''.join(filter(str.isdigit, self.diameter)))
        
        # Look up bend radius in the predefined dictionary
        bend_radius = MIN_BEND_RADII.get(numeric_diameter)
        
        if bend_radius is None:
            # Fallback calculation if diameter not found in MIN_BEND_RADII
            # These factors are illustrative and should be verified against BS 8660:2020
            if numeric_diameter <= 16:
                bend_radius = 2 * numeric_diameter
            else:
                bend_radius = 3.5 * numeric_diameter

            print(f"Warning: Minimum bend radius for diameter {numeric_diameter}mm not found in config. Using calculated value: {bend_radius}mm.")
            
        return bend_radius

    def calculate_cut_length(self) -> float:
        """
        Calculates the cut length of the bar based on its shape code and BS 8660:2020 formulas.
        Dispatches to the appropriate function from CUT_LENGTH_FORMULAS.
        """
        calculator_func = CUT_LENGTH_FORMULAS.get(self.shape_code)
        if calculator_func:
            bend_radius = self._get_bend_radius()
            print(bend_radius)
            print(float(''.join(filter(str.isdigit, self.diameter))))
            raw = calculator_func(self.lengths, float(''.join(filter(str.isdigit, self.diameter))), bend_radius) * 1000
            return math.ceil(raw / 10) * 10
        else:
            # Fallback for unknown shape codes, or raise an error
            print(f"Warning: No cut length formula found for shape code {self.shape_code}. Summing lengths.")
            raw = sum(self.lengths.values())
            return math.ceil(raw / 10) * 10

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
        total_weight = (self.cut_length/1000) * unit_weight * self.number_of_bars
        return unit_weight, total_weight

    def to_dict(self) -> dict:
        """
        Converts the bar object to a dictionary, useful for Pandas DataFrames and JSON serialization.
        """
        return {
            "bar_id": self.bar_id,
            "bar_mark": self.bar_mark,
            "diameter": self.diameter, # Stored as string
            "number_of_bars": self.number_of_bars,
            "cut_length": self.cut_length,
            "unit_weight": self.unit_weight,
            "total_weight": self.total_weight,
            "shape_code": self.shape_code,
            "lengths": self.lengths, 
            "parent_tree": self.parent_tree,
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
            parent_tree=data.get("parent_tree", [])
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
    def __init__(self, name: str, quantity: int = 1, parent_tree: list[dict] = None):
        self.id = str(uuid.uuid4()) # Unique ID for each element
        self._name = name
        self.quantity = quantity
        self.bars: list[Bar] = []
        self.parent_tree = parent_tree if parent_tree is not None else []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name != new_name:
            self._name = new_name
            self._update_child_parent_trees()
    def _sync_parent_tree_names(self, child_parent_tree: list[dict]) -> list[dict]:
        """
        Ensures that every entry in child_parent_tree (except the one belonging to this CategoryLower)
        matches the corresponding entry in self.parent_tree by both id and type.
        If the name differs, it updates the child's entry to match self.parent_tree.
        """
        # Build a lookup for self.parent_tree: (id, type) -> name
        own_lookup = {(entry.get('id'), entry.get('type')): entry.get('name')
                      for entry in self.parent_tree}

        for entry in child_parent_tree:
            key = (entry.get('id'), entry.get('type'))
            if key in own_lookup and entry.get('name') != own_lookup[key]:
                entry['name'] = own_lookup[key]
        return (child_parent_tree)

    def _update_child_parent_trees(self):
        for bar in self.bars:
            for parent_info in bar.parent_tree:
                if parent_info.get('id') == self.id and parent_info.get('type') == 'Element':
                    parent_info['name'] = self._name

    def _update_other_child_parent_trees(self):
        for bar in self.bars:
            bar.parent_tree = self._sync_parent_tree_names(bar.parent_tree)

    def add_bar(self, bar: Bar):
        # Ensure the bar has a unique ID within this element
        existing_bar_ids = {b.bar_id for b in self.bars}
        while bar.bar_id in existing_bar_ids:
            bar.bar_id = str(uuid.uuid4()) # Generate a new ID until it's unique
        
        # Set the parent_tree for the bar
        bar.parent_tree = self.parent_tree + [{'id': self.id, 'name': self.name, 'type': 'Element'}]
        self.bars.append(bar)

    def remove_bar(self, bar_id: str) -> bool:
        initial_len = len(self.bars)
        self.bars = [bar for bar in self.bars if bar.bar_id != bar_id]
        return len(self.bars) < initial_len

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "bars": [bar.to_dict() for bar in self.bars],
            "parent_tree": self.parent_tree,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Element':
        if "name" not in data:
            raise ValueError("Element name is required.")
        element = cls(name=data["name"], quantity=data.get("quantity", 1), parent_tree=data.get("parent_tree", []))
        element.id = data.get("id", str(uuid.uuid4()))
        element.bars = [Bar.from_dict(bar_data) for bar_data in data.get("bars", [])]
        return element
    
    def get_children(self) -> list[Bar]:
        return self.bars

    def sort_bars(self):
        """
        Sorts the bars in ascending order of bar_mark.
        If any bar's shape code is in [51, 52, 56, 63, 64, 75] and bar_mark is 1,
        that bar is placed first in the list.
        """
        priority_shape_codes = {51, 52, 56, 63, 64, 75}
        priority_bars = []
        other_bars = []

        for bar in self.bars:
            if bar.bar_mark == 1 and int(bar.shape_code) in priority_shape_codes:
                priority_bars.append(bar)
            else:
                other_bars.append(bar)

        other_bars.sort(key=lambda bar: bar.bar_mark)
        self.bars = priority_bars + other_bars


class CategoryLower:
    """
    Represents a category containing multiple Element objects.
    """
    def __init__(self, name: str, parent_tree: list[dict] = None):
        self.id = str(uuid.uuid4()) # Unique ID for each subcategory
        self._name = name
        self.elements: list[Element] = []
        self.parent_tree = parent_tree if parent_tree is not None else []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name != new_name:
            self._name = new_name
            self._update_child_parent_trees()

    def _sync_parent_tree_names(self, child_parent_tree: list[dict]) -> list[dict]:
        """
        Ensures that every entry in child_parent_tree (except the one belonging to this CategoryLower)
        matches the corresponding entry in self.parent_tree by both id and type.
        If the name differs, it updates the child's entry to match self.parent_tree.
        """
        # Build a lookup for self.parent_tree: (id, type) -> name
        own_lookup = {(entry.get('id'), entry.get('type')): entry.get('name')
                      for entry in self.parent_tree}

        for entry in child_parent_tree:
            key = (entry.get('id'), entry.get('type'))
            if key in own_lookup and entry.get('name') != own_lookup[key]:
                entry['name'] = own_lookup[key]
        return (child_parent_tree)

    def _update_child_parent_trees(self):
        for element in self.elements:
            for parent_info in element.parent_tree:
                if parent_info.get('id') == self.id and parent_info.get('type') == 'CategoryLower':
                    parent_info['name'] = self._name
            element._update_other_child_parent_trees()

    def _update_other_child_parent_trees(self):
        for element in self.elements:
            element.parent_tree = self._sync_parent_tree_names(element.parent_tree)
            element._update_other_child_parent_trees()
    def add_element(self, element: Element):
        # Ensure the element has a unique ID within this subcategory
        existing_ids = {e.id for e in self.elements}
        while element.id in existing_ids:
            element.id = str(uuid.uuid4()) # Generate a new ID until it's unique
        
        # Set the parent_tree for the element
        element.parent_tree = self.parent_tree + [{'id': self.id, 'name': self.name, 'type': 'CategoryLower'}]
        self.elements.append(element)

    def remove_element(self, id: str) -> bool:
        initial_len = len(self.elements)
        self.elements = [e for e in self.elements if e.id != id]
        return len(self.elements) < initial_len

    def to_dict(self) -> dict:
        return {
            "type": "CategoryLower",
            "id": self.id,
            "name": self.name,
            "elements": [element.to_dict() for element in self.elements],
            "parent_tree": self.parent_tree,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CategoryLower':
        category_lower = cls(name=data["name"], parent_tree=data.get("parent_tree", []))
        category_lower.id = data.get("id", str(uuid.uuid4())) # Ensure id is set, generate if missing
        category_lower.elements = [Element.from_dict(element_data) for element_data in data.get("elements", [])]
        return category_lower
    
    def get_children(self) -> list[Element]:
        return self.elements


class CategoryHigher:
    """
    Represents a category containing multiple CategoryLower or CategoryHigher objects.
    """
    def __init__(self, name: str, parent_tree: list[dict] = None):
        self.id = str(uuid.uuid4()) # Unique ID for each category
        self._name = name
        self.children: list[Union['CategoryLower', 'CategoryHigher']] = []
        self.parent_tree = parent_tree if parent_tree is not None else []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name != new_name:
            self._name = new_name
            self._update_child_parent_trees()
    def _sync_parent_tree_names(self, child_parent_tree: list[dict]) -> list[dict]:
        """
        Ensures that every entry in child_parent_tree (except the one belonging to this CategoryLower)
        matches the corresponding entry in self.parent_tree by both id and type.
        If the name differs, it updates the child's entry to match self.parent_tree.
        """
        # Build a lookup for self.parent_tree: (id, type) -> name
        own_lookup = {(entry.get('id'), entry.get('type')): entry.get('name')
                      for entry in self.parent_tree}

        for entry in child_parent_tree:
            key = (entry.get('id'), entry.get('type'))
            if key in own_lookup and entry.get('name') != own_lookup[key]:
                entry['name'] = own_lookup[key]
        return (child_parent_tree)

    def _update_child_parent_trees(self):
        for child in self.children:
            for parent_info in child.parent_tree:
                if parent_info.get('id') == self.id and parent_info.get('type') == 'CategoryHigher':
                    parent_info['name'] = self._name
            child._update_other_child_parent_trees()

    def _update_other_child_parent_trees(self):
        for child in self.children:
            child.parent_tree = self._sync_parent_tree_names(child.parent_tree)
            child._update_other_child_parent_trees()

    def add_child(self, child: Union['CategoryLower', 'CategoryHigher']):
        # Ensure the child has a unique ID within this category
        existing_child_ids = {c.id if isinstance(c, CategoryLower) else c.id for c in self.children}
        if isinstance(child, CategoryLower):
            while child.id in existing_child_ids:
                child.id = str(uuid.uuid4()) # Generate a new ID until it's unique
            child.parent_tree = self.parent_tree + [{'id': self.id, 'name': self.name, 'type': 'CategoryHigher'}]
        elif isinstance(child, CategoryHigher):
            while child.id in existing_child_ids:
                child.id = str(uuid.uuid4()) # Generate a new ID until it's unique
            child.parent_tree = self.parent_tree + [{'id': self.id, 'name': self.name, 'type': 'CategoryHigher'}]
        self.children.append(child)

    def remove_child(self, child_id: str) -> bool:
        initial_len = len(self.children)
        self.children = [c for c in self.children if (isinstance(c, CategoryLower) and c.id != child_id) or (isinstance(c, CategoryHigher) and c.id != child_id)]
        return len(self.children) < initial_len

    def to_dict(self) -> dict:
        return {
            "type": "CategoryHigher",
            "id": self.id,
            "name": self.name,
            "children": [child.to_dict() for child in self.children],
            "parent_tree": self.parent_tree,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CategoryHigher':
        category_higher = cls(name=data["name"], parent_tree=data.get("parent_tree", []))
        category_higher.id = data.get("id", str(uuid.uuid4())) # Ensure id is set, generate if missing
        children_data = data.get("children", [])
        for child_data in children_data:
            if child_data["type"] == "CategoryLower":
                category_higher.children.append(CategoryLower.from_dict(child_data))
            elif child_data["type"] == "CategoryHigher":
                category_higher.children.append(CategoryHigher.from_dict(child_data))
        return category_higher

    def get_children(self) -> list[Union['CategoryLower', 'CategoryHigher']]:
        return self.children

class Project:
    """
    Represents a project containing multiple CategoryHigher or CategoryLower objects.
    """
    def __init__(self, name: str):
        self.id = str(uuid.uuid4()) # Unique ID for each project
        self._name = name
        self.categories: list[Union['CategoryLower', 'CategoryHigher']] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name != new_name:
            self._name = new_name
            self._update_child_parent_trees()
    def _sync_parent_tree_names(self, child_parent_tree: list[dict]) -> list[dict]:
        """
        Ensures that every entry in child_parent_tree (except the one belonging to this CategoryLower)
        matches the corresponding entry in self.parent_tree by both id and type.
        If the name differs, it updates the child's entry to match self.parent_tree.
        """
        # Build a lookup for self.parent_tree: (id, type) -> name
        own_lookup = {(entry.get('id'), entry.get('type')): entry.get('name')
                      for entry in self.parent_tree}

        for entry in child_parent_tree:
            key = (entry.get('id'), entry.get('type'))
            if key in own_lookup and entry.get('name') != own_lookup[key]:
                entry['name'] = own_lookup[key]
        return (child_parent_tree)

    def _update_child_parent_trees(self):
        for category in self.categories:
            for parent_info in category.parent_tree:
                if parent_info.get('id') == self.id and parent_info.get('type') == 'Project':
                    parent_info['name'] = self._name
            category._update_other_child_parent_trees()

    def _update_other_child_parent_trees(self):
        for category in self.categories:
            category.parent_tree = self._sync_parent_tree_names(category.parent_tree)
            category._update_other_child_parent_trees()

    def add_category(self, category: Union['CategoryLower', 'CategoryHigher']):
        # Ensure the category has a unique ID within this project
        existing_category_ids = {c.id if isinstance(c, CategoryLower) else c.id for c in self.categories}
        if isinstance(category, CategoryLower):
            while category.id in existing_category_ids:
                category.id = str(uuid.uuid4()) # Generate a new ID until it's unique
            category.parent_tree = [{'id': self.id, 'name': self.name, 'type': 'Project'}]
        elif isinstance(category, CategoryHigher):
            while category.id in existing_category_ids:
                category.id = str(uuid.uuid4()) # Generate a new ID until it's unique
            category.parent_tree = [{'id': self.id, 'name': self.name, 'type': 'Project'}]
        self.categories.append(category)

    def remove_category(self, category_id: str) -> bool:
        initial_len = len(self.categories)
        self.categories = [c for c in self.categories if (isinstance(c, CategoryLower) and c.id != category_id) or (isinstance(c, CategoryHigher) and c.id != category_id)]
        return len(self.categories) < initial_len

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "categories": [category.to_dict() for category in self.categories]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Project':
        project = cls(name=data["name"])
        project.id = data.get("id", str(uuid.uuid4())) # Ensure id is set, generate if missing
        categories_data = data.get("categories", [])
        for category_data in categories_data:
            if category_data["type"] == "CategoryLower":
                project.categories.append(CategoryLower.from_dict(category_data))
            elif category_data["type"] == "CategoryHigher":
                project.categories.append(CategoryHigher.from_dict(category_data))
        return project

    def get_children(self) -> list[Union['CategoryLower', 'CategoryHigher']]:
        return self.categories