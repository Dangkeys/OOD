class Queue:
    def __init__(self,items = None, max_size = None) -> None:
        self.items = items if items else []
        self.max_size = max_size
    def __str__(self) -> str:
        return str(self.items)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def is_full(self):
        return self.max_size and self.size() >= self.max_size
    def dequeue(self):
        if self.is_empty():
            return 'Empty'
        return self.items.pop(0)
    def enqueue(self,item, position = None):
        if self.is_full():
            return 'Full'
        if position == None:
            self.items.append(item)
        else:
            self.items.insert(position, item)
    def peek(self, position):
        if self.is_empty():
            return 'Empty'
        return self.items[position]

def radix_sort(arr):
    place = 1
    queues = [Queue() for _ in range(10)]
    max_digit = max(arr)
    while max_digit > 0:
        for number in arr:
            queues[get_number_of_palce(number,place)].enqueue(number)
        
        i = 0
        for queue in queues:
            while not queue.is_empty():
                arr[i] = queue.dequeue()
                i += 1
        
        
        place *= 10
        max_digit-=1
    
    return arr
def get_number_of_palce(number, place):
    return (number // place) % 10
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr) 