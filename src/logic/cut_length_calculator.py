import math
from src.config.config import Q_HOOK_DIA

def calculate_cut_length_shape_00(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 00 (straight bar).
    Formula: A
    """
    A = lengths.get("A", 0)
    return A / 1000.0

def calculate_cut_length_shape_01(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 01 (stock lengths).
    Formula: A
    """
    A = lengths.get("A", 0)
    return A / 1000.0

def calculate_cut_length_shape_11(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 11 (U-shaped bar).
    Formula: A + B - 0.5r - d
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    # r is the internal bend radius, d is the diameter
    # The formula provided in the search results is A + B - 0.5r - d
    # Assuming r is bend_radius and d is diameter
    return (A + B - (0.5 * bend_radius) - diameter) / 1000.0

def calculate_cut_length_shape_12(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 12 (L-shaped bar).
    Formula: A + B - 0.43R - 1.2d
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    # R is the external bend radius, d is the diameter
    # The formula provided in the search results is A + B - 0.43R - 1.2d
    # Assuming R is bend_radius and d is diameter
    return (A + B - (0.43 * bend_radius) - (1.2 * diameter)) / 1000.0

def calculate_cut_length_shape_13(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 13 (hooked bar).
    Formula: A + 0.57B + C - 1.6d
    B shall not be less than 2(r + d).
    Neither A nor C shall be less than P in Table 2 nor less than (B/2 + 5d).
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + (0.57 * B) + C - (1.6 * diameter)) / 1000.0

def calculate_cut_length_shape_14(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 14 (cranked bar).
    Formula: A + C
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    C = lengths.get("C", 0)
    return (A + C) / 1000.0

def calculate_cut_length_shape_15(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 15 (cranked bar).
    Formula: A + C
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    C = lengths.get("C", 0)
    return (A + C) / 1000.0

def calculate_cut_length_shape_21(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 21 (two bends).
    Formula: A + B + C - r - 2d
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    # r is the internal bend radius, d is the diameter
    print (f"Bend radius:{bend_radius}, diameter: {diameter}, A:{A}, B:{B}, C{C}")
    return (A + B + C - (bend_radius) - (2 * diameter)) / 1000.0

def calculate_cut_length_shape_22(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 22 (two bends).
    Formula: A + B + 0.57C + D - 0.5r - 2.6d
    C shall not be less than 2(r + d).
    Neither A nor (D) shall be less than P in Table 2. (D) shall not be less than C/2 + 5d or 90
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    return (A + B + (0.57 * C) + D - (0.5 * bend_radius) - (2.6 * diameter)) / 1000.0

def calculate_cut_length_shape_23(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 23 (two bends).
    Formula: A + B + C - r - 2d
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + B + C - bend_radius - (2 * diameter)) / 1000.0

def calculate_cut_length_shape_24(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 24 (two bends).
    Formula: A + B + C
    A and (C) are at 90° to one another.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + B + C) / 1000.0

def calculate_cut_length_shape_25(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 25 (two bends).
    Formula: A + B + E
    Neither A nor B shall be less than P in Table 2. If E is the critical dimension, schedule as 99 and specify A or B as the free dimension.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    E = lengths.get("E", 0)
    return (A + B + E) / 1000.0

def calculate_cut_length_shape_26(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 26 (two bends).
    Formula: A + B + C
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + B + C) / 1000.0

def calculate_cut_length_shape_27(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 27 (two bends).
    Formula: A + B + C - 0.5r - d
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + B + C - (0.5 * bend_radius) - diameter) / 1000.0

def calculate_cut_length_shape_28(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 28 (two bends).
    Formula: A + B + C - 0.5r - d
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + B + C - (0.5 * bend_radius) - diameter) / 1000.0

def calculate_cut_length_shape_29(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 29 (two bends).
    Formula: A + B + C
    Neither A nor (C) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return (A + B + C) / 1000.0

def calculate_cut_length_shape_31(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 31 
    Formula: A + B + C + D - 1.5r - 3d
    Neither A nor (D) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    return (A + B + C + D - (1.5 * bend_radius) - (3 * diameter)) / 1000.0

def calculate_cut_length_shape_32(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 32 
    Formula: A + B + C + D - 1.5r - 3d
    Neither A nor (D) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    return (A + B + C + D - (1.5 * bend_radius) - (3 * diameter)) / 1000.0


def calculate_cut_length_shape_33(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 33 (stirrup/link).
    Formula: 2A + 1.7B + 2C - 4d
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    # r is the internal bend radius, d is the diameter
    return (2*A + 1.7*B + 2*C - (4 * diameter)) / 1000.0

def calculate_cut_length_shape_34(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 34 (three bends).
    Formula: A + B + C + E - 0.5r - d
    Neither A nor (E) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    E = lengths.get("E", 0)
    return (A + B + C + E - (0.5 * bend_radius) - diameter) / 1000.0

def calculate_cut_length_shape_35(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 35 (three bends).
    Formula: A + B + C + E - 0.5r - d
    Neither A nor (E) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    E = lengths.get("E", 0)
    return (A + B + C + E - (0.5 * bend_radius) - diameter) / 1000.0

def calculate_cut_length_shape_36(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 36 (three bends).
    Formula: A + B + C + D - r - 2d
    Neither A nor (D) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    return (A + B + C + D - bend_radius - (2 * diameter)) / 1000.0

def calculate_cut_length_shape_41(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 41 (four bends).
    Formula: A + B + C + D + E - 2r - 4d
    Neither A nor (E) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    E = lengths.get("E", 0)
    return (A + B + C + D + E - (2 * bend_radius) - (4 * diameter)) / 1000.0

def calculate_cut_length_shape_44(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 44 (four bends).
    Formula: A + B + C + D + E - 2r - 4d
    Neither A nor (E) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    E = lengths.get("E", 0)
    return (A + B + C + D + E - (2 * bend_radius) - (4 * diameter)) / 1000.0

def calculate_cut_length_shape_46(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 46 (four bends).
    Formula: A + 2B + C + E
    Neither A nor (E) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    E = lengths.get("E", 0)
    return (A + (2 * B) + C + E) / 1000.0

# To be reviewed
def calculate_cut_length_shape_47(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 47 (four bends).
    Formula: 2A + B + 2C + 2q - 3r - 6d
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    q = Q_HOOK_DIA.get(int(diameter), 0)
    return ((2 * A) + B + (2 * C) + (2 * q) + (3 * bend_radius) - (6 * diameter)) / 1000.0

def calculate_cut_length_shape_48(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 48 (three bends).
    Formula: 2A + B + 2C - r - 2d
    C and D shall be equal and not more than A or less than P
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return ((2*A) + B + (2*C) - bend_radius - (2 * diameter)) / 1000.0

def calculate_cut_length_shape_51(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 51 (five bends).
    Formula: 2(A + B + C) - 2.5r - 5d
    (C) and (D) shall be equal and not more than A nor less than P in Table 2.
    Where (C) and (D) are to be minimized the following formula may be used: L = 2A + 2B + max (16d, 160)
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return ((2 * (A + B + C)) - (2.5 * bend_radius) - (5 * diameter)) / 1000.0

def calculate_cut_length_shape_52(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 52 (five bends).
    Formula: 2(A + B) + 2C - 1.5r - 3d
    (C) and (D) shall be equal and not more than A nor less than P in Table 2.
    Where (C) and (D) are to be minimized the following formula may be used: L = 2A + 2B + max (16d, 160)
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return ((2 * (A + B)) + (2 * C) - (1.5 * bend_radius) - (3 * diameter)) / 1000.0


def calculate_cut_length_shape_56(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 56 (five bends).
    Formula: A + B + C + D + 2E - 1.5r - 3d
    (E) and (F) shall be equal and not more than B or C, nor less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    E = lengths.get("E", 0)
    return (A + B + C + D + (2 * E) - (1.5 * bend_radius) - (3 * diameter)) / 1000.0

def calculate_cut_length_shape_63(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 63 (six bends).
    Formula: 2A + 3B + 2C - 3r - 6d
    (C) and (D) shall be equal and not more than A or B nor less than P in Table 2.
    Where (C) and (D) are to be minimized the following formula may be used: L = 2A + 3B + max(14d, 150)
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    return ((2 * A) + (3 * B) + (2 * C) - (3 * bend_radius) - (6 * diameter)) / 1000.0

def calculate_cut_length_shape_64(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 64 (six bends).
    Formula: A + B + C + 2D + E + F - 3r - 6d
    Neither A nor (F) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    E = lengths.get("E", 0)
    F = lengths.get("F", 0)
    return (A + B + C + (2 * D) + E + F - (3 * bend_radius) - (6 * diameter)) / 1000.0

def calculate_cut_length_shape_67(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 67 (special shape).
    Formula: A (See clause 10) - This shape code typically refers to a drawn shape.
    For now, we'll assume it's a straight length A.
    """
    A = lengths.get("A", 0)
    return A / 1000.0

def calculate_cut_length_shape_75(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 75 (circular).
    Formula: π (A - d) + B + 25
    Where B is the lap.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    return (math.pi * (A - diameter) + B + 25) / 1000.0

def calculate_cut_length_shape_77(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 77 (helical/spiral).
    Formula: Cπ(A-d)
    Where B is greater than A/5 this equation no longer applies, in which case the following formula may be used:
    L = C((π(A -d))² + B²)0.5
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0) # Number of turns
    if B > (A / 5):
        return (C * math.sqrt((math.pi * (A - diameter))**2 + B**2)) / 1000.0
    else:
        return (C * math.pi * (A - diameter)) / 1000.0

def calculate_cut_length_shape_98(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 98 (isometric sketch).
    Formula: A + 2B + C + D - 2r - 4d
    Neither C or (D) shall be less than P in Table 2.
    """
    A = lengths.get("A", 0)
    B = lengths.get("B", 0)
    C = lengths.get("C", 0)
    D = lengths.get("D", 0)
    return (A + (2 * B) + C + D - (2 * bend_radius) - (4 * diameter)) / 1000.0

def calculate_cut_length_shape_99(lengths: dict, diameter: float, bend_radius: float) -> float:
    """
    Calculates cut length for Shape Code 99 (special shape - drawn out).
    This shape code requires the length to be calculated from a drawing.
    For programmatic purposes, this might involve a more complex geometric calculation or
    a direct input of the total length. For now, we'll assume a sum of all provided lengths.
    """
    return sum(lengths.values()) / 1000.0