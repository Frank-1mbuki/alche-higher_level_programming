#!/usr/bin/python3
"""
Generates all answer files for the 'Python - Everything is object' project.
"""
import os

# Map of filenames to their exact single-line contents
answers = {
    "0-answer.txt": "type",
    "1-answer.txt": "id",
    "2-answer.txt": "No",
    "3-answer.txt": "Yes",
    "4-answer.txt": "Yes",
    "5-answer.txt": "No",
    "6-answer.txt": "True",
    "7-answer.txt": "True",
    "8-answer.txt": "True",
    "9-answer.txt": "Yes",
    "10-answer.txt": "True",
    "11-answer.txt": "False",
    "12-answer.txt": "True",
    "13-answer.txt": "True",
    "14-answer.txt": "[1, 2, 3, 4]",
    "15-answer.txt": "[1, 2, 3]",
    "16-answer.txt": "1",
    "17-answer.txt": "[1, 2, 3, 4]",
    "18-answer.txt": "[1, 2, 3]",
    "19-copy_list.py": """#!/usr/bin/python3
def copy_list(l):
    return l.copy()
""",
    "20-answer.txt": "Yes",
    "21-answer.txt": "Yes",
    "22-answer.txt": "No",
    "23-answer.txt": "Yes",
    "24-answer.txt": "True",
    "25-answer.txt": "False",
    "26-answer.txt": "True",
    "27-answer.txt": "No",
    "28-answer.txt": "Yes",
}

for filename, content in answers.items():
    with open(filename, "w", encoding="utf-8") as f:
        # Ensure content ends with a single newline character
        f.write(content.strip() + "\n")

    # Set execution permissions (+x) on executable script files
    if filename.endswith(".py"):
        os.chmod(filename, 0o755)

    print(f"Created {filename}")

print("\nAll task files generated successfully!")
