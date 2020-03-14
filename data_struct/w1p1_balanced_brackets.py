import sys
from containers import Stack

def is_balanced(seq):
    stack = Stack()
    brackets = {"(": ")", "[": "]", "{": "}"}

    for idx, char in enumerate(seq):
        if char in brackets.keys():
            stack.push((char, idx + 1))
        elif char in brackets.values():
            if stack.empty():
                return (False, idx + 1)

            top, _ = stack.pop()
            if brackets[top] != char:
                return (False, idx + 1)
        else:
            continue

    return (stack.empty(), len(seq) - 1 if not stack.top() else stack.pop()[1])


def test():
    assert is_balanced("")[0] is True
    assert is_balanced("(")[0] is False
    assert is_balanced("()")[0] is True
    assert is_balanced("({")[0] is False
    assert is_balanced("([{}])")[0] is True
    assert is_balanced(")")[0] is False
    assert is_balanced("ab")[0] is True
    assert is_balanced("[ab]")[0] is True
    assert is_balanced("(ab]")[0] is False
    assert is_balanced("(ab")[0] is False
    assert is_balanced("[][") == (False, 3)
    assert is_balanced("foo(bar[i);") == (False, 10)
    assert is_balanced("([]") == (False, 1)

    print("TESTS: OK")

def main():
    string = input()
    balanced, idx = is_balanced(string)

    print("Success" if balanced else idx)


if __name__ == "__main__":
    test()
    main()