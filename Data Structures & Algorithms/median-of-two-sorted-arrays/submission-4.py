class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def binary_search(arr, low, high, target):
            binary_idx = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= target:
                    binary_idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return binary_idx

        # Test binary search (ok!)
        # a = [2, 3, 5, 8]
        # i = binary_search(a, 0, len(a) - 1, 10)
        # print(i, a[i])
        if not nums1 and not nums2:
            return 0
        single = nums2 if not nums1 else (nums1 if not nums2 else None)
        if single:
            mid = len(single) // 2
            median = single[mid]
            if len(single) % 2 == 0:
                median = (single[mid - 1] + single[mid]) / 2
            return median

        smaller = bigger = None
        if nums1[0] < nums2[0]:
            smaller, bigger = nums1, nums2
        else:
            smaller, bigger = nums2, nums1
        
        half = (len(smaller) + len(bigger)) // 2
        # mid = half
        # if half > len(smaller):
        #     mid = half - len(smaller)
        l = r = 0
        arr = []
        while l < len(smaller):
            # if len(arr) > half:
            #     if (len(smaller) + len(bigger)) % 2 == 0:
            #         return (arr[half] + arr[half - 1]) / 2
            #     return arr[half]
            arr.append(smaller[l])
            if l < len(smaller) - 1 and r <len(bigger) and smaller[l] <= bigger[r] <= smaller[l + 1]:
                # last b[r] <= smaller[l + 1]
                next_r = binary_search(bigger, r, len(bigger) - 1, smaller[l + 1])
                arr += bigger[r:(next_r + 1)]
                r = next_r + 1
            l += 1
        arr += bigger[r:]
        print(arr)
        if (len(smaller) + len(bigger)) % 2 == 0:
            return (arr[half] + arr[half - 1]) / 2
        return arr[half]



