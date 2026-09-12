class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(arr):
            low, high = 0, len(arr) - 1 
            boundary_index = -1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] <= timestamp:
                    boundary_index = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return boundary_index

        if key not in self.storage:
            return ""

        times = self.storage[key]
        i = binary_search(times)

        if i != -1:
            return times[i][1]
            
        return ""

