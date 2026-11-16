class MinStack:

    def __init__(self):
        self.stack =[]
        self.minele = float('inf')

    def push(self, val: int) -> None:
        self.minele = min(self.minele, val)
        self.stack.append([val,self.minele])

    def pop(self) -> None:
        self.stack.pop()

        self.minele = self.stack[-1][1] if self.stack  else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
