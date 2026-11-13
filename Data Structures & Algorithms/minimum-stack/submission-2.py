class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minimum = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        if not self.minimum or val <= self.minimum[0]:
            self.minimum.appendleft(val)

    def pop(self) -> None:
        popped = self.stack.popleft()
        if popped == self.minimum[0]:
            self.minimum.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minimum[0]
