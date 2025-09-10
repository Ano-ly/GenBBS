import os

folders = [
    "src/gui",
    "src/core",
    "src/export",
    "tests",
    "resources",
    "installer",
    "packaging",
    "docs"
]

base_path = r"c:\Users\Amy-Jay\Desktop\programming\GenBBS"

for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create empty README.md and requirements.txt
open(os.path.join(base_path, "docs", "README.md"), "a").close()
open(os.path.join(base_path, "requirements.txt"), "a").close()
