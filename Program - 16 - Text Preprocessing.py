#PROGRAM – 16 Text Preprocessing: Bag-of-Words Encoding for 'Text' Column"
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

d=pd.DataFrame({
    'Text': [ "I'm Deepak R Raj, I am a Digital Marketer.",
                "Calm in approach, fierce in resolve,!",
                "I turn complexity into clarity,",
              "making every challenge a deliberate step forward.",
    ]
})

v = CountVectorizer()

x = v.fit_transform(d['Text'])

bf = pd.DataFrame(x.toarray(), columns=v.get_feature_names_out())

result = pd.concat([d, bf], axis=1)
print(result)
