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


class ProblemHandler:
    def __init__(self, user_input: str) -> None:
        self.input_split = user_input.split("/")
        self.persons_and_groups = self.input_split[0]
        self.commands = self.input_split[1].split(",")
        self.queue = Queue()
        self.init_group_and_person()
        
    def init_group_and_person(self):
        person_and_group_list = self.persons_and_groups.split(",")
        self.person_by_group = {}
        self.last_position_of_group = {}
        for person_and_group in person_and_group_list:
            group, person = person_and_group.split()
            if group not in self.person_by_group:
                self.person_by_group[group] = []
                self.last_position_of_group[group] = -1
            self.person_by_group[group].append(person)
            
    def get_group_by_person(self, person):
        for group, persons in self.person_by_group.items():
            if person in persons:
                return group
        return None
    
    def enqueue_person(self, person):
        group = self.get_group_by_person(person)
        if group is None:
            return
        
        # Find the correct insert position
        insert_position = self.queue.size()
        for i in range(self.queue.size()):
            current_person = self.queue.items[i]
            current_group = self.get_group_by_person(current_person)
            if current_group == group:
                insert_position = i + 1

        self.queue.enqueue(person, insert_position)
        
        # Update the last position of the group
        for i in range(insert_position, self.queue.size()):
            if self.get_group_by_person(self.queue.items[i]) == group:
                self.last_position_of_group[group] = i

    def run(self):
        for command in self.commands:
            parts = command.split()
            action = parts[0]
            if action == "D":
                result = self.queue.dequeue()
                if result:
                    print(result)
            elif action == "E":
                person = parts[1]
                self.enqueue_person(person)
                # print(self.queue)


# Test case
user_input = input("Enter Input : ")
handler = ProblemHandler(user_input)
handler.run()
