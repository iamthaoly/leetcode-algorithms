class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        cur_max = float("-inf")
        for i in range(len(height)):
            max_left[i] = cur_max = max(cur_max, height[i])
        
        cur_max = float("-inf")
        for i in range(len(height)-1, -1, -1):
            max_right[i] = cur_max = max(cur_max, height[i])

        water = [0] * len(height)   
             
        for i in range(len(height)):
            water[i] = min(max_left[i], max_right[i]) - height[i]

        # print(max_left, max_right)
        return sum(water)

