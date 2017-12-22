import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    (a, b, e, p) = map(int, input.readline().split(" "))
    for rule in [[map(int, line.split(" "))] for line in input]:
        
        output.print("hello")




if __name__ == '__main__':
    main()
