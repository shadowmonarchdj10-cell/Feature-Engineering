#Program - 17 - TF-IDF Transformation on 'Text' Column
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

d = pd.DataFrame({
    'Text': [
        "I, am Deepak R Raj, I am a software engineer.",
        "Calm in approach, fierce in resolve,!",
        "I turn complexity into clarity,",
        "making every challenge a deliberate step forward.",
    ]
})

v = TfidfVectorizer()
x = v.fit_transform(d['Text'])
tfidf = pd.DataFrame(x.toarray(), columns=v.get_feature_names_out())
result = pd.concat([d, tfidf], axis=1)
print(result)
