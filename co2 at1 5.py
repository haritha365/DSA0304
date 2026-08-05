# Porter Stemmer Example

from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("{:<12} {:<20} {:<15}".format(
    "Word", "Intermediate Form", "Final Stem"))

for word in words:

    intermediate = word

    # Show simple intermediate form
    if word.endswith("ational"):
        intermediate = word.replace("ational", "ate")
    elif word.endswith("ation"):
        intermediate = word.replace("ation", "ate")

    stem = ps.stem(word)

    print("{:<12} {:<20} {:<15}".format(
        word, intermediate, stem))