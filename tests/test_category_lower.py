import pytest
from src.logic.data_models import CategoryLower, Element, Bar

class TestCategoryLower:
    def test_category_lower_initialization(self):
        category = CategoryLower(name="Test Category Lower")
        assert category.name == "Test Category Lower"
        assert category.elements == []
        assert isinstance(category.id, str)

    def test_add_element(self):
        category = CategoryLower(name="Test Category Lower")
        element = Element(name="Test Element")
        category.add_element(element)
        assert len(category.elements) == 1
        assert category.elements[0] == element

    def test_remove_element(self):
        category = CategoryLower(name="Test Category Lower")
        element1 = Element(name="Test Element 1")
        element2 = Element(name="Test Element 2")
        category.add_element(element1)
        category.add_element(element2)
        category.remove_element(element1.element_id)
        assert len(category.elements) == 1
        assert category.elements[0] == element2

    def test_remove_non_existent_element(self):
        category = CategoryLower(name="Test Category Lower")
        element = Element(name="Test Element")
        category.add_element(element)
        category.remove_element("non_existent_id")
        assert len(category.elements) == 1

    def test_to_dict(self):
        category = CategoryLower(name="Test Category Lower")
        element = Element(name="Test Element")
        bar = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        element.add_bar(bar)
        category.add_element(element)
        expected_dict = {
            "type": "CategoryLower",
            "id": category.id,
            "name": "Test Category Lower",
            "elements": [element.to_dict()]
        }
        assert category.to_dict() == expected_dict

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
        category_dict = {
            "type": "CategoryLower",
            "id": "CL1",
            "name": "Test Category Lower",
            "elements": [element_dict]
        }
        category = CategoryLower.from_dict(category_dict)
        assert category.id == "CL1"
        assert category.name == "Test Category Lower"
        assert len(category.elements) == 1
        assert category.elements[0].element_id == "E1"
        assert category.elements[0].bars[0].bar_id == "B1"

    def test_from_dict_missing_name(self):
        category_dict = {
            "id": "CL1",
            "elements": []
        }
        with pytest.raises(KeyError, match="'name'"):
            CategoryLower.from_dict(category_dict)