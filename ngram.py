import pandas as pd
import numpy as np
import nltk
from nltk import ngrams
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import tensorflow as tf
import pickle
import re
import string
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences

def generate_N_grams(text,ngram=3):
    text= nltk.word_tokenize(text)
    temp=zip(*[text[i:] for i in range(0,ngram)])
    ans=[' '.join(ngram) for ngram in temp]
    return ans

preprocessed_text = "jokowi widodo adalah penghianat bangsa indonesia dengan melakukan praktik plotik dinasti"
ngram_result = generate_N_grams(preprocessed_text, ngram=3)
print(ngram_result)