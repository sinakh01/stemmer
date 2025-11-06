from pathlib import Path
from typing import List

def read_text_file(relative_file_path: str) -> str:

    base_path = Path().resolve() # Daryafter adresse motlaghe main.py
    final_path = base_path / relative_file_path
    return final_path.read_text(encoding="utf-8")

def write_list_to_file(file_path: str, items: List[str], precision: float, recall: float) -> None:
    """
    Writes a list of strings to a text file, one item per line.
    If the file doesn't exist, it will be created.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")

        file.write("\n--- Evaluation Factors ---\n")
        # Write precision and recall, rounded to 2 decimals
        file.write(f"Precision: {precision:.2f}\n")
        file.write(f"Recall: {recall:.2f}\n")
        
