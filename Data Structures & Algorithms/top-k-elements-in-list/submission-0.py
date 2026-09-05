class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        arr = []
        for key in freq:
            heapq.heappush(arr, [freq[key], key])
            if len(arr) > k:
                heapq.heappop(arr)
        res = []
        while arr:
            val, key = heapq.heappop(arr)
            res.append(key)
        return res