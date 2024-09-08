def sum(n,m):
    if n == 0:
        return 1
    if m == 0 or n < 0:
        return 0
    return sum(n-m,m) + sum(n, m-1)