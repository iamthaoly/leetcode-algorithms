class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_nums = defaultdict(int)
        for task in tasks:
            task_nums[task] += 1
        
        heap = []
        for task, num in task_nums.items():
            heap.append([-num, task])

        heapq.heapify(heap)
        total_task = len(tasks)
        queue = deque()
        count = 0
        res = []

        while total_task > 0:
            if queue:
                num, task = queue.popleft()
                if num and task:
                    heapq.heappush(heap, [-num, task])
            if heap:
                num, task = heapq.heappop(heap)
                total_task -= 1
                num = (-num) - 1
                res.append(task)
                if num > 0:
                    while len(queue) < n:
                        queue.append([None, None])
                    queue.append([num, task])
            else:
                res.append(None)
            count += 1

        # print(res)
        return count

