import pytest
from src.logic.data_models import Element, Bar

class TestElement:
    def test_element_initialization(self):
        element = Element(name="Test Element")
        assert element.name == "Test Element"
        assert element.bars == []
        assert isinstance(element.element_id, str)

    def test_add_bar(self):
        element = Element(name="Test Element")
        bar = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        element.add_bar(bar)
        assert len(element.bars) == 1
        assert element.bars[0] == bar

    def test_remove_bar(self):
        element = Element(name="Test Element")
        bar1 = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        bar2 = Bar(bar_mark=2, shape_code="00", diameter="12", lengths={"A": 1200}, number_of_bars=3)
        element.add_bar(bar1)
        element.add_bar(bar2)
        element.remove_bar(bar1.bar_id)
        assert len(element.bars) == 1
        assert element.bars[0] == bar2

    def test_remove_non_existent_bar(self):
        element = Element(name="Test Element")
        bar = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        element.add_bar(bar)
        element.remove_bar("non_existent_id")
        assert len(element.bars) == 1

    def test_to_dict(self):
        element = Element(name="Test Element")
        bar = Bar(bar_mark=1, shape_code="00", diameter="10", lengths={"A": 1000}, number_of_bars=5)
        element.add_bar(bar)
        expected_dict = {
            "element_id": element.element_id,
            "name": "Test Element",
            "bars": [bar.to_dict()]
        }
        assert element.to_dict() == expected_dict

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
        element = Element.from_dict(element_dict)
        assert element.element_id == "E1"
        assert element.name == "Test Element"
        assert len(element.bars) == 1
        assert element.bars[0].bar_id == "B1"

    def test_from_dict_missing_name(self):
        element_dict = {
            "element_id": "E1",
            "bars": []
        }
        with pytest.raises(ValueError, match="Element name is required."):
            Element.from_dict(element_dict)