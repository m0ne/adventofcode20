

def check_if_complete(passport_string, params):
    if all(x in passport_string for x in params):
        return 1
    return 0


def serialize(passports):
    serialized_passports = []
    serialized_passport = []
    for passport in passports:
        parameters = passport.split(" ")
        if (passport):
            for parameter in parameters:
                serialized_passport.append(parameter)
        if (len(passport) == 0):
            serialized_passports.append(serialized_passport)
            serialized_passport = []

    serialized_passports.append(serialized_passport)
    print("Number of Passports:       ", len(serialized_passports))
    return serialized_passports


def count(serialized_passports, params):
    valid_passport_count = 0
    for pp in serialized_passports:
        pp_as_string = ' '.join(map(str, pp))
        # print(pp_as_string)
        valid_passport_count += check_if_complete(pp_as_string, params)
    print("Number of Valid Passworts: ", valid_passport_count) 
    return valid_passport_count


def main():
    passports = open("input.txt", "r").read().split("\n")

    params = ["byr",
              "iyr",
              "eyr",
              "hgt",
              "hcl",
              "ecl",
              "pid",
              ]

    serialized_input = serialize(passports)
    valid_passports = count(serialized_input, params)


if (__name__ == "__main__"):
    main()
