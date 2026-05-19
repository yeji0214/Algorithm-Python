class MyQueue:
    myQueue = []
    def __init__(self):
        self.myQueue = []

    def push(self, x: int) -> None:
        self.myQueue.append(x)

    def pop(self) -> int:
        return self.myQueue.pop(0)

    def peek(self) -> int:
        return self.myQueue[0]

    def empty(self) -> bool:
        if len(self.myQueue) > 0:
            return False
        return True