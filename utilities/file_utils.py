from pathlib import Path
from typing import List

def read_text_file(relative_file_path: str) -> str:

    base_path = Path().resolve()
    final_path = base_path / relative_file_path
    return final_path.read_text(encoding="utf-8")

def write_list_to_file(file_path: str, word_list: List[str], precision: float, recall: float) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        for word in word_list:
            file.write(word + "\n")

        file.write("\n--- Evaluation Factors ---\n")
        file.write(f"Precision: {precision:.2f}\n")
        file.write(f"Recall: {recall:.2f}\n")
        
