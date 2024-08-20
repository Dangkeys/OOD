def is_palindrome(user_input):
    if user_input == '':
        return True
    elif user_input[0] != user_input[-1]:
        return False
    return is_palindrome(user_input[1:-1])

user_input = input('Enter Input : ')
print(f"'{user_input}' is {'not ' if not is_palindrome(user_input)else ''}palindrome")