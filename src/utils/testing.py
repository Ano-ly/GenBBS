import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def test_image():
    output_dir = r"C:\Users\Amy-Jay\Desktop\programming\GenBBS\src\temp_bar_images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "test_ba.png")

    fig, ax = plt.subplots()
    ax.add_patch(Rectangle((0, 0), 80, 5, color='blue'))
    ax.set_xlim(-10, 100)
    ax.set_ylim(-10, 20)
    ax.axis('off')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved test image to:", output_path)

test_image()
