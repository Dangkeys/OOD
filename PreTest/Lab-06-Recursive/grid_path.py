def grid_path(n,m):
    if n <= 1 or m <= 1:
        return 1
    return grid_path(n-1,m) + grid_path(n, m- 1)
print(grid_path(3,2))