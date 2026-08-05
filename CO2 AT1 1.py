# Morphological Analysis Pipeline for Document Indexing

words = ["connected", "connecting", "connection"]

# Suffix rules
suffix_rules = {
    "ed": "Inflectional",
    "ing": "Inflectional",
    "ion": "Derivational"
}

# Function for morphological analysis
def analyze_word(word):
    for suffix, suffix_type in suffix_rules.items():
        if word.endswith(suffix):
            root = word[:-len(suffix)]
            normalized = root

            return root, suffix, suffix_type, normalized

    return word, "None", "None", word


# Display output in table format

print("-" * 75)
print(f"{'Word':15}{'Root':15}{'Suffix':10}{'Type':20}{'Normalized'}")
print("-" * 75)

for word in words:
    root, suffix, suffix_type, normalized = analyze_word(word)

    print(f"{word:15}{root:15}{suffix:10}{suffix_type:20}{normalized}")

print("-" * 75)