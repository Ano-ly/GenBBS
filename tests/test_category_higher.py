import pytest
from src.logic.data_models import CategoryHigher, CategoryLower, Element, Bar

class TestCategoryHigher:
    def test_category_higher_initialization(self):
        category = CategoryHigher(name="Test Category Higher")
        assert category.name == "Test Category Higher"
        assert category.children == []
        assert isinstance(category.id, str)

    def test_add_child_category_lower(self):
        parent_category = CategoryHigher(name="Parent Category")
        child_category_lower = CategoryLower(name="Child Lower")
        parent_category.add_child(child_category_lower)
        assert len(parent_category.children) == 1
        assert parent_category.children[0] == child_category_lower

    def test_add_child_category_higher(self):
        parent_category = CategoryHigher(name="Parent Category")
        child_category_higher = CategoryHigher(name="Child Higher")
        parent_category.add_child(child_category_higher)
        assert len(parent_category.children) == 1
        assert parent_category.children[0] == child_category_higher

    def test_remove_child(self):
        parent_category = CategoryHigher(name="Parent Category")
        child1 = CategoryLower(name="Child 1")
        child2 = CategoryHigher(name="Child 2")
        parent_category.add_child(child1)
        parent_category.add_child(child2)
        parent_category.remove_child(child1.id)
        assert len(parent_category.children) == 1
        assert parent_category.children[0] == child2

    def test_remove_non_existent_child(self):
        parent_category = CategoryHigher(name="Parent Category")
        child = CategoryLower(name="Child")
        parent_category.add_child(child)
        parent_category.remove_child("non_existent_id")
        assert len(parent_category.children) == 1

    def test_to_dict(self):
        parent_category = CategoryHigher(name="Parent Category")
        child_lower = CategoryLower(name="Child Lower")
        element = Element(name="Test Element")
        bar = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        element.add_bar(bar)
        child_lower.add_element(element)
        parent_category.add_child(child_lower)

        child_higher = CategoryHigher(name="Child Higher")
        parent_category.add_child(child_higher)

        expected_dict = {
            "type": "CategoryHigher",
            "id": parent_category.id,
            "name": "Parent Category",
            "children": [
                child_lower.to_dict(),
                child_higher.to_dict()
            ]
        }
        assert parent_category.to_dict() == expected_dict

    def test_from_dict(self):
        bar_dict = {
            "bar_id": "B1",
            "bar_mark": 1,
            "shape_code": "00",
            "diameter": "10",
            "lengths": {"A": 1000},
            "number_of_bars": 5,
            "cut_length": 1.0,
            "unit_weight": 0.6165,
            "total_weight": 3.0825
        }
        element_dict = {
            "element_id": "E1",
            "name": "Test Element",
            "bars": [bar_dict]
        }
        child_lower_dict = {
            "type": "CategoryLower",
            "id": "CL1",
            "name": "Child Lower",
            "elements": [element_dict]
        }
        child_higher_dict = {
            "type": "CategoryHigher",
            "id": "CH1",
            "name": "Child Higher",
            "children": []
        }
        parent_category_dict = {
            "type": "CategoryHigher",
            "id": "PCH1",
            "name": "Parent Category",
            "children": [child_lower_dict, child_higher_dict]
        }

        category = CategoryHigher.from_dict(parent_category_dict)
        assert category.id == "PCH1"
        assert category.name == "Parent Category"
        assert len(category.children) == 2
        assert isinstance(category.children[0], CategoryLower)
        assert category.children[0].id == "CL1"
        assert isinstance(category.children[1], CategoryHigher)
        assert category.children[1].id == "CH1"

    def test_from_dict_missing_name(self):
        category_dict = {
            "id": "CH1",
            "children": []
        }
        with pytest.raises(KeyError, match="'name'"):
            CategoryHigher.from_dict(category_dict)