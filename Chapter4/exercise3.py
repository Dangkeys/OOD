class Queue:
    def __init__(self,items = None, maxSize = None) -> None:
        self.items = items if items else []
        self.maxSize = maxSize

    def __str__(self) -> str:
        return str(self.items)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def isFull(self):
        return self.maxSize is not None and self.size() >= self.maxSize
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        self.items.pop(0)

word, hint = input("Enter code,hint : ").strip().split(",")

diff_val = ord(word[0]) - ord(hint) 

q = Queue()
for i in word:
    q.enQueue(chr(ord(i) - diff_val))
    print(q)
