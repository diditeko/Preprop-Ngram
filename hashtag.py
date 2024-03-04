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

# def extract_hashtags(text):
#     # Extract hashtags using regex
#     hashtags = re.findall(r'#\w+', str(text))

#     # Flatten the list and convert to lowercase
#     hashtags = [tag.lower() for tag in hashtags]

#     # Create a DataFrame from the hashtags
#     hashtags_df = pd.DataFrame({'Hashtags': hashtags})

#     return hashtags_df
def extract_hashtags(text_list):
    hashtags_dict = {}
    for text in text_list:
        hashtags = re.findall(r'#\w+', str(text))
        for hashtag in hashtags:
            hashtag = hashtag.lower()
            if hashtag in hashtags_dict:
                hashtags_dict[hashtag] += 1
            else:
                hashtags_dict[hashtag] = 1
    hashtags_df = pd.DataFrame({"hashtags": list(hashtags_dict.keys()), "values": list(hashtags_dict.values())})
    return hashtags_df

text = ["Here are some #hashtags and #morehashtags #Python #DataScience",
        "alin anak sehat #indonesiasehat #indonesiakuat #indonesiakuat #indonesiasehat"]
result = extract_hashtags(text)
print(result)