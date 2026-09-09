class MinStack:

    def __init__(self):
        self.stack_all = deque()
        self.stack_min = deque()

    def push(self, val: int) -> None:
        self.stack_all.append(val)
        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)

    def pop(self) -> None:
        num = self.stack_all.pop()
        if num == self.stack_min[-1]:
            self.stack_min.pop()

    def top(self) -> int:
        return self.stack_all[-1]
        

    def getMin(self) -> int:
        return self.stack_min[-1]
        
