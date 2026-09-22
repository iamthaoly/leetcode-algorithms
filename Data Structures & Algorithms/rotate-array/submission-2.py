class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # print(k)
        # for i in range(k):
        #     nums[i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[i]
        
        # nums[0] - nums[4]
        # i = 2
        # nums[2] - nums[6]
        N = len(nums)
        # q = deque([])
        # for i in range(N - 1, N - k, -1):
        #     q.append(nums[i])

        q = deque(nums)
        # print(q.pop())
        for i in range(k - 1, -1, -1):
            nums[i] = q.pop()
        # print(nums)
        # print(q)
        for i in range(k, N):
            nums[i] = q.popleft()


        