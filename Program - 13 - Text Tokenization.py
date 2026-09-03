import pandas as pd
import re
data = {
'Text': [
"Neither God can stop me,Nor demons control me!",
"I'm not here to be a choice, I am here to be myself.",
"I’m the lone wolf, My path is mine alone."
]
}
# Load into DataFrame
df = pd.DataFrame(data)
# Define a simple tokenizer function
def simple_tokenizer(text):
  # Lowercase the text (optional)
  text = text.lower()
  # Remove punctuation (keep only words and numbers)
  text = re.sub(r'[^\w\s]', '', text)
  # Split on whitespace
  tokens = text.split()
  return tokens
# Apply the tokenizer
df['Tokens'] = df['Text'].apply(simple_tokenizer)
print(df[['Text', 'Tokens']])
