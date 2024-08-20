def staircase(n, current_step = 1):
    if n == 0:
        return 'Not Draw!'
    elif current_step > abs(n):
        return ''
    return f"{'_'*(n-current_step)}{'#'*current_step}\n{staircase(n, current_step+1)}" if n > 0 else f"{'_'*(current_step -1)}{'#'*(abs(n) - current_step + 1)}\n{staircase(n, current_step+1)}" 

# Example usage:
n = int(input("Enter Input : "))
print(staircase(n))
