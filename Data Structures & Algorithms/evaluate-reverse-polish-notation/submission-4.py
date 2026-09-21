class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token in op:
                res = 0
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    res = (num1 + num2)
                if token == "-":
                    res = (num1 - num2)
                if token == "*":
                    res = (num1 * num2)
                if token == "/":
                    res = num1 / num2
                    res = math.ceil(res) if res < 0 else int(res)
                stack.append(res)
            else:
                num = int(token)
                stack.append(num)

        # print(stack)
        return stack[0]