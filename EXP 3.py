import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required data (first time only)
nltk.download('punkt')
nltk.download('punkt_tab')

text = "running runs easily studies studying"

# Tokenize the text
words = word_tokenize(text)

# Create Porter Stemmer object
ps = PorterStemmer()

print("Original Words:")
print(words)

print("\nStemmed Words:")
for word in words:
    print(word, "->", ps.stem(word))