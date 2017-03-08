import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def count_changes(a, b):
    changes = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            changes += 1
    return changes


def solve(input, output):
    input.readline()  # skip question
    number_of_answers = int(input.readline())

    answers = [None] * number_of_answers
    changes_per_answer = [0] * number_of_answers
    for i in range(0, number_of_answers):
        answers[i] = input.readline().strip().split(", ")

    for i in range(0, number_of_answers - 1):
        for j in range(i + 1, number_of_answers):
            changes = count_changes(answers[i], answers[j])
            if changes > changes_per_answer[i]:
                changes_per_answer[i] = changes
            if changes > changes_per_answer[j]:
                changes_per_answer[j] = changes

    min_changes = min(changes_per_answer)
    for i, j in enumerate(changes_per_answer):
        if j == min_changes:
            output.write(", ".join(answers[i]))
            output.write("\n")

if __name__ == '__main__':
    main()
