class TowerOfHanoi:
    def __init__(self, height):
        self.height = height
        self.max_height = height + 1
        self.pillars = {
            'A': list(range(height, 0, -1)),
            'B': [],
            'C': []
        }
    
    def tower_of_hanoi(self, n, source, auxiliary, target):
        if n == 1:
            self.move_disk(source, target)
            return
        self.tower_of_hanoi(n-1, source, target, auxiliary)
        self.move_disk(source, target)
        self.tower_of_hanoi(n-1, auxiliary, source, target)
    
    def move_disk(self, source, target):
        disk = self.pillars[source].pop()
        self.pillars[target].append(disk)
        print(f"move {disk} from  {source} to {target}")
        self.print_pillars()
    
    def print_pillars(self):
        for i in range(self.max_height - 1, -1, -1):
            for pillar in ['A', 'B', 'C']:
                if i < len(self.pillars[pillar]):
                    print(f"{self.pillars[pillar][i]} ", end=" ")
                else:
                    print("| ", end=" ")
            print()
            

def main():
    try:
        height = int(input("Enter Input : "))
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        
        game = TowerOfHanoi(height)
        game.print_pillars()
        game.tower_of_hanoi(height, 'A', 'B', 'C')
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
