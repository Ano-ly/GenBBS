# src/logic/bs8666_validator.py

# This module will contain functions for validating bar dimensions against BS 8666:2020.
# Each function will return a boolean indicating validity and a warning message if not compliant.
from src.config.config import MIN_BEND_RADII, SHAPE_CODE_LENGTH_MAP, SHAPE_CODE_FORMULA_STRINGS, P2, P2, Q_HOOK_DIA

def validate_bar_dimensions(dimensions: dict, shape_code: str, diameter: str) -> tuple[bool, list[str], list[str]]:
    """
    Validates bar dimensions against BS 8666:2020 requirements.

    Args:
        dimensions (dict): A dictionary of bar dimensions (e.g., {'A': 100, 'B': 200}).
        shape_code (str): The shape code of the bar.
        diameter (float): The diameter of the bar.

    Returns:
        list[str]: A list of warning messages for non-compliant dimensions.
    """
    warnings = []
    affected_dimensions = []

    # Placeholder for BS 8666:2020 validation rules
    # Example: A simple rule for dimension 'A'
    diameter = int(''.join(filter(str.isdigit, diameter)))
    for key, value in dimensions.items():
        if value != "":
            dimensions[key] = int(float(value))
        else:
            dimensions[key] = 0
    match shape_code:
        case "00":
            is_valid, errs, aff_dims = validate_shape_00(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "01":
            is_valid, errs, aff_dims = validate_shape_01(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "11":
            is_valid, errs, aff_dims = validate_shape_11(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "12":
            is_valid, errs, aff_dims = validate_shape_12(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "13":
            is_valid, errs, aff_dims = validate_shape_13(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "14":
            is_valid, errs, aff_dims = validate_shape_14(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "15":
            is_valid, errs, aff_dims = validate_shape_15(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "21":
            is_valid, errs, aff_dims = validate_shape_21(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "22":
            is_valid, errs, aff_dims = validate_shape_22(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "23":
            is_valid, errs, aff_dims = validate_shape_23(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "24":
            is_valid, errs, aff_dims = validate_shape_24(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "25":
            is_valid, errs, aff_dims = validate_shape_25(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "26":
            is_valid, errs, aff_dims = validate_shape_26(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "27":
            is_valid, errs, aff_dims = validate_shape_27(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "28":
            is_valid, errs, aff_dims = validate_shape_28(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "29":
            is_valid, errs, aff_dims = validate_shape_29(dimensions, diameter) 
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "31":
            is_valid, errs, aff_dims = validate_shape_31(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "32":
            is_valid, errs, aff_dims = validate_shape_32(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "33":
            is_valid, errs, aff_dims = validate_shape_33(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "34":
            is_valid, errs, aff_dims = validate_shape_34(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "35":
            is_valid, errs, aff_dims = validate_shape_35(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "36":
            is_valid, errs, aff_dims = validate_shape_36(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "41":
            is_valid, errs, aff_dims = validate_shape_41(dimensions, diameter)  
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "44":
            is_valid, errs, aff_dims = validate_shape_44(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "46":
            is_valid, errs, aff_dims = validate_shape_46(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "47":
            is_valid, errs, aff_dims = validate_shape_47(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "48":
            is_valid, errs, aff_dims = validate_shape_48(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "51":
            is_valid, errs, aff_dims = validate_shape_51(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "52":
            is_valid, errs, aff_dims = validate_shape_52(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "56":
            is_valid, errs, aff_dims = validate_shape_56(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "63":
            is_valid, errs, aff_dims = validate_shape_63(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "64":
            is_valid, errs, aff_dims = validate_shape_64(dimensions, diameter)  
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "67":
            is_valid, errs, aff_dims = validate_shape_67(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "75":
            is_valid, errs, aff_dims = validate_shape_75(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "77":
            is_valid, errs, aff_dims = validate_shape_77(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "98":
            is_valid, errs, aff_dims = validate_shape_98(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case "99":
            is_valid, errs, aff_dims = validate_shape_99(dimensions, diameter)
            warnings.extend(errs)
            affected_dimensions.extend(aff_dims)
        case _:
            pass
    is_valid = True if len(warnings) == 0 else False
    return (is_valid, warnings, affected_dimensions)

def validate_shape_00(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    return True, [], []

def validate_shape_01(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    return True, [], []

def validate_shape_11(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['B'] < P_value:
        is_valid = False
        err_strs.append(f"B must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('B')
    return is_valid, err_strs, affected_dims

def validate_shape_12(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    min_value = dimensions['R'] + diameter + max((5 * diameter), 90)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < min_value:
        is_valid = False
        err_strs.append(f"A must be greater than R + d + (5d or 90 whichever is greater) [{min_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['B'] < min_value:
        is_valid = False
        err_strs.append(f"B must be greater than R + d + (5d or 90 whichever is greater) [{min_value}]: See BS8666:2020")
        affected_dims.append('B')
    return is_valid, err_strs, affected_dims

def validate_shape_13(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    min_value1 = (dimensions['B'] / 2) + max((5 * diameter), 90)
    min_value2 = Q_HOOK_DIA.get(diameter, 0)
    max_value = 400 + (2 * diameter)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < min_value1:
        is_valid = False
        err_strs.append(f"A must be greater than (B/2) + (5d or 90 whichever is greater) [{min_value1}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['C'] < min_value1:
        is_valid = False
        err_strs.append(f"C must be greater than (B/2) + (5d or 90 whichever is greater) [{min_value1}]: See BS8666:2020")
        affected_dims.append('C')
    if dimensions['B'] < min_value2:
        is_valid = False
        err_strs.append(f"B must be greater than hook diameter [{min_value2}]: See BS8666:2020")
        affected_dims.append('B')
    if dimensions['B'] > max_value:
        is_valid = False
        err_strs.append(f"B must be less than 400 + (2d) [{max_value}]: See BS8666:2020")
        affected_dims.append('B')
    return is_valid, err_strs, affected_dims

def validate_shape_14(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_15(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume bend angle > 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_21(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_22(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    min_value1 = (dimensions['C'] / 2) + max((5 * diameter), 90)
    min_value2 = Q_HOOK_DIA.get(diameter, 0)
    max_value = 400 + (2 * diameter)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['D'] < P_value:
        is_valid = False
        err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('D')
    if dimensions['D'] < min_value1:
        is_valid = False
        err_strs.append(f"D must be greater than (C/2) + (5d or 90 whichever is greater) [{min_value1}]: See BS8666:2020")
        affected_dims.append('D')
    if dimensions['C'] < min_value2:
        is_valid = False
        err_strs.append(f"C must be greater than hook diameter [{min_value2}]: See BS8666:2020")
        affected_dims.append('C')
    if dimensions['C'] > max_value:
        is_valid = False
        err_strs.append(f"C must be less than 400 + (2d) [{max_value}]: See BS8666:2020")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims


def validate_shape_23(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_24(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume bend angle > 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_25(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume bend angle > 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['B'] < P_value:
        is_valid = False
        err_strs.append(f"B must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('B')
    return is_valid, err_strs, affected_dims

def validate_shape_26(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume bend angle > 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_27(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are <= 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_28(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are <= 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_29(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are <= 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('C')
    return is_valid, err_strs, affected_dims

def validate_shape_31(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['D'] < P_value:
        is_valid = False
        err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_32(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['D'] < P_value:
        is_valid = False
        err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_33(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    min_value1 = (dimensions['B'] / 2) + max((5 * diameter), 90)
    min_value2 = Q_HOOK_DIA.get(diameter, 0)
    min_value3 = (dimensions['B'] / 2) + dimensions['C']
    max_value = 400 + (2 * diameter)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < min_value3:
        is_valid = False
        err_strs.append(f"A must be greater than (B/2) + C [{min_value3}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['C'] < min_value1:
        is_valid = False
        err_strs.append(f"C must be greater than (B/2) + (5d or 90 whichever is greater) [{min_value1}]: See BS8666:2020")
        affected_dims.append('C')
    if dimensions['B'] < min_value2:
        is_valid = False
        err_strs.append(f"B must be greater than hook diameter [{min_value2}]: See BS8666:2020")
        affected_dims.append('B')
    if dimensions['B'] > max_value:
        is_valid = False
        err_strs.append(f"B must be less than 400 + (2d) [{max_value}]: See BS8666:2020")
        affected_dims.append('B')
    return is_valid, err_strs, affected_dims

def validate_shape_34(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are <= 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['E'] < P_value:
        is_valid = False
        err_strs.append(f"E must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('E')
    return is_valid, err_strs, affected_dims

def validate_shape_35(dimensions: dict, diameter: int, affected_dims: list[str] = []) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are <= 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['E'] < P_value:
        is_valid = False
        err_strs.append(f"E must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('E')
    return is_valid, err_strs, affected_dims

def validate_shape_36(dimensions: dict, diameter: int, affected_dims: list[str] = []) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are <= 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['D'] < P_value:
        is_valid = False
        err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_41(dimensions: dict, diameter: int, affected_dims: list[str] = []) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['E'] < P_value:
        is_valid = False
        err_strs.append(f"E must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('E')
    return is_valid, err_strs, affected_dims

def validate_shape_44(dimensions: dict, diameter: int, affected_dims: list[str] = []) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['E'] < P_value:
        is_valid = False
        err_strs.append(f"E must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('E')
    return is_valid, err_strs, affected_dims

def validate_shape_46(dimensions: dict, diameter: int, affected_dims: list[str] = []) -> tuple[bool, list[str], list[str]]:
    #Assume BOTH bend angles are > 150
    P_value = P2.get(diameter, 0)
    err_strs = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('A')
    if dimensions['E'] < P_value:
        is_valid = False
        err_strs.append(f"E must be greater than P[{P_value}]: See BS8666:2020 for allowances if bend angle >= 150")
        affected_dims.append('E')
    return is_valid, err_strs, affected_dims

def validate_shape_47(dimensions: dict, diameter: int, affected_dims: list[str] = []) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    max_value = dimensions['A']
    err_strs = []
    is_valid = True
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    #Commented out because D is not supplied at the frontend and will eventually equal C
    # if dimensions['D'] < P_value:
    #     is_valid = False
    #     err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    if dimensions['C'] > max_value:
        is_valid = False
        err_strs.append(f"C must be less than A [{max_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] > max_value:
    #     is_valid = False
    #     err_strs.append(f"D must be less than A [{max_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_48(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    max_value = dimensions['A']
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] < P_value:
    #     is_valid = False
    #     err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    if dimensions['C'] > max_value:
        is_valid = False
        err_strs.append(f"C must be less than A [{max_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] > max_value:
    #     is_valid = False
    #     err_strs.append(f"D must be less than A [{max_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_51(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    max_value = min(dimensions['A'], dimensions['B'])
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] < P_value:
    #     is_valid = False
    #     err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    if dimensions['C'] > max_value:
        is_valid = False
        err_strs.append(f"C must be less than A and B [{max_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] > max_value:
    #     is_valid = False
    #     err_strs.append(f"D must be less than A and B [{max_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_52(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    max_value = dimensions['B']
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] < P_value:
    #     is_valid = False
    #     err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    if dimensions['C'] > max_value:
        is_valid = False
        err_strs.append(f"C must be less than B [{max_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] > max_value:
    #     is_valid = False
    #     err_strs.append(f"D must be less than B [{max_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_56(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    max_value = min(dimensions['A'], dimensions['B'])
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['E'] < P_value:
        is_valid = False
        err_strs.append(f"E must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('E')
    if dimensions['F'] < P_value:
        is_valid = False
        err_strs.append(f"F must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('F')
    if dimensions['E'] > max_value:
        is_valid = False
        err_strs.append(f"E must be less than A and B [{max_value}]: See BS8666:2020")
        affected_dims.append('E')
    if dimensions['F'] > max_value:
        is_valid = False
        err_strs.append(f"F must be less than A and B [{max_value}]: See BS8666:2020")
        affected_dims.append('F')
    return is_valid, err_strs, affected_dims

def validate_shape_63(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    max_value = dimensions['A']
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] < P_value:
    #     is_valid = False
    #     err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    if dimensions['C'] > max_value:
        is_valid = False
        err_strs.append(f"C must be less than A [{max_value}]: See BS8666:2020")
        affected_dims.append('C')
    # if dimensions['D'] > max_value:
    #     is_valid = False
    #     err_strs.append(f"D must be less than A [{max_value}]: See BS8666:2020")
    #     affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_64(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['A'] < P_value:
        is_valid = False
        err_strs.append(f"A must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('A')
    if dimensions['F'] < P_value:
        is_valid = False
        err_strs.append(f"F must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('F')
    return is_valid, err_strs, affected_dims

def validate_shape_67(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    return True, [], []

def validate_shape_75(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    return True, [], []

def validate_shape_77(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    return True, [], []

def validate_shape_98(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    P_value = P2.get(diameter, 0)
    err_strs = []
    affected_dims = []
    is_valid = True
    if dimensions['C'] < P_value:
        is_valid = False
        err_strs.append(f"C must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('C')
    if dimensions['D'] < P_value:
        is_valid = False
        err_strs.append(f"D must be greater than P[{P_value}]: See BS8666:2020")
        affected_dims.append('D')
    return is_valid, err_strs, affected_dims

def validate_shape_99(dimensions: dict, diameter: int) -> tuple[bool, list[str], list[str]]:
    return True, [], []
