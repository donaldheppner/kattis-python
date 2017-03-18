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

blah = [x for x in range(0, 100)]
blahblah = itertools.permutations(blah)
for x in blahblah:
    print(x)

# while len(stack) > 0:
#     if stack[-1] == target:
#         print(stack, sep=' ', end='\n')
#
#     # for next_junction in [x for x in all if x not in path and current.can_connect(x, path)]:
#     #     costs.append(find_min_cost(next_junction, target, all, path.copy()))
#
#
#     for x in [x for x in range(0, target) if x not in stack]:
#         stack.append(x)
#
#     for x in range(0, target):
#         if x not in stack:
#             stack.append(x)
#             break
