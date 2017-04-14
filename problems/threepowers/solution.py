import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    number = int(input.readline())
    while number != 0:
        base_two = bin(number - 1)[2:]
        base_two = base_two[::-1]  # reverse string

        answer = []
        for index in range(0, len(base_two)):
            if base_two[index] == '1':
                answer.append(3 ** index)

        if len(answer) > 0:
            output.write("{ ")
            output.write(", ".join(map(str, answer)))
            output.write(" }\n")
        else:
            output.write("{ }\n")

        number = int(input.readline())



if __name__ == '__main__':
    main()
