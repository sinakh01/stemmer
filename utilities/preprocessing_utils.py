import re
from typing import List
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

def remove_stopwords(word_list: List[str]) -> List[str]:
    stop_words = {"is", "a", "the", "to", "of"}
    return [word for word in word_list if word not in stop_words]

def normalize_words(word_list: List[str]) -> List[str]:

    """
    Keeps:
    - Dashes inside words (like state-of-the-art)
    
    Removes:
    - Ownership 's
    - All dots
    - Sentence-ending punctuation
    """

    all_words: List[str] = []
    for word in word_list:
        # Remove ownership 's
        word = re.sub(r"'s\b", "", word, flags=re.IGNORECASE)
        
        # Remove all dots (for words like U.S.A.)
        word = word.replace(".", "")
        
        # Extract words with optional dashes. Word boundaries are defined by punctuation marks
        words = re.findall(r'\b\w+(?:-\w+)*\b', word)
        all_words.extend(words)

    return all_words

def stem_words(word_list: List[str]) -> List[str]:

  # Ensure required data for nltk is available
    required_packages = ["wordnet", "averaged_perceptron_tagger_eng", "omw-1.4"]
    for pkg in required_packages:
        try:
            nltk.data.find(f"corpora/{pkg}")
        except LookupError:
            nltk.download(pkg)

    # Map POS tags (from nltk) to WordNet POS tags
    def get_wordnet_pos(nltk_tag: str):
        if nltk_tag.startswith('J'):
            return wordnet.ADJ
        elif nltk_tag.startswith('V'):
            return wordnet.VERB
        elif nltk_tag.startswith('N'):
            return wordnet.NOUN
        elif nltk_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN 

   # Tag each word with its POS (Part of Speech)
   # e.g: countrymen -> (countrymen, N)
    pos_tags = nltk.pos_tag(word_list)

    # Lemmatize each word with its correct POS
    return [WordNetLemmatizer().lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]



