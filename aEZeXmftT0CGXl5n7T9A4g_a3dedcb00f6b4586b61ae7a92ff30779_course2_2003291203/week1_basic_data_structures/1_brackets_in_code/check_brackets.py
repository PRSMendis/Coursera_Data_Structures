# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

# print('test')
# standard_input = 'hello world'
# print(input())


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    pos = 0
    for i, next in enumerate(text):
        pos = i + 1
        if next in "([{":
            stack.append((pos, next))
        if next in ")]}":
            if len(stack) == 0:
                stack.append((pos, next))
                break
            if are_matching(stack[-1][1],  next):
                stack.pop()
            else:
                stack.append((pos, next))
                break

    if len(stack) > 0:
        return stack[-1][0]
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
