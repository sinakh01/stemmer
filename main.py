from utilities.file_utils import read_text_file, write_list_to_file
from utilities.preprocessing_utils import remove_stopwords, normalize_words, stem_words
from utilities.evaluation_utils import calculate_precision, calculate_recall

"""
https://github.com/sinakh01/stemmer

Ghabl az ejra bayad pishniyazha nasb shavad:
1. python -m venv venv
2. venv\Scripts\activate
2. pip install -r requirements.txt
"""

# Insert the relative path for the input file that needs to processed
input_text = read_text_file("tests/input2.txt")
# Insert the relative path for the manually created file that contains the expected words
golden_output = read_text_file("tests/output2.txt").split()
word_list = input_text.lower().split()

output = stem_words(normalize_words(remove_stopwords(word_list)))
precision = calculate_precision(output, golden_output)
recall = calculate_recall(output, golden_output)

print('\nScript Output:', output)
print('Expected Output:', golden_output)
print('Precision:', precision)
print('Recall:', recall)

write_list_to_file("output.txt", output, precision, recall)
