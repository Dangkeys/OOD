class Stack:
    def __init__(self,items = None) -> None:
        self.items = items if items else []
    def __str__(self) -> str:
        return "".join(self.items)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def push(self,item):
        return self.items.append(item)
    def peek(self):
        return self.items[-1]
    def pop(self):
        if self.is_empty():
            return "Empty"
        return self.items.pop()
    
class Queue:
    def __init__(self,items = None,max_size=None) -> None:
        self.items = items if items else []
        self.max_size = max_size
    def __str__(self) -> str:
        return "".join(self.items)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def is_full(self):
        return self.max_size is not None and self.size() >= self.max_size
    def enqueue(self,item):
        if self.is_full():
            return
        return self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        return self.items.pop(0)
normal, mirror = input("Enter Input (Normal, Mirror) : ").split()


