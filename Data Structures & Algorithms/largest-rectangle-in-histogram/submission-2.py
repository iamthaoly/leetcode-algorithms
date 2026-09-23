class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h, n = heights, len(heights)
        prefix = [-1] * len(heights)
        suffix = [n] * len(heights)
        stack = []
        # Forgot to set def suffix to n (instead of -1)
        # Forgot to reset stack

        for i in range(n):
            # while stack and h[i] < h[stack[-1]]:
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prefix[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            # while stack and h[i] < h[stack[-1]]:
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                suffix[i] = stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(len(heights)):
            prefix[i] += 1
            suffix[i] -= 1
            res = max(res, heights[i] * (suffix[i] - prefix[i] + 1))

        # print(prefix)
        # print(suffix)
        # [0, 0, 2, 2, 2, 5]
        # [0, 5, 2, 5, 5, 5]

        return res