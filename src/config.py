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

SHAPE_CODE_LENGTH_MAP = {
    "00": ["A"], # Stock lengths
    "01": ["A"], # Stock lengths
    "11": ["A", "B"],
    "12": ["A", "B"],
    "13": ["A", "B", "C"],
    "14": ["A", "C"],
    "15": ["A", "C"],
    "21": ["A", "B", "C"],
    "22": ["A", "B", "C", "D"],
    "23": ["A", "B", "C"],
    "24": ["A", "B", "C"],
    "25": ["A", "B", "E"],
    "26": ["A", "B", "C"],
    "27": ["A", "B", "C"],
    "28": ["A", "B", "C"],
    "29": ["A", "B", "C"],
    "31": ["A", "B", "C", "D"],
    "32": ["A", "B", "C", "D"],
    "33": ["A", "B", "C"],
    "34": ["A", "B", "C", "E"],
    "35": ["A", "B", "C", "E"],
    "36": ["A", "B", "C", "D"],
    "41": ["A", "B", "C", "D", "E"],
    "44": ["A", "B", "C", "D", "E"],
    "46": ["A", "B", "C", "E"],
    "47": ["A", "B", "C"],
    "48": ["A", "B", "C"],
    "51": ["A", "B", "C"],
    "52": ["A", "B", "C"],
    "56": ["A", "B", "C", "D", "E"],
    "63": ["A", "B", "C"],
    "64": ["A", "B", "C", "D", "E", "F"],
    "67": ["A"],
    "75": ["A", "B"],
    "77": ["A", "C"],
    "98": ["A", "B", "C", "D"],
    "99": [] # For all other shapes where standard shapes cannot be used, no specific lengths
}

CUT_LENGTH_FORMULAS = {
    "00": calculate_cut_length_shape_00,
    "01": calculate_cut_length_shape_01,
    "11": calculate_cut_length_shape_11,
    "12": calculate_cut_length_shape_12,
    "13": calculate_cut_length_shape_13,
    "14": calculate_cut_length_shape_14,
    "15": calculate_cut_length_shape_15,
    "21": calculate_cut_length_shape_21,
    "22": calculate_cut_length_shape_22,
    "23": calculate_cut_length_shape_23,
    "24": calculate_cut_length_shape_24,
    "25": calculate_cut_length_shape_25,
    "26": calculate_cut_length_shape_26,
    "27": calculate_cut_length_shape_27,
    "28": calculate_cut_length_shape_28,
    "29": calculate_cut_length_shape_29,
    "31": calculate_cut_length_shape_31,
    "32": calculate_cut_length_shape_32,
    "33": calculate_cut_length_shape_33,
    "34": calculate_cut_length_shape_34,
    "35": calculate_cut_length_shape_35,
    "36": calculate_cut_length_shape_36,
    "41": calculate_cut_length_shape_41,
    "44": calculate_cut_length_shape_44,
    "46": calculate_cut_length_shape_46,
    "47": calculate_cut_length_shape_47,
    "48": calculate_cut_length_shape_48,
    "51": calculate_cut_length_shape_51,
    "52": calculate_cut_length_shape_52,
    "56": calculate_cut_length_shape_56,
    "63": calculate_cut_length_shape_63,
    "64": calculate_cut_length_shape_64,
    "67": calculate_cut_length_shape_67,
    "75": calculate_cut_length_shape_75,
    "77": calculate_cut_length_shape_77,
    "98": calculate_cut_length_shape_98,
    "99": calculate_cut_length_shape_99
}


# Minimum bend radii (in mm) for different bar diameters (in mm) as per BS 8660:2020.
# These values are illustrative and should be verified against the official standard.
MIN_BEND_RADII = {
    6: 12,   # 4 * 6mm
    8: 16,   # 4 * 8mm
    10: 20,  # 4 * 10mm
    12: 24,  # 4 * 12mm
    16: 32,  # 4 * 16mm
    20: 70, # 5 * 20mm
    25: 87, # 5 * 25mm
    32: 112, # 6 * 32mm
    40: 140, # 6 * 40mm
    50: 175, # 6 * 50mm
}