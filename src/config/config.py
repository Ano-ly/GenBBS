
SHAPE_CODE_LENGTH_MAP = {
    "00": ["A"], # Stock lengths
    "01": ["A"], # Stock lengths
    "11": ["A", "B"],
    "12": ["A", "B", "R"],
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
    "77": ["A", "B", "C"],
    "98": ["A", "B", "C", "D"],
    "99": ["A", "B", "C", "D", "E", "F", "R"] # For all other shapes where standard shapes cannot be used, no specific lengths
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

SHAPE_CODE_FORMULA_STRINGS = {
    "00": "A",
    "01": "A",
    "11": "A + B - 0.5r - d",
    "12": "A + B - 0.43R - 1.2d",
    "13": "A + 0.57B + C - 1.6d",
    "14": "A + C",
    "15": "A + C",
    "21": "A + B + C - r - 2d",
    "22": "A + B + 0.57C + D - 0.5r - 2.6d",
    "23": "A + B + C - r - 2d",
    "24": "A + B + C",
    "25": "A + B + E",
    "26": "A + B + C",
    "27": "A + B + C - 0.5r - d",
    "28": "A + B + C - 0.5r - d",
    "29": "A + B + C",
    "31": "A + B + C + D - 1.5r - 3d",
    "32": "A + B + C + D - 1.5r - 3d",
    "33": "2A + 1.7B + 2C - 4d",
    "34": "A + B + C + E - 0.5r - d",
    "35": "A + B + C + E - 0.5r - d",
    "36": "A + B + C + D - r - 2d",
    "41": "A + B + C + D + E - 2r - 4d",
    "44": "A + B + C + D + E - 2r - 4d",
    "46": "A + 2B + C + E",
    "47": "2A + B + 2C + 2q - 3r - 6d",
    "48": "2A + B + 2C - r - 2d",
    "51": "2(A + B + C) - 2.5r - 5d",
    "52": "2(A + B) + 2C - 1.5r - 3d",
    "56": "A + B + C + D + 2E - 1.5r - 3d",
    "63": "2A + 3B + 2C - 3r - 6d",
    "64": "A + B + C + 2D + E + F - 3r - 6d",
    "67": "A (See clause 10)",
    "75": "π (A - d) + B + 25",
    "77": "Cπ(A-d) or C((π(A -d))² + B²)0.5 if B > A/5",
    "98": "A + 2B + C + D - 2r - 4d",
    "99": "Sum of all provided lengths"
}

#Value of minimum end dimension for bend >= 150
P1 = {  6:110, 
        8:115,
        10:120,
        12:125,
        16:140,
        20:190,
        25:235,
        32:305,
        40:380,
        50:475,
    }
#Value of minimum end dimension for bend < 150
#Only P2 will be used in this application for better simplification.
P2 = {  6:110, 
        8:115,
        10:130,
        12:155,
        16:210,
        20:290,
        25:365,
        32:465,
        40:580,
        50:725,
}
#3d +2r approx to higher multiple of 5
Q_HOOK_DIA = {
        6:45, 
        8:60,
        10:70,
        12:85,
        16:115,
        20:200,
        25:250,
        32:320,
        40:400,
        50:400, #Should be N/A accroding to BS 8666:2020
}

NO_OF_COLS_FOR_ITEMS = {"Project": 1, "CategoryHigher": 1, "CategoryLower": 1, "Element": 1, "Bar": 1}