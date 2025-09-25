import pytest
from src.logic.data_models import Project, CategoryHigher, CategoryLower, Element, Bar

class TestProject:
    def test_project_initialization(self):
        project = Project(name="Test Project")
        assert project.name == "Test Project"
        assert project.categories == []
        assert isinstance(project.id, str)

    def test_add_category(self):
        project = Project(name="Test Project")
        category_higher = CategoryHigher(name="Test Category Higher")
        project.add_category(category_higher)
        assert len(project.categories) == 1
        assert project.categories[0] == category_higher

    def test_remove_category(self):
        project = Project(name="Test Project")
        category1 = CategoryHigher(name="Category 1")
        category2 = CategoryHigher(name="Category 2")
        project.add_category(category1)
        project.add_category(category2)
        project.remove_category(category1.id)
        assert len(project.categories) == 1
        assert project.categories[0] == category2

    def test_remove_non_existent_category(self):
        project = Project(name="Test Project")
        category = CategoryHigher(name="Category")
        project.add_category(category)
        project.remove_category("non_existent_id")
        assert len(project.categories) == 1

    def test_to_dict(self):
        project = Project(name="Test Project")
        category_higher = CategoryHigher(name="Test Category Higher")
        category_lower = CategoryLower(name="Test Category Lower")
        element = Element(name="Test Element")
        bar = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        element.add_bar(bar)
        category_lower.add_element(element)
        category_higher.add_child(category_lower)
        project.add_category(category_higher)

        expected_dict = {
            "id": project.id,
            "name": "Test Project",
            "categories": [
                category_higher.to_dict()
            ]
        }
        assert project.to_dict() == expected_dict

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
        category_lower_dict = {
            "type": "CategoryLower",
            "id": "CL1",
            "name": "Test Category Lower",
            "elements": [element_dict]
        }
        category_higher_dict = {
            "type": "CategoryHigher",
            "id": "CH1",
            "name": "Test Category Higher",
            "children": [category_lower_dict]
        }
        project_dict = {
            "type": "Project",
            "id": "P1",
            "name": "Test Project",
            "categories": [category_higher_dict]
        }

        project = Project.from_dict(project_dict)
        assert project.id == "P1"
        assert project.name == "Test Project"
        assert len(project.categories) == 1
        assert isinstance(project.categories[0], CategoryHigher)
        assert project.categories[0].id == "CH1"
        assert isinstance(project.categories[0].children[0], CategoryLower)
        assert project.categories[0].children[0].id == "CL1"

    def test_from_dict_missing_name(self):
        project_dict = {
            "id": "P1",
            "categories": []
        }
        with pytest.raises(KeyError, match="'name'"):
            Project.from_dict(project_dict)