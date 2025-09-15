class Stack:
    def __init__ (self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(f"The Added item is : {item}")

    def pop(self):
        if self.is_empty():
            print("The Stack is Empty, can't pop")
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("The Stack is Empty, can't peek")
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top element", s.peek())
print("Popped element", s.pop())
print("Peeking after poping", s.peek())
print("If the stack is impty", s.is_empty())




#after a lot of struggle and error's finally completed this one 