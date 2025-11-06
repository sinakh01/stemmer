from typing import List
from collections import Counter
"""
Precision:
Precision measures how many of the items you predicted as “positive” were actually correct.

Precision = True Positives (TP) / (True Positives (TP) + False Positives (FP))

Example:
If your system predicts 10 words as correct, but only 7 of them actually match the gold standard:

Precision = 7/10

---------------

Recall:
Recall measures how many of the actual correct items your model successfully found.

Recall = True Positives (TP) / (True Positives (TP) + False Negatives(FN))

Example:
If there are 10 correct words in total, and your model only finds 7 of them:

Recall = 7/10
"""

# collections.Counter turns each list into a dictionary of word frequencies:

# Example:
# predicted = ["cat", "cat", "dog", "fish"]
# expected = ["cat", "dog", "dog"]

# Then:
# predicted_counts = {"cat": 2, "dog": 1, "fish": 1}
# expected_counts  = {"cat": 1, "dog": 2}

def calculate_precision(predicted: List[str], expected: List[str]) -> float:
    if not predicted:
        return 0.0  # Avoid division by zero
    
    predicted_counts = Counter(predicted)
    expected_counts = Counter(expected)

    # True positives = sum of min(counts) for words that appear in both lists
    true_positives = sum(min(predicted_counts[w], expected_counts[w]) for w in predicted_counts)
    total_predicted = sum(predicted_counts.values())

    precision = true_positives / total_predicted
    return precision

def calculate_recall(predicted: List[str], expected: List[str]) -> float:
    if not expected:
        return 0.0  # Avoid division by zero if gold standard is empty
    
    predicted_counts = Counter(predicted)
    expected_counts = Counter(expected)

    # True positives: words that appear in both, considering their min counts
    true_positives = sum(min(predicted_counts[w], expected_counts[w]) for w in predicted_counts)
    total_expected = sum(expected_counts.values())

    recall = true_positives / total_expected
    return recall