import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    defs_by_word = {}
    defs_by_value = {}

    for line in input:
        line = line.strip()

        if len(line) == 0:
            continue

        items = [x for x in map(str, line.split(" "))]
        if items[0] == "def":
            if len(items) > 3:
                raise Exception("Too many items for def")
            word = items[1];
            value = int(items[2])

            # don't forget to erase old values
            old_value = defs_by_word.get(word)
            if old_value is not None:
                defs_by_value.pop(old_value)

            defs_by_word[word] = value
            defs_by_value[value] = word

        elif items[0] == "clear":
            defs_by_word.clear()
            defs_by_value.clear()

        elif items[0] == "calc":
            expected_word = True
            last_operator = None
            total = 0
            for item in items[1:]:
                if expected_word:
                    expected_word = False
                    value = defs_by_word.get(item)
                    if value is None:
                        output.write("{} {}".format(" ".join(items[1:]), "unknown"))
                        output.write("\n")
                        break

                    if last_operator is None:
                        total = value
                    elif last_operator == "+":
                        total += value
                    elif last_operator == "-":
                        total -= value
                    else:
                        raise Exception("Invalid last operator {}".format(item))
                else:
                    expected_word = True
                    if item == "+" or item == "-":
                        last_operator = item
                    elif item == "=":
                        total_word = defs_by_value.get(total)
                        if total_word is None:
                            output.write("{} {}".format(" ".join(items[1:]), "unknown"))
                            output.write("\n")
                            break
                        else:
                            output.write("{} {}".format(" ".join(items[1:]), total_word))
                            output.write("\n")

                        break
                    else:
                        raise Exception("Invalid operator {}".format(item))
        else:
            raise Exception("Invalid command {}".format(line))


if __name__ == '__main__':
    main()
