import numpy as np
import math
input = open("input.txt", "r")


def treeNapper(character):
    if character == ".":
        return 1
    if character == "#":
        return 0


def serialize():
    serialized = input.read().split('\n')

    mapped_array = []
    line_length = len(serialized[0])

    for line in serialized:
        mapped_array.append(list(map(treeNapper, line)))

    return mapped_array, line_length


def slopeSetter(steps_vert, steps_hor):
    x = 0
    count = 0

    for i in range(0, len(mapped_array), steps_vert):
        if (mapped_array[i][x] == 0):
            count += 1
        if ((steps_hor + x) >= line_length):
            x = (x + steps_hor) - line_length
        else:
            x = x + steps_hor

    print("Final Trees: ", count)
    print("steps_vert:  ", steps_vert)
    print("steps_hor:   ", steps_hor)
    print("-------------------")
    return count


if (__name__ == "__main__"):
    mapped_array, line_length = serialize()
    tree_count_1 = slopeSetter(1, 3)
    tree_count_2 = math.prod([slopeSetter(1, 1), slopeSetter(
        1, 3), slopeSetter(1, 5), slopeSetter(1, 7), slopeSetter(2, 1)])
    print("Quiz 1: ", tree_count_1)
    print("Quiz 2: ", tree_count_2)
