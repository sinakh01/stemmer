from utilities.file_utils import read_text_file, write_list_to_file
from utilities.preprocessing_utils import remove_stopwords, normalize_words, stem_words
from utilities.evaluation_utils import calculate_precision, calculate_recall
"""
Ghabl az ejra bayad pishniyazha nasb shavad:
1. python -m venv venv
venv\Scripts\activate

2. pip install -r requirements.txt
"""

# Insert the path for the input file that needs to processed
input_text = read_text_file("tests/input1.txt")
# Insert the path for the manually created file that contains the expected words
golden_output = read_text_file("tests/output1.txt").split()
word_list = input_text.lower().split()

output = stem_words(normalize_words(remove_stopwords(word_list)))
precision = calculate_precision(output, golden_output)
recall = calculate_recall(output, golden_output)

print('\nScript Output:', output)
print('Expected Output:', golden_output)
print('Precision:', precision)
print('Recall:', recall)

write_list_to_file("output.txt", output, precision, recall)
