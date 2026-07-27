string = input("Enter a string (a,b): ")

state = "q0"

print("\nTransition Path:")
print(state, end="")

for ch in string:

    if state == "q0":
        if ch == "a":
            state = "q1"
        else:
            state = "q0"

    elif state == "q1":
        if ch == "a":
            state = "q1"
        else:
            state = "q2"

    elif state == "q2":
        if ch == "a":
            state = "q1"
        else:
            state = "q0"

    print(" ->", state, end="")

print()

if state == "q2":
    print("Accepted")
else:
    print("Rejected")