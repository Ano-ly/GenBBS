import os
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from pathlib import Path

def generate_bar_image(shape_code, dimensions, bar_id, output_dir):
    """
    Generate and save an image of a bar shape (as per BS8666-style shape codes).

    Args:
        shape_code (str): The shape code (e.g., "11", "21", "41", etc.)
        dimensions (dict): Mapping of labels (A, B, C, ...) to numeric values.
        bar_id (str or int): Unique bar ID to include in filename.
        output_dir (str or Path): Directory where image will be saved.

    Returns:
        str: The path to the saved image file.
    """
    # Ensure output directory exists
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"bar_{shape_code}_{bar_id}.png"

    # Base plot setup
    fig, ax = plt.subplots(figsize=(20, 3))
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    ax.set_xlim(0, 250)
    ax.set_ylim(0, 80)

    # Helper to add labeled line segments
    def draw_segment(x1, y1, x2, y2, label=None):
        add_y = 15 if (x1 == x2) else 3
        ax.plot([x1, x2], [y1, y2], color='black', linewidth=4)
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, mid_y + add_y, label, ha='center', va='bottom', fontsize=30, color='blue')

    # Example drawings for common shape codes
    # (You can extend this list further as needed)
    if shape_code in ["00", "01"]:
        draw_segment(10, 40, 240, 40, f"A={dimensions.get('A', '')}")

    elif shape_code == "11":
        draw_segment(10, 10, 235, 10, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((235, 15), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 15, 240, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "12":
        draw_segment(10, 10, 220, 10, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((220, 20), 20, 20, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(230, 20, 230, 40, f"B={dimensions.get('B', '')}")
        ax.text(190, 20, f"R={dimensions.get('R', '')}", ha='center', fontsize=30, color='blue')
    elif shape_code == "13":
        draw_segment(10, 10, 220, 10, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((220, 30), 40, 40, theta1=270, theta2=90, color='black', linewidth=4))
        draw_segment(220, 50, 140, 50, f"C={dimensions.get('C', '')}")
        ax.text(200, 30, f"B={dimensions.get('B', '')}", ha='center', fontsize=30, color='blue')
    elif shape_code == "14":
        draw_segment(10, 10, 235, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((235, 15), 10, 10, theta1=270, theta2=90, color='black', linewidth=4))
        draw_segment(235, 20, 10, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "15":
        draw_segment(55, 10, 240, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((55, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(50, 15, 10, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "21":
        draw_segment(15, 10, 235, 10, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((235, 15), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 15, 240, 50, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((15, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 15, 10, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "22":
        draw_segment(200, 10, 220, 10, f"D={dimensions.get('D', '')}")
        ax.add_patch(Arc((220, 30), 40, 40, theta1=270, theta2=90, color='black', linewidth=4))
        draw_segment(220, 50, 15, 50, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((15, 45), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(10, 45, 10, 10, f"A={dimensions.get('A', '')}")
        ax.text(200, 30, f"C={dimensions.get('C', '')}", ha='center', fontsize=30, color='blue')
    elif shape_code == "23":
        draw_segment(15, 50, 235, 50, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((235, 45), 10, 10, theta1=360, theta2=90, color='black', linewidth=4))
        draw_segment(240, 45, 240, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((15, 55), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 55, 10, 80, f"A={dimensions.get('A', '')}")
    elif shape_code == "24":
        draw_segment(10, 10, 140, 10, f"A={dimensions.get('A', '')}")
        draw_segment(140, 10, 240, 50, f"B={dimensions.get('B', '')}")
        draw_segment(240, 50, 240, 80, f"C={dimensions.get('C', '')}")
    elif shape_code == "25":
        draw_segment(80, 10, 190, 10, f"E={dimensions.get('E', '')}")
        draw_segment(190, 10, 240, 50, f"B={dimensions.get('B', '')}")
        draw_segment(80, 10, 30, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "26":
        draw_segment(10, 10, 60, 10, f"A={dimensions.get('A', '')}")
        draw_segment(60, 10, 100, 70, f"B={dimensions.get('B', '')}")
        draw_segment(100, 70, 240, 70, f"C={dimensions.get('C', '')}")
    elif shape_code == "27":
        draw_segment(10, 10, 100, 50, f"A={dimensions.get('A', '')}")
        draw_segment(100, 50, 235, 50, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((235, 45), 10, 10, theta1=360, theta2=90, color='black', linewidth=4))
        draw_segment(240, 45, 240, 10, f"C={dimensions.get('C', '')}")
    elif shape_code == "28":
        draw_segment(10, 10, 100, 50, f"A={dimensions.get('A', '')}")
        draw_segment(100, 50, 235, 50, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((235, 55), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 55, 240, 80, f"C={dimensions.get('C', '')}")
    elif shape_code == "29":
        draw_segment(40, 10, 235, 10, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((235, 15), 10, 10, theta1=270, theta2=90, color='black', linewidth=4))
        draw_segment(235, 20, 140, 50, f"B={dimensions.get('B', '')}")
        draw_segment(140, 50, 10, 50, f"C={dimensions.get('C', '')}")
    elif shape_code == "31":
        draw_segment(15, 10, 235, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((235, 15), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 15, 240, 70, f"D={dimensions.get('D', '')}")
        ax.add_patch(Arc((15, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 15, 10, 45, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((15, 45), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(15, 50, 100, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "32":
        draw_segment(15, 40, 235, 40, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((235, 35), 10, 10, theta1=360, theta2=90, color='black', linewidth=4))
        draw_segment(240, 35, 240, 10, f"D={dimensions.get('D', '')}")
        ax.add_patch(Arc((15, 45), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 45, 10, 65, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((15, 65), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(15, 70, 100, 70, f"A={dimensions.get('A', '')}")
    elif shape_code == "33":
        draw_segment(140, 10, 220, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((220, 30), 40, 40, theta1=270, theta2=90, color='black', linewidth=4))
        draw_segment(220, 50, 15, 50, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((15, 45), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(10, 45, 10, 15, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((15, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(15, 10, 220, 10, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((220, 30), 40, 40, theta1=270, theta2=90, color='black', linewidth=4))
        draw_segment(220, 50, 140, 50,  f"C={dimensions.get('C', '')}")
        draw_segment(140, 50, 120, 40, "")
        draw_segment(140, 10, 120, 20, "")
        ax.text(200, 30, f"B={dimensions.get('B', '')}", ha='center', fontsize=30, color='blue')
    elif shape_code == "34":
        draw_segment(10, 10, 60, 10, f"A={dimensions.get('A', '')}")
        draw_segment(60, 10, 100, 70, f"B={dimensions.get('B', '')}")
        draw_segment(100, 70, 235, 70, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((235, 65), 10, 10, theta1=360, theta2=90, color='black', linewidth=4))
        draw_segment(240, 65, 240, 40, f"E={dimensions.get('E', '')}")
    elif shape_code == "35":
        draw_segment(10, 10, 60, 10, f"A={dimensions.get('A', '')}")
        draw_segment(60, 10, 100, 60, f"B={dimensions.get('B', '')}")
        draw_segment(100, 60, 235, 60, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((235, 65), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 65, 240, 80, f"E={dimensions.get('E', '')}")
    elif shape_code == "36":
        draw_segment(15, 10, 140, 10, f"B={dimensions.get('B', '')}")
        draw_segment(140, 10, 240, 70, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((15, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 15, 10, 45, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((15, 45), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(15, 50, 100, 50, f"D={dimensions.get('D', '')}")
    elif shape_code == "41":
        draw_segment(15, 10, 235, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((235, 15), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 15, 240, 45, f"D={dimensions.get('D', '')}")
        ax.add_patch(Arc((235, 45), 10, 10, theta1=360, theta2=90, color='black', linewidth=4))
        draw_segment(235, 50, 200, 50, f"E={dimensions.get('E', '')}")
        ax.add_patch(Arc((15, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 15, 10, 65, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((15, 65), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(15, 70, 100, 70, f"A={dimensions.get('A', '')}")
    elif shape_code == "44":
        draw_segment(65, 10, 185, 10, f"C={dimensions.get('C', '')}")
        ax.add_patch(Arc((185, 15), 10, 10, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(190, 15, 190, 45, f"D={dimensions.get('D', '')}")
        ax.add_patch(Arc((195, 45), 10, 10, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(195, 50, 240, 50, f"E={dimensions.get('E', '')}")
        ax.add_patch(Arc((65, 15), 10, 10, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(60, 15, 60, 65, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((55, 65), 10, 10, theta1=360, theta2=90, color='black', linewidth=4))
        draw_segment(55, 70, 10, 70, f"A={dimensions.get('A', '')}")
    elif shape_code == "46":
        draw_segment(80, 10, 160, 10, f"C={dimensions.get('C', '')}")
        draw_segment(160, 10, 200, 70, f"B={dimensions.get('B', '')}")
        draw_segment(200, 70, 240, 70, f"E={dimensions.get('E', '')}")
        draw_segment(80, 10, 40, 70, f"B={dimensions.get('B', '')}")
        draw_segment(40, 70, 10, 70, f"A={dimensions.get('A', '')}")
    # elif shape_code == "47":
    #     draw_segment(10, 10, 240, 10, f"C={dimensions.get('C', '')}")
    #     draw_segment(240, 10, 240, 70, f"D={dimensions.get('D', '')}")
    #     draw_segment(240, 70, 200, 70, f"E={dimensions.get('E', '')}")
    #     draw_segment(200, 70, 200, 50, f"E={dimensions.get('E', '')}")
    #     draw_segment(10, 10, 10, 70, f"B={dimensions.get('B', '')}")
    #     draw_segment(10, 70, 50, 70, f"A={dimensions.get('A', '')}")
    #     draw_segment(50, 70, 50, 50, f"E={dimensions.get('E', '')}")
    elif shape_code == "48":
        draw_segment(20, 10, 230, 10, f"B={dimensions.get('B', '')}")
        ax.add_patch(Arc((230, 20), 20, 20, theta1=270, theta2=360, color='black', linewidth=4))
        draw_segment(240, 20, 240, 60, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((230, 60), 20, 20, theta1=0, theta2=90, color='black', linewidth=4))
        draw_segment(230, 70, 200, 50, f"D={dimensions.get('D', '')}")
        ax.add_patch(Arc((20, 20), 20, 20, theta1=180, theta2=270, color='black', linewidth=4))
        draw_segment(10, 20, 10, 60, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((20, 60), 20, 20, theta1=90, theta2=180, color='black', linewidth=4))
        draw_segment(20, 70, 50, 50, f"C={dimensions.get('C', '')}")
    elif shape_code == "52":
        draw_segment(90, 10, 150, 10, f"B={dimensions.get('B', '')}")
        draw_segment(150, 10, 150, 70, f"A={dimensions.get('A', '')}")
        draw_segment(150, 70, 140, 70, "")
        draw_segment(140, 70, 130, 60, f"D={dimensions.get('C', '')}")
        draw_segment(90, 10, 90, 70, f"A={dimensions.get('A', '')}")
        draw_segment(90, 70, 150, 70, f"B={dimensions.get('B', '')}")
        draw_segment(150, 70, 150, 60, "")
        draw_segment(150, 60, 140, 50, f"C={dimensions.get('C', '')}")
    elif shape_code == "56":
        draw_segment(40, 10, 240, 10, f"A={dimensions.get('A', '')}")
        draw_segment(240, 10, 140, 70, f"D={dimensions.get('D', '')}")
        draw_segment(140, 70, 10, 70, f"C={dimensions.get('C', '')}")
        draw_segment(10, 70, 10, 10, f"B={dimensions.get('B', '')}")
        draw_segment(10, 10, 50, 10, f"E={dimensions.get('E', '')}")
        draw_segment(50, 10, 60, 20, "")
        draw_segment(10, 10, 10, 50, f"F={dimensions.get('E', '')}")
        draw_segment(10, 50, 20, 60, "")
    elif shape_code == "63":
        draw_segment(90, 10, 150, 10, f"B={dimensions.get('B', '')}")
        draw_segment(150, 10, 150, 70, f"A={dimensions.get('A', '')}")
        draw_segment(150, 70, 90, 70, f"B={dimensions.get('B', '')}")
        draw_segment(90, 70, 90, 40, f"C={dimensions.get('C', '')}")
        draw_segment(90, 40, 100, 30, "")
        draw_segment(90, 10, 90, 70, f"A={dimensions.get('A', '')}")
        draw_segment(90, 70, 150, 70, f"B={dimensions.get('B', '')}")
        draw_segment(150, 70, 150, 40, f"D={dimensions.get('C', '')}")
        draw_segment(150, 40, 140, 30, "")
    elif shape_code == "64":
        draw_segment(140, 10, 170, 10, f"F={dimensions.get('F', '')}")
        draw_segment(170, 10, 180, 20, "")
        draw_segment(140, 10, 140, 70, f"D={dimensions.get('D', '')}")
        draw_segment(140, 70, 240, 70, f"E={dimensions.get('E', '')}")
        draw_segment(240, 70, 240, 10, f"D={dimensions.get('D', '')}")
        draw_segment(240, 10, 10, 10, f"C={dimensions.get('C', '')}")
        draw_segment(10, 10, 10, 40, f"B={dimensions.get('B', '')}")
        draw_segment(10, 40, 200, 40, f"A={dimensions.get('A', '')}")
    elif shape_code == "98":
        draw_segment(10, 10, 40, 10, f"C={dimensions.get('C', '')}")
        draw_segment(40, 10, 40, 40, f"B={dimensions.get('B', '')}")
        draw_segment(40, 40, 150, 70, f"A={dimensions.get('A', '')}")
        draw_segment(150, 70, 150, 40, f"B={dimensions.get('B', '')}")
        draw_segment(150, 40, 180, 40, f"D={dimensions.get('D', '')}")


    

    else:
        # Generic placeholder shape for unsupported codes
        ax.text(50, 30, f"Shape {shape_code}\n(Not defined yet)", 
                ha='center', va='center', fontsize=8, color='gray')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    
    return str(output_path)