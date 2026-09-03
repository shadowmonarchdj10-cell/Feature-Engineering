import re
from nltk.stem import PorterStemmer
# Sample text
text = "Data Science uses scientific methods algorithms and many types of processes."
# Initialize stemmer
stemmer = PorterStemmer()
# Extract words using regex instead of tokenizing
words = re.findall(r'\b\w+\b', text)
# Apply stemming
stemmed_words = [stemmer.stem(word) for word in words]
# Join back into a string (if needed)
stemmed_text = ' , '.join(stemmed_words)
print(stemmed_text)
