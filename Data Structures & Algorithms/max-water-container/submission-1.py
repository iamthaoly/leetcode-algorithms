class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # input: heights[], h[i] is height of i bar
        # 2 <= len(h) <= 1000
        # 0 <= h[i] <= 1000
        # two bars -> container
        # output: max water a container can store

        # calculate water?
        # count * min (bar 1, bar 2)
        max_water = 0
        l = 0
        r = len(heights) - 1
        while (l < r):
            water = (r - l) * min(heights[l], heights[r])
            max_water = max(max_water, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        
        return max_water


