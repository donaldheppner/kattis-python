import itertools

stack = [0]
target = 3

while len(stack) > 0:
    val = stack[-1]
    if val == target:
        print(stack, sep=' ', end='\n')
        stack.pop()
        if len(stack) == 0:
            break

        stack[-1] += 1
        continue
    else:
        stack.append(val + 1)

stack = [0]
target = 3

# while len(stack) > 0:
#     for x in [x for x in range(0, target) if x not in stack]:
#         stack.append(x)
#         print(stack)    # do something
#     else:
#         while len(stack) > 0 and stack[-1] == target - 1 and stack[-1] + 1 in stack:
#             stack.pop()
#         else:
#             stack[-1] += 1
#

input = [x for x in range(0, 4)]
factorials = [0] * (len(input) + 1)
factorials[0] = 1

for i in range(1, len(input) + 1):
    factorials[i] = factorials[i-1] * i

print(factorials)

    # for next_junction in [x for x in all if x not in path and current.can_connect(x, path)]:
    #     costs.append(find_min_cost(next_junction, target, all, path.copy()))

