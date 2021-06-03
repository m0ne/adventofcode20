import re


def check_if_complete(passport_string, keys, has_validation):
    if all(x in passport_string for x in keys):
        if (has_validation):
            for key in keys:
                if(re.search(keys[key], passport_string) == None):
                    return 0
            return 1
        else:
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
    print("Nr. Passports: ", len(serialized_passports))
    return serialized_passports


def count(serialized_passports, keys, has_validation):
    valid_passport_count = 0
    for pp in serialized_passports:
        pp_as_string = ' '.join(map(str, pp))
        # print(pp_as_string)
        valid_passport_count += check_if_complete(pp_as_string, keys, has_validation)
    return valid_passport_count


def main():
    passports = open("input.txt", "r").read().split("\n")

    keys = {
        "byr": r"byr:\s*(19[2-9]\d|200[0-2])\b",
        "iyr": r"iyr:\s*20(1\d|20)\b",
        "eyr": r"eyr:\s*20(2\d|30)\b",
        "hgt": r"hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",
        "hcl": r"hcl:\s*#[0-9a-f]{6}\b",
        "ecl": r"ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b",
        "pid": r"pid:\s*\d{9}\b",
    }

    serialized_input = serialize(passports)

    print("Part: 1 - Valid:", count(serialized_input, keys, False))
    print("Part: 2 - Valid:", count(serialized_input, keys, True))


if (__name__ == "__main__"):
    main()
