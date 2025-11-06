Simple NLTK Stemmer & Text Normalization Script

This project implements a **lightweight NLP preprocessing pipeline** using **NLTK**.  
It includes:

✅ Stopword removal  
✅ Word normalization (punctuation removal, hyphen preservation)  
✅ Lemmatization-based stemming  
✅ Precision & recall evaluation  

The project is designed for educational purposes.

## ✅ Usage

Before running the script, initialize a virtual environment & install the project prerequisites:
Run in terminal

python -m venv venv
venv\Scripts\activate

then:
pip install -r requirements.txt

Simply insert your input & golden output file path as the arguments for the following methods in the main.py file:
input_text = read_text_file("tests/input1.txt")
golden_output = read_text_file("tests/output1.txt").split()

## ✅ Features

### 🔹 1. Stopword removal
Removes basic English stopwords such as:
is, a, the, to, of

### 🔹 2. Word normalization
- Converts to lowercase
- Removes `'s`
- Removes all `.` dots for words such as U.S.A
- Keeps hyphens (e.g., `state-of-the-art`)
- Extracts wordlike tokens using regex

### 🔹 3. Lemmatization-based stemming
Uses:
- `WordNetLemmatizer`
- POS tags from `averaged_perceptron_tagger_eng`

Example:
countrymen → countryman
running → run
better → good

### 🔹 4. Evaluation metrics
Provides:

- **Precision**  
- **Recall**

Based on comparing your output tokens vs. a gold standard.

---

✅ Example Output:

Input: John's new U.S.A. laptop is a state-of-the-art device. The price is high, but the quality is amazing!

Script Output: ['john', 'new', 'usa', 'laptop', 'state-of-the-art', 'device', 'price', 'high', 'but', 'quality', 'amazing']

Expected Output: ['john', 'new', 'usa', 'laptop', 'state-of-the-art', 'device', 'price', 'high', 'but', 'quality', 'amazing']

Precision: 0.75 
Recall: 1.00
