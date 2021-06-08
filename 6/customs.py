# One person one line
# encoding: <question> == yes
# 26 questions

from itertools import count


def main():
    groups = serialize()

    solution_1, unique_questions = count_answers(groups)
    solution_2 = count_answers_everyone(groups, unique_questions)

    print("Quiz Part 1:", solution_1)
    print("Quiz Part 2:", solution_2)


def count_answers(answer_groups):
    unique_questions_count = 0
    unique_questions_collection = []
    for group in answer_groups:
        unique_questions = set()
        for subgroup in group:
            for letters in subgroup:
                unique_questions.add(letters)
        unique_questions_count += len(unique_questions)
        unique_questions_collection.append(unique_questions)
    return unique_questions_count, unique_questions_collection


def count_answers_everyone(answer_groups, unique_questions):
    correct_answers_collection_count = 0
    for group in range(len(answer_groups)):
        unique_question = unique_questions[group]
        for answer in range(len(answer_groups[group])):
            correct_answers = set()
            for character in answer_groups[group][answer]:
                correct_answers.add(character)
            unique_question = unique_question.intersection(correct_answers)
        correct_answers_collection_count += (len(unique_question))
    return correct_answers_collection_count


def serialize():
    groups = []
    group = []

    input = open("input.txt", "r").read().split("\n")
    for qa in input:

        if qa:
            group.append(qa)
        else:
            groups.append(group)
            group = []

    groups.append(group)
    return groups


if (__name__ == "__main__"):
    main()
