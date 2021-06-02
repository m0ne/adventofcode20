input = open("input.txt", "r")
serialized = input.read().split("\n")
serialized = serialized[:-1]


[int(i) for i in serialized]

for index in serialized:
    for deep in serialized:
        if ((int(index)+int(deep) == 2020):
            print(int(index)*int(deep))

