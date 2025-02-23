import pytest
from .stack import Solution


@pytest.mark.parametrize(
    "parens, output_bool",
    [("()", True), ("()[]{}", True), ("(]", False), ("){", False)],
)
def test_isValid(parens, output_bool):
    assert Solution().isValid(parens) == output_bool


import pytest


@pytest.mark.parametrize(
    "funcs, params",
    [
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [2], [0], [-3], [], [], [], []],
        ),
    ],
)
def test_MinStack(funcs, params):
    stack = []
    for f, p in zip(funcs, params):
        if f == "MinStack":
            if stack:
                raise NameError("MinStack already declared")
            stack = Solution().MinStack()
        if f == "push":
            try:
                if not p:
                    raise AttributeError
                stack.push(p)
            except AttributeError:
                print("push() called on None stack, or null arg")
        if f == "getMin":
            try:
                stack.getMin()
            except AttributeError:
                print("getMin() called on None stack")
        if f == "pop":
            try:
                stack.pop()
            except AttributeError:
                print("pop() called on None stack")


@pytest.mark.parametrize(
    "tokens,output",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_evalRPN(tokens, output):
    assert Solution().evalRPN(tokens) == output


@pytest.mark.parametrize(
    "n, output",
    [
        (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
        (1, {"()"}),
    ],
)
def test_generateParenthesis(n, output):
    assert set(Solution().generateParenthesis(n)) == set(output)


@pytest.mark.parametrize(
    "temperatures, output",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 45, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([55, 38, 53, 81, 61, 93, 97, 32, 43, 78], [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]),
    ],
)
def test_dailyTemperatures(temperatures, output):
    assert Solution().dailyTemperatures(temperatures) == output


@pytest.mark.parametrize(
    "target, position, speed, output",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (100, [0, 2, 4], [4, 2, 1], 1),
        (10, [3], [3], 1),
    ],
)
def test_carFleet(target, position, speed, output):
    assert Solution().carFleet(target, position, speed) == output
