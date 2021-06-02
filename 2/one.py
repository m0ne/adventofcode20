input = open("input.txt", "r")
serialized = input.read().split("\n")
serialized = serialized[:-1]

nr_of_passwords = len(serialized)
wrong_passwords = 0
lower = ""
higher = ""
letter = ""

for arg in serialized:
    for low in arg:
        if low.isdigit():
            lower = lower + low
        else:
            break

    if len(lower) > 1:
        arg = arg[3:]
    else:
        arg = arg[2:]
    
    for high in arg:
        if high.isdigit():
            higher = higher + high
        elif high == " ":
            print("---")
        else:
            letter = high
            break

    password = arg[arg.index(letter)+3:]

    print(lower,higher,letter)

    count = (password.count(letter))

    if (count < int(lower) or count > int(higher)):
        wrong_passwords = wrong_passwords + 1

    higher = ""
    lower = ""
    letter = ""

print("Correct Passwords: ", nr_of_passwords - wrong_passwords)
