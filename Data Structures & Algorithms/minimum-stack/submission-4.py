class MinStack:
    def __init__(self):
        self.stack = []
        self.length = 0
        self.value = 0
        # others
    
    def push(self, val:int)-> None:
            self.stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
    