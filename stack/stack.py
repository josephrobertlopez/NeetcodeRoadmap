class Solution:
    # https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        d = dict()
        stack = list()
        d['}'] = '{'
        d[']'] = '['
        d[')'] = '('
        for char in s:
            if char in d.values():
                stack.append(char)
            elif len(stack) > 0 and d[char] == stack[-1]:
                stack.pop()
        return len(stack) == 0

    # https://leetcode.com/problems/min-stack/
    class MinStack:

        def __init__(self):
            self.stack = list()

        def push(self, val: int) -> None:
            self.stack.append(val)

        def pop(self) -> None:
            self.stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return min(self.stack)

    # https://leetcode.com/problems/evaluate-reverse-polish-notation/
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        tokens.reverse()
        stack = list()
        output = 0
        while len(tokens) > 0:
            if tokens[-1] in ["+", "-", "*", "/"]:
                op = tokens.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                match op:
                    case "-":
                        output = a - b
                    case "+":
                        output = a + b
                    case "*":
                        output = a * b
                    case "/":
                        output = int(a / b)
                stack.append(output)
            else:
                stack.append(tokens.pop())
        return output

    # https://leetcode.com/problems/generate-parentheses/
    def generateParenthesis(self, n: int) -> list[str]:
        stack = list()
        res = list()

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        to_return = [0] * len(temperatures)
        stack = list()
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temp:
                stack_index, stack_head = stack.pop()
                to_return[stack_index] = i - stack_index
            stack.append((i, temp))
        return to_return

    # https://leetcode.com/problems/car-fleet/
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        position_dict = dict()
        stack = list()
        for p, s in zip(position, speed):
            position_dict[p] = s
        position = sorted(position, reverse=True)
        for p2 in position:
            if len(stack) == 0:
                stack.append(p2)
            else:
                p1 = stack[-1]
                s1 = position_dict[p1]
                s2 = position_dict[p2]

                t1 = (target - p1) / (s1)
                t2 = (target - p2) / (s2)
                if t1 < t2:
                    stack.append(p2)
        return len(stack)
    # https://leetcode.com/problems/largest-rectangle-in-histogram/
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
