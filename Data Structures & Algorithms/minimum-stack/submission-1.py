class MinStack:

    def __init__(self):
        self.stack = [] # Empty Stack Creation
        self.minStack = [] # Empty minStack Creation
        

    def push(self, val: int) -> None:
        self.stack.append(val) # add the value to the end of the list
        if not self.minStack or val <= self.minStack[-1]: # if minStack is empty or if val is less than the current minStack value
            self.minStack.append(val) # add the value to the minStack

    def pop(self) -> None:
        val = self.stack.pop() # pop the stack
        if val == self.minStack[-1]: # if the value is removed check if its on the minStack and remove it there
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # return the top of the stack
        

    def getMin(self) -> int:
        return self.minStack[-1] # return the top of the minStack

        
