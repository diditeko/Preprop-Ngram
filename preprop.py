from nlp_id.lemmatizer import Lemmatizer 
import pandas as pd
import numpy as np
from nltk import ngrams
import numpy as np
import tensorflow as tf
import re
import string
from nltk.tokenize import word_tokenize
import spacy
from spacy.lang.id.stop_words import STOP_WORDS
from nlp_id.stopword import StopWord
import warnings
from nlp_id.lemmatizer import Lemmatizer 
warnings.filterwarnings('ignore')

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove tab, new line, and backslash
    text = text.replace('\\t', ' ').replace('\\n', ' ').replace('\\u', '').replace('\\', '')
    # Remove non ASCII characters
    text = text.encode('ascii', 'replace').decode('ascii')
    # Remove mention, link, hashtag
    text = ' '.join(re.sub("([@][A-Za-z0-9]+)|(\w+:\/\/\S+)", " ", text).split())
    # Remove incomplete URL
    text = text.replace("http://", " ").replace("https://", " ")
    # Remove numbers
    text = re.sub(r"\d+", "", text)
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove leading and trailing whitespace
    text = text.strip()
    # Remove multiple whitespace into single whitespace
    text = re.sub('\s+', ' ', text)
    # Remove single characters
    text = re.sub(r"\b[a-zA-Z]\b", "", text)
    # NLTK word tokenize
    tokens = word_tokenize(text)
    tokens = ' '.join(tokens)
    return tokens

nlp = spacy.blank("id")
stopword = StopWord()
lemmatizer = Lemmatizer()

def stopword_remover(text):
    text = preprocess_text(text)
    additional_stopwords = pd.read_csv("stopword\stopwords_noise.txt", sep=" ",header=None).values.tolist()
    doc = nlp(text)
    tokens_without_sw = [token.text for token in doc if not token.is_stop and token.text not in additional_stopwords]
    text = ' '.join(tokens_without_sw)
    text = lemmatizer.lemmatize(text)
    test = stopword.remove_stopword(text)
    return test

text = " @prabowo sedang menjemput takdirnya - @AHMADDHANIPRAST -\n\nKatanya perpolitikan indon semangkin membingungkan, lha.... MOSSAD koq dilawan ??😅 @TheMossadIL https://t.co/U0VmtHHRF4"
test = stopword_remover(text)
print(test)