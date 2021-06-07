import math
from math import ceil
# F => lower half
# B => upper half
plane_length = 128
column_length = 7


def mapping(array):
    mapped_to_binary = []
    for character in array:
        if ((character == "B") or (character == "R")):
            mapped_to_binary.append(1)
        if ((character == "F") or (character == "L")):
            mapped_to_binary.append(0)
    return mapped_to_binary


def partition(lower, upper, array, index):
    mid = (lower + upper) / 2

    if (len(array) == index):
        return lower
    if(array[index] == 0):
        return partition(lower, mid, array, index+1)

    if(array[index] == 1):
        return partition(mid, upper, array, index+1)


def serialize(input):
    max_seat_id = 0
    seat_ids = []
    for grouping in input:
        grouping = mapping(grouping)
        row = partition(0, plane_length, grouping[:7], 0)
        column = partition(0, column_length, grouping[7:], 0)
        seat_id = ceil((row * 8) + column)
        seat_ids.append(seat_id)
        max_seat_id = max(max_seat_id, seat_id)
    return max_seat_id, seat_ids


def find_seat(seat_ids):
    seat_ids.sort()
    for i in range(len(seat_ids)-1):
        if (seat_ids[i+1] - seat_ids[i] == 2):
            return (seat_ids[i]+1)


def main():
    input = open("input.txt", "r").read().split("\n")

    result, seat_ids = serialize(input)
    my_seat = find_seat(seat_ids)
    
    print("Quiz Part 1: ", result)
    print("Quiz Part 2: ", my_seat)


if (__name__ == "__main__"):

    main()

# 823
