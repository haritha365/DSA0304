# Finite-State Morphological Parser

words = ["writes", "writing", "written"]

print("{:<10} {:<25} {:<12} {:<15} {:<12}".format(
    "Word", "State Path", "Root", "Pattern", "Normalized"))

for word in words:

    if word == "writes":
        path = "Start -> Verb -> s -> End"
        root = "write"
        pattern = "Regular"

    elif word == "writing":
        path = "Start -> Verb -> ing -> End"
        root = "write"
        pattern = "Regular"

    elif word == "written":
        path = "Start -> Verb -> irregular -> End"
        root = "write"
        pattern = "Irregular"

    print("{:<10} {:<25} {:<12} {:<15} {:<12}".format(
        word, path, root, pattern, root))