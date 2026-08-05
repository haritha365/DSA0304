# Morphological Parsing Module

words = ["unhappy", "happiness", "happily"]

print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<12}".format(
    "Word", "Prefix", "Base", "Suffix", "Type", "Root"))

for word in words:

    prefix = "-"
    suffix = "-"
    base = word

    if word.startswith("un"):
        prefix = "un"
        base = word[2:]
        t = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        base = word[:-4]
        if base.endswith("i"):
            base = base[:-1] + "y"
        t = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        base = word[:-2]
        if base.endswith("i"):
            base = base[:-1] + "y"
        t = "Derivational"

    else:
        t = "-"

    print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<12}".format(
        word, prefix, base, suffix, t, "happy"))