user_input = int(input('Enter Input : '))
def get_size(): return (2*user_input) + 4
def get_half_size(): return get_size() /2
for row in range(get_size()):
    for col in range(get_size()):
        if row < get_half_size():
            if col >= get_half_size():
                print('#'if row >= 1 and row <= user_input and col < get_size() -1 and col >= get_size() - user_input - 1 else '+',end='')
            else:
                print('.' if row + col + 1 < get_half_size() else '#',end='')
        else:
            if col >= get_half_size():
                print('.'if row + col > get_size() +user_input + 1 else '+',end='')
            else:
                print('+'if row > get_half_size() and row < get_size() -1 and col >= 1 and col < get_half_size() - 1  else '#',end='')
    print()
