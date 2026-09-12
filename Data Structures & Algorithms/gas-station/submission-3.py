class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        if sum_gas < sum_cost:
            return -1
        cur = 0
        res = 0
        for i in range(len(gas)):
            cur += (gas[i] - cost[i])
            if cur < 0:
                cur = 0
                res = i + 1
        return res


    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        # Mistakes
        # - Not store index
        # - left.pop() instead of left.popleft() in the else case

        left = deque([])
        for i in range(len(gas)):
            left.append([gas[i] - cost[i], i])
        
        cur_sum = 0
        travel = deque([])
        print(left)
        while left:
            if not travel or cur_sum >= left[0][0]:
                move = left.popleft()
                cur_sum += move[0]
                travel.append(move)
            else:
                move = left.popleft()
                cur_sum += move[0]
                travel.appendleft(move)
            
        print(travel)
        if cur_sum < 0:
            return -1
        return travel[0][1]
                

            



