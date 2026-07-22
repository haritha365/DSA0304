from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "studies", "playing", "happily"]

print("Stemmed Words:")
for word in words:
    print(word, "->", ps.stem(word))