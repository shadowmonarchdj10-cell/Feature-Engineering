#Program - 15 - Text Lemmatization
import pandas as pd
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

data = {
    'Text': [ "Neither God can stop me,",
              "Nor demons control me!",
             "I'm not here to be a choice,",
              "I'm here to be myself.!",
             "I'm the Lonewolf,",
              "My path is mine alone.",
             ]
    }
df = pd.DataFrame(data)

lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    words = re.findall(r'\b\w+\b', text)
    lemmatized = [lemmatizer.lemmatize(word.lower()) for word in words]
    return ' '.join(lemmatized)

df['Lemmatized_Text'] = df['Text'].apply(lemmatize_text)
print(df)
