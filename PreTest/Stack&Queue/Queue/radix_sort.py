class Queue:
    def __init__(self, items=None, max_size=None) -> None:
        self.items = items if items else []
        self.max_size = max_size

    def __str__(self) -> str:
        return str(self.items)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.max_size is not None and self.size() >= self.max_size
    
    def enqueue(self, item, position=-1):
        if self.is_full():
            return
        
        if position == -1 or position >= self.size():
            self.items.append(item)
        else:
            self.items.insert(position, item)

    def dequeue(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.items.pop(0)


def radix_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the maximum number to know the number of digits
    max_num = max(arr)
    max_digits = len(str(max_num))

    # Initialize queues for each digit (0 to 9)
    queues = [Queue() for _ in range(10)]

    # Start with the least significant digit
    place = 1
    while max_digits > 0:
        # Distribute the elements into queues based on the current digit
        for num in arr:
            digit = (num // place) % 10
            queues[digit].enqueue(num)

        # Collect the numbers from the queues
        i = 0
        for queue in queues:
            while not queue.is_empty():
                arr[i] = queue.dequeue()
                i += 1

        # Move to the next digit place
        place *= 10
        max_digits -= 1

    return arr


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
