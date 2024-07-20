class Queue:
    def __init__(self, items=None, maxSize=None) -> None:
        self.items = items if items else []
        self.max_size = maxSize
        self.remove_items = []

    def size(self):
        return len(self.items)
    def isFull(self):
        return self.max_size is not None and self.size() >= self.max_size
    def enQueue(self, i):
        if self.isFull():
            return
        self.items.append(i)
        print(self)

    def deQueue(self):
        if self.isEmpty():
            print(self)
            return
        remove_item = self.items.pop(0)
        self.remove_items.append(remove_item)
        print(f"{remove_item} <- {self}")
    def peekleft(self):
        return self.items[0]
    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return ", ".join([item for item in self.items]) if not self.isEmpty() else "Empty"
    def run(self,command_list: str):
        for command in command_list:
            parts = command.strip().split()
            action = parts[0]
            if(action == "E"):
                item = parts[1] 
                self.enQueue(item)
            elif(action == "D"):
                self.deQueue()

        print((", ".join([item for item in self.remove_items]) if self.remove_items else "Empty") + f" : {self}")

            
queue = Queue()
queue.run(input("Enter Input : ").split(","))