class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t, j = stack.pop()
                res[j] = i - j
            stack.append([temperatures[i], i])

        return res
            

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        # Mistakes:
        # - Init deque [x, y] wrong

        stack = deque([(temperatures[0], 0)])
        # print(stack)
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t, j = stack.pop()
                res[j] = i - j
            stack.append([temperatures[i], i])

        res[-1] = 0
        # print(res)
        return res

