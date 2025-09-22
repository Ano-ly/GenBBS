import pytest
from src.logic.cut_length_calculator import (
    calculate_cut_length_shape_00,
    calculate_cut_length_shape_01,
    calculate_cut_length_shape_11,
    calculate_cut_length_shape_12,
    calculate_cut_length_shape_13,
    calculate_cut_length_shape_14,
    calculate_cut_length_shape_15,
    calculate_cut_length_shape_21,
    calculate_cut_length_shape_22,
    calculate_cut_length_shape_23,
    calculate_cut_length_shape_24,
    calculate_cut_length_shape_25,
    calculate_cut_length_shape_26,
    calculate_cut_length_shape_27,
    calculate_cut_length_shape_28,
    calculate_cut_length_shape_29,
    calculate_cut_length_shape_31,
    calculate_cut_length_shape_32,
    calculate_cut_length_shape_33,
    calculate_cut_length_shape_34,
    calculate_cut_length_shape_35,
    calculate_cut_length_shape_36,
    calculate_cut_length_shape_41,
    calculate_cut_length_shape_44,
    calculate_cut_length_shape_46,
    calculate_cut_length_shape_47,
    calculate_cut_length_shape_48,
    calculate_cut_length_shape_51,
    calculate_cut_length_shape_52,
    calculate_cut_length_shape_56,
    calculate_cut_length_shape_63,
    calculate_cut_length_shape_64,
    calculate_cut_length_shape_67,
    calculate_cut_length_shape_75,
    calculate_cut_length_shape_77,
    calculate_cut_length_shape_98,
    calculate_cut_length_shape_99
)

class TestCutLengthCalculator:
    def test_calculate_cut_length_shape_00(self):
        lengths = {"A": 1000}
        diameter = 10
        bend_radius = 0
        expected_cut_length = 1.0
        assert calculate_cut_length_shape_00(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_01(self):
        lengths = {"A": 1000}
        diameter = 10
        bend_radius = 0
        expected_cut_length = 1.0
        assert calculate_cut_length_shape_01(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_11(self):
        lengths = {"A": 500, "B": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 - (0.5 * 20) - 10) / 1000.0 # 980 / 1000 = 0.98
        assert calculate_cut_length_shape_11(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_12(self):
        lengths = {"A": 500, "B": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 - (0.43 * 20) - (1.2 * 10)) / 1000.0 # (1000 - 8.6 - 12) / 1000 = 979.4 / 1000 = 0.9794
        assert calculate_cut_length_shape_12(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_13(self):
        lengths = {"A": 500, "B": 100, "C": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + (0.57 * 100) + 500 - (1.6 * 10)) / 1000.0 # (1000 + 57 - 16) / 1000 = 1041 / 1000 = 1.041
        assert calculate_cut_length_shape_13(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_14(self):
        lengths = {"A": 500, "C": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + 500) / 1000.0
        assert calculate_cut_length_shape_14(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_15(self):
        lengths = {"A": 500, "C": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + 500) / 1000.0
        assert calculate_cut_length_shape_15(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_21(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 - 20 - (2 * 10)) / 1000.0 # (1500 - 20 - 20) / 1000 = 1460 / 1000 = 1.46
        assert calculate_cut_length_shape_21(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_22(self):
        lengths = {"A": 500, "B": 500, "C": 100, "D": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + (0.57 * 100) + 500 - (0.5 * 20) - (2.6 * 10)) / 1000.0 # (1500 + 57 - 10 - 26) / 1000 = 1521 / 1000 = 1.521
        assert calculate_cut_length_shape_22(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_23(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 - 20 - (2 * 10)) / 1000.0 # (1500 - 20 - 20) / 1000 = 1460 / 1000 = 1.46
        assert calculate_cut_length_shape_23(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_24(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + 500 + 500) / 1000.0
        assert calculate_cut_length_shape_24(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_25(self):
        lengths = {"A": 500, "B": 500, "E": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + 500 + 500) / 1000.0
        assert calculate_cut_length_shape_25(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_26(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + 500 + 500) / 1000.0
        assert calculate_cut_length_shape_26(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_27(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 - (0.5 * 20) - 10) / 1000.0 # (1500 - 10 - 10) / 1000 = 1480 / 1000 = 1.48
        assert calculate_cut_length_shape_27(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_28(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 - (0.5 * 20) - 10) / 1000.0 # (1500 - 10 - 10) / 1000 = 1480 / 1000 = 1.48
        assert calculate_cut_length_shape_28(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_29(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + 500 + 500) / 1000.0
        assert calculate_cut_length_shape_29(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_31(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 - (1.5 * 20) - (3 * 10)) / 1000.0 # (2000 - 30 - 30) / 1000 = 1940 / 1000 = 1.94
        assert calculate_cut_length_shape_31(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_32(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 - (1.5 * 20) - (3 * 10)) / 1000.0 # (2000 - 30 - 30) / 1000 = 1940 / 1000 = 1.94
        assert calculate_cut_length_shape_32(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_33(self):
        lengths = {"A": 200, "B": 100, "C": 200}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (2 * 200 + 1.7 * 100 + 2 * 200 - (4 * 10)) / 1000.0 # (400 + 170 + 400 - 40) / 1000 = 930 / 1000 = 0.93
        assert calculate_cut_length_shape_33(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_34(self):
        lengths = {"A": 500, "B": 500, "C": 500, "E": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 - (0.5 * 20) - 10) / 1000.0 # (2000 - 10 - 10) / 1000 = 1980 / 1000 = 1.98
        assert calculate_cut_length_shape_34(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_35(self):
        lengths = {"A": 500, "B": 500, "C": 500, "E": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 - (0.5 * 20) - 10) / 1000.0 # (2000 - 10 - 10) / 1000 = 1980 / 1000 = 1.98
        assert calculate_cut_length_shape_35(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_36(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 - 20 - (2 * 10)) / 1000.0 # (2000 - 20 - 20) / 1000 = 1960 / 1000 = 1.96
        assert calculate_cut_length_shape_36(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_41(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 500, "E": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 + 500 - (2 * 20) - (4 * 10)) / 1000.0 # (2500 - 40 - 40) / 1000 = 2420 / 1000 = 2.42
        assert calculate_cut_length_shape_41(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_44(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 500, "E": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 + 500 - (2 * 20) - (4 * 10)) / 1000.0 # (2500 - 40 - 40) / 1000 = 2420 / 1000 = 2.42
        assert calculate_cut_length_shape_44(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_46(self):
        lengths = {"A": 500, "B": 100, "C": 500, "E": 500}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (500 + (2 * 100) + 500 + 500) / 1000.0 # (500 + 200 + 500 + 500) / 1000 = 1700 / 1000 = 1.7
        assert calculate_cut_length_shape_46(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_47(self):
        lengths = {"A": 500, "B": 100, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = ((2 * 500) + 100 + (2 * 500) + (3 * 20) - (6 * 10)) / 1000.0 # (1000 + 100 + 1000 + 60 - 60) / 1000 = 2100 / 1000 = 2.1
        assert calculate_cut_length_shape_47(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_48(self):
        lengths = {"A": 500, "B": 100, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = ((2 * 500) + 100 + (2 * 500) - 20 - (2 * 10)) / 1000.0 # (1000 + 100 + 1000 - 20 - 20) / 1000 = 2060 / 1000 = 2.06
        assert calculate_cut_length_shape_48(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_51(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = ((2 * (500 + 500 + 500)) - (2.5 * 20) - (5 * 10)) / 1000.0 # (3000 - 50 - 50) / 1000 = 2900 / 1000 = 2.9
        assert calculate_cut_length_shape_51(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_52(self):
        lengths = {"A": 500, "B": 500, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = ((2 * (500 + 500)) + (2 * 500) - (1.5 * 20) - (3 * 10)) / 1000.0 # (2000 + 1000 - 30 - 30) / 1000 = 2940 / 1000 = 2.94
        assert calculate_cut_length_shape_52(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_56(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 500, "E": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + 500 + (2 * 500) - (1.5 * 20) - (3 * 10)) / 1000.0 # (2000 + 1000 - 30 - 30) / 1000 = 2940 / 1000 = 2.94
        assert calculate_cut_length_shape_56(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_63(self):
        lengths = {"A": 500, "B": 100, "C": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = ((2 * 500) + (3 * 100) + (2 * 500) - (3 * 20) - (6 * 10)) / 1000.0 # (1000 + 300 + 1000 - 60 - 60) / 1000 = 2180 / 1000 = 2.18
        assert calculate_cut_length_shape_63(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_64(self):
        lengths = {"A": 500, "B": 500, "C": 500, "D": 100, "E": 500, "F": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + 500 + 500 + (2 * 100) + 500 + 500 - (3 * 20) - (6 * 10)) / 1000.0 # (2500 + 200 - 60 - 60) / 1000 = 2580 / 1000 = 2.58
        assert calculate_cut_length_shape_64(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_67(self):
        lengths = {"A": 1000}
        diameter = 10
        bend_radius = 0
        expected_cut_length = 1.0
        assert calculate_cut_length_shape_67(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_75(self):
        import math
        lengths = {"A": 100, "B": 50}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (math.pi * (100 - 10) + 50 + 25) / 1000.0 # (math.pi * 90 + 75) / 1000 = (282.74 + 75) / 1000 = 357.74 / 1000 = 0.35774
        assert calculate_cut_length_shape_75(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_77_case1(self):
        import math
        lengths = {"A": 100, "B": 10, "C": 2}
        diameter = 10
        bend_radius = 0
        # B (10) is not greater than A/5 (100/5 = 20), so use first formula
        expected_cut_length = (2 * math.pi * (100 - 10)) / 1000.0 # (2 * math.pi * 90) / 1000 = 565.48 / 1000 = 0.56548
        assert calculate_cut_length_shape_77(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_77_case2(self):
        import math
        lengths = {"A": 100, "B": 30, "C": 2}
        diameter = 10
        bend_radius = 0
        # B (30) is greater than A/5 (100/5 = 20), so use second formula
        expected_cut_length = (2 * math.sqrt((math.pi * (100 - 10))**2 + 30**2)) / 1000.0 # (2 * sqrt((math.pi * 90)**2 + 900)) / 1000 = (2 * sqrt(282.74**2 + 900)) / 1000 = (2 * sqrt(79942.5 + 900)) / 1000 = (2 * sqrt(80842.5)) / 1000 = (2 * 284.32) / 1000 = 568.64 / 1000 = 0.56864
        assert calculate_cut_length_shape_77(lengths, diameter, bend_radius) == pytest.approx(expected_cut_length)

    def test_calculate_cut_length_shape_98(self):
        lengths = {"A": 500, "B": 100, "C": 500, "D": 500}
        diameter = 10
        bend_radius = 20
        expected_cut_length = (500 + (2 * 100) + 500 + 500 - (2 * 20) - (4 * 10)) / 1000.0 # (500 + 200 + 500 + 500 - 40 - 40) / 1000 = 1620 / 1000 = 1.62
        assert calculate_cut_length_shape_98(lengths, diameter, bend_radius) == expected_cut_length

    def test_calculate_cut_length_shape_99(self):
        lengths = {"A": 100, "B": 200, "C": 300}
        diameter = 10
        bend_radius = 0
        expected_cut_length = (100 + 200 + 300) / 1000.0 # 600 / 1000 = 0.6
        assert calculate_cut_length_shape_99(lengths, diameter, bend_radius) == expected_cut_length