import pytest
from src.logic.data_models import Bar
from src.config import MIN_BEND_RADII

# Test cases for _get_bend_radius method
@pytest.mark.parametrize(
    "diameter_str, expected_bend_radius",
    [
        ("Y6", MIN_BEND_RADII[6]),
        ("Y10", MIN_BEND_RADII[10]),
        ("Y20", MIN_BEND_RADII[20]),
        ("Y50", MIN_BEND_RADII[50]),
        ("Y7", 2 * 7), # Fallback for diameter not in MIN_BEND_RADII (<=16mm)
        ("Y18", 3.5 * 18), # Fallback for diameter not in MIN_BEND_RADII (16mm < d <= 25mm)
        ("Y30", 3.5 * 30), # Fallback for diameter not in MIN_BEND_RADII (>25mm)
    ],
)
def test_get_bend_radius(diameter_str, expected_bend_radius):
    bar = Bar(bar_mark=1, shape_code="00", diameter=diameter_str, lengths={"A": 1000}, number_of_bars=1)
    assert bar._get_bend_radius() == expected_bend_radius

# Test cases for calculate_cut_length method
@pytest.mark.parametrize(
    "shape_code, lengths, diameter_str, expected_cut_length",
    [
        # Shape 00: Straight bar, cut length is A
        ("00", {"A": 5000}, "Y10", 5.0), # 5000mm = 5m
        # Shape 01: Straight bar, cut length is A
        ("01", {"A": 2500}, "Y12", 2.5), # 2500mm = 2.5m
        # Shape 11: L-shape, A + B - 1R - 1D
        ("11", {"A": 1000, "B": 500}, "Y10", (1000 + 500 - (0.5 * MIN_BEND_RADII[10]) - 10) / 1000.0), # (A + B - R - D) / 1000
        # Shape 21: U-shape, A + B + C - R - 2D
        ("21", {"A": 500, "B": 1000, "C": 500}, "Y16", (500 + 1000 + 500 - MIN_BEND_RADII[16] - (2 * 16)) / 1000.0),
        # Shape 99: Unknown shape code, sums lengths
        ("99", {"A": 1000, "B": 2000, "C": 3000}, "Y10", (1000 + 2000 + 3000) / 1000.0),
    ],
)
def test_calculate_cut_length(shape_code, lengths, diameter_str, expected_cut_length):
    bar = Bar(bar_mark=1, shape_code=shape_code, diameter=diameter_str, lengths=lengths, number_of_bars=1)
    assert bar.cut_length == pytest.approx(expected_cut_length)

# Test cases for calculate_weight method
@pytest.mark.parametrize(
    "diameter_str, cut_length, number_of_bars, expected_unit_weight, expected_total_weight",
    [
        ("Y10", 1.0, 1, 0.6165, 0.6165), # 10mm bar, 1m length, 1 bar
        ("Y12", 2.5, 2, 0.8878, 4.439), # 12mm bar, 2.5m length, 2 bars
        ("Y16", 0.5, 10, 1.5783, 7.8915), # 16mm bar, 0.5m length, 10 bars
    ],
)
def test_calculate_weight(diameter_str, cut_length, number_of_bars, expected_unit_weight, expected_total_weight):
    bar = Bar(bar_mark=1, shape_code="00", diameter=diameter_str, lengths={"A": cut_length * 1000}, number_of_bars=number_of_bars)
    # Manually set cut_length for testing weight calculation independently
    bar.cut_length = cut_length
    unit_weight, total_weight = bar.calculate_weight()
    assert unit_weight == pytest.approx(expected_unit_weight, rel=1e-3)
    assert total_weight == pytest.approx(expected_total_weight, rel=1e-3)

# Test cases for to_dict and from_dict methods
def test_to_from_dict():
    original_bar = Bar(bar_mark=1, shape_code="21", diameter="Y16", lengths={"A": 500, "B": 1000, "C": 500}, number_of_bars=5)
    bar_dict = original_bar.to_dict()
    reconstructed_bar = Bar.from_dict(bar_dict)

    assert original_bar.bar_mark == reconstructed_bar.bar_mark
    assert original_bar.shape_code == reconstructed_bar.shape_code
    assert original_bar.diameter == reconstructed_bar.diameter
    assert original_bar.lengths == reconstructed_bar.lengths
    assert original_bar.number_of_bars == reconstructed_bar.number_of_bars
    assert original_bar.cut_length == pytest.approx(reconstructed_bar.cut_length)
    assert original_bar.unit_weight == pytest.approx(reconstructed_bar.unit_weight)
    assert original_bar.total_weight == pytest.approx(reconstructed_bar.total_weight)
    assert original_bar.bar_id == reconstructed_bar.bar_id

def test_from_dict_missing_id():
    bar_data = {
        "bar_mark": 2,
        "shape_code": "00",
        "diameter": "Y10",
        "lengths": {"A": 2000},
        "number_of_bars": 3,
    }
    reconstructed_bar = Bar.from_dict(bar_data)
    assert reconstructed_bar.bar_mark == 2
    assert reconstructed_bar.shape_code == "00"
    assert reconstructed_bar.diameter == "Y10"
    assert reconstructed_bar.lengths == {"A": 2000}
    assert reconstructed_bar.number_of_bars == 3
    assert reconstructed_bar.bar_id is not None