class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binary_search(low, high, h):
            while low < high:
                mid = (low + high) // 2
                cnt = 0
                for p in piles:
                    cnt += math.ceil(p / mid)
                if cnt <= h:
                    high = mid
                else:
                    low = mid + 1

            return high

        upper = max(piles)
        
        min_k = binary_search(1, upper, h)
        return min_k
