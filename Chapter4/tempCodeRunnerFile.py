class Node:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.next_student = None
        self.next_course = None

class MultiList:
    def __init__(self):
        self.heads = {}  # A dictionary to store both student and course heads

    def add_enrollment(self, student, course):
        new_node = Node(student, course)
        
        # Add to course list
        if course not in self.heads:
            self.heads[course] = new_node
        else:
            current = self.heads[course]
            while current.next_student:
                current = current.next_student
            current.next_student = new_node
        
        # Add to student list
        if student not in self.heads:
            self.heads[student] = new_node
        else:
            current = self.heads[student]
            while current.next_course:
                current = current.next_course
            current.next_course = new_node

    def display(self):
        # Display courses and enrolled students
        print("Courses and their students:")
        for key, head in self.heads.items():
            if key.startswith('C'):  # If key is a course
                print(f"{key}: ", end="")
                current = head
                while current:
                    print(current.student, end=" -> ")
                    current = current.next_student
                print("None")

        # Display students and their courses
        print("\nStudents and their courses:")
        for key, head in self.heads.items():
            if key.startswith('s'):  # If key is a student
                print(f"{key}: ", end="")
                current = head
                while current:
                    print(current.course, end=" -> ")
                    current = current.next_course
                print("None")

# Example usage
multilist = MultiList()
enrollments = [
    ('s1', 'C1'), ('s1', 'C3'),
    ('s2', 'C1'),
    ('s3', 'C1'), ('s3', 'C2'), ('s3', 'C3'), ('s3', 'C4'),
    ('s4', 'C3'), ('s4', 'C4'),
    ('s5', 'C2')
]

for student, course in enrollments:
    multilist.add_enrollment(student, course)

multilist.display()
