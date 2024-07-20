class Queue:
    def __init__(self,items = None, max_size = None, task_duration = None) -> None:
        self.items = items if items else []
        self.max_size = max_size
        self.task_duration = task_duration
        self.last_counter = 0
    def __str__(self) -> str:
        return str(self.items)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def isFull(self):
        return self.max_size is not None and self.size() >= self.max_size
    def enQueue(self, i, last_counter):
        if(self.isEmpty()):
            self.last_counter = last_counter
        self.items.append(i)
    def deQueue(self,last_counter = None):
        if self.isEmpty():
            return None
        self.last_counter = last_counter if last_counter else 0
        return self.items.pop(0)

class Store:
    def __init__(self, people, time) -> None:
        self.main_queue = Queue(items=[person for person in people])
        self.cashier1 = Queue(max_size=5, task_duration=3)
        self.cashier2 = Queue(max_size=5, task_duration=2)
        self.counter = 1
        self.time = time + 1

    def add_person_to_cashier(self):
        if self.cashier1.isFull() and  self.cashier2.isFull():
            return
        person = self.main_queue.deQueue()
        if not person:
            return
        if not self.cashier1.isFull():
            self.cashier1.enQueue(person, self.counter)
        else:
            self.cashier2.enQueue(person, self.counter)

    def handle_task_every_minute(self):
        if self.counter - self.cashier1.last_counter == self.cashier1.task_duration:
            self.cashier1.deQueue(self.counter) 
        if self.counter -  self.cashier2.last_counter == self.cashier2.task_duration:
            self.cashier2.deQueue(self.counter)
        self.add_person_to_cashier()


    def run(self):
        for i in range(1,self.time):
            self.handle_task_every_minute()
            print(f"{self.counter} {self.main_queue} {self.cashier1} {self.cashier2}")
            self.counter += 1
    


people, time = input("Enter people and time : ").split()  

store = Store(people=people,time=int(time))
store.run()