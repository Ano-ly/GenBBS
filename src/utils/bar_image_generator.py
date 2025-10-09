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
        ax.plot([x1, x2], [y1, y2], color='black', linewidth=4)
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, mid_y + 3, label, ha='center', va='bottom', fontsize=30, color='blue')

    # Example drawings for common shape codes
    # (You can extend this list further as needed)
    if shape_code in ["00", "01"]:
        draw_segment(10, 40, 240, 40, f"A={dimensions.get('A', '')}")

    elif shape_code == "11":
        draw_segment(10, 10, 240, 10, f"B={dimensions.get('B', '')}")
        draw_segment(240, 10, 240, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "13":
        draw_segment(10, 10, 240, 10, f"A={dimensions.get('A', '')}")
        draw_segment(240, 10, 240, 50, f"B={dimensions.get('B', '')}")
        draw_segment(240, 50, 140, 50, f"C={dimensions.get('C', '')}")
    elif shape_code == "14":
        draw_segment(10, 10, 240, 10, f"C={dimensions.get('C', '')}")
        draw_segment(240, 10, 10, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "15":
        draw_segment(50, 10, 240, 10, f"C={dimensions.get('C', '')}")
        draw_segment(50, 10, 10, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "21":
        draw_segment(10, 10, 240, 10, f"B={dimensions.get('B', '')}")
        draw_segment(240, 10, 240, 50, f"C={dimensions.get('C', '')}")
        draw_segment(10, 10, 10, 50, f"A={dimensions.get('A', '')}")
    elif shape_code == "22":
        draw_segment(200, 10, 240, 10, f"D={dimensions.get('D', '')}")
        draw_segment(240, 10, 240, 50, f"C={dimensions.get('C', '')}")
        draw_segment(240, 50, 10, 50, f"B={dimensions.get('B', '')}")
        draw_segment(10, 50, 10, 10, f"A={dimensions.get('A', '')}")

    elif shape_code == "41":
        draw_segment(10, 20, 50, 20, f"A={dimensions.get('A', '')}")
        draw_segment(50, 20, 50, 40, f"B={dimensions.get('B', '')}")
        draw_segment(50, 40, 20, 40, f"C={dimensions.get('C', '')}")
        draw_segment(20, 40, 20, 20, f"D={dimensions.get('D', '')}")
        draw_segment(20, 20, 10, 20, f"E={dimensions.get('E', '')}")

    elif shape_code == "12":
        # Sample with a bend radius
        draw_segment(10, 20, 60, 20, f"A={dimensions.get('A', '')}")
        ax.add_patch(Arc((60, 25), 10, 10, theta1=270, theta2=360, color='black'))
        draw_segment(65, 25, 65, 50, f"B={dimensions.get('B', '')}")
        ax.text(60, 30, f"R={dimensions.get('R', '')}", ha='center', fontsize=8, color='blue')

    else:
        # Generic placeholder shape for unsupported codes
        ax.text(50, 30, f"Shape {shape_code}\n(Not defined yet)", 
                ha='center', va='center', fontsize=8, color='gray')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    
    return str(output_path)