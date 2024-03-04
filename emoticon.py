import pandas as pd
import re

# def extract_emoticon(text_list):
#     # Refined regular expression pattern
#     emoticon_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002700-\U000027BF\U00002600-\U000026FF\U00002C60-\U00002C7F\U0001F018-\U0001F021\U0001F1E0-\U0001F1FF\U0001F3FB-\U0001F3FF]+'

#     # Extract and collect emoticons into a new DataFrame
#     emoticons_list = []
#     for text in text_list:
#         emoticons = re.findall(emoticon_pattern, text.strip())
#         for emoticon in emoticons:
#             emoticons_list.extend(emoticon)

#     # Create a new DataFrame from the collected emoticons list
#     emoticons_df = pd.DataFrame({"emoticon": emoticons_list})
#     return emoticons_df
def extract_emoticon(text_list):
    emoticon_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002700-\U000027BF\U00002600-\U000026FF\U00002C60-\U00002C7F\U0001F018-\U0001F021\U0001F1E0-\U0001F1FF\U0001F3FB-\U0001F3FF]+'
    emoticons_dict = {}
    for text in text_list:
        emoticons = re.findall(emoticon_pattern, text.strip())
        for emoticon in emoticons:
            if emoticon in emoticons_dict:
                emoticons_dict[emoticon] += 1
            else:
                emoticons_dict[emoticon] = 1
    emoticons_df = pd.DataFrame({"emoticon": list(emoticons_dict.keys()), "values": list(emoticons_dict.values())})
    return emoticons_df

text = "aku lagi senang dong 😂😂😂😂 aku lagi senang dong 😂😂😂😂 🤲🤲🤲🤲🤲 hahahaha 🤣🤣🤣"
result = extract_emoticon(text)
print(result)