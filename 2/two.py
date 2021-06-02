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
        new_arg = arg[3:]
    else:
        new_arg = arg[2:]
    
    for high in new_arg:
        if high.isdigit():
            higher = higher + high
        elif high == " ":
            print("---")
        else:
            letter = high
            break

    password = arg[arg.index(letter)+1:]

    print(lower,higher,letter)

    count = (password.count(letter))

    lower = int(lower)
    higher = int(higher)

    if (password[lower+1] == letter and password[higher+1] == letter):
        wrong_passwords = wrong_passwords + 1
    elif (password[lower+1] == letter or password[higher+1] == letter):
        wrong_passwords = wrong_passwords
    else:
        wrong_passwords = wrong_passwords + 1

    higher = ""
    lower = ""
    letter = ""

print("Correct Passwords: ", nr_of_passwords - wrong_passwords)
