# Define the matrices
B_matrices = [
    [[3, -1, -1], [-4, 9, 1], [-1, 0, 1]],
    [[2, 1, 2], [1, -9, 1], [2, 3, 2]],
    [[-3, 0, 3], [0, 3, 0], [-3, 0, 3]],
    [[4, 1, -6], [-4, -7, 3], [1, -7, -4]],
    [[2, -1, 0], [-1, 2, -1], [0, -1, 1]]
]

# Function to multiply two 3x3 matrices
def multiply_matrices(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0] + A[0][2] * B[2][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1] + A[0][2] * B[2][1],
            A[0][0] * B[0][2] + A[0][1] * B[1][2] + A[0][2] * B[2][2]
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0] + A[1][2] * B[2][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1] + A[1][2] * B[2][1],
            A[1][0] * B[0][2] + A[1][1] * B[1][2] + A[1][2] * B[2][2]
        ],
        [
            A[2][0] * B[0][0] + A[2][1] * B[1][0] + A[2][2] * B[2][0],
            A[2][0] * B[0][1] + A[2][1] * B[1][1] + A[2][2] * B[2][1],
            A[2][0] * B[0][2] + A[2][1] * B[1][2] + A[2][2] * B[2][2]
        ]
    ]

# Function to check if two 3x3 matrices are equal
def are_matrices_equal(A, B):
    for i in range(3):
        for j in range(3):
            if A[i][j] != B[i][j]:
                return False
    return True

# Initialize an empty list to hold the results
commuting_B_pairs = []

# Check if B_i * B_j == B_j * B_i for each pair of matrices
for i in range(len(B_matrices)):
    for j in range(len(B_matrices)):
        if i != j:
            B_i = B_matrices[i]
            B_j = B_matrices[j]
            B_iB_j = multiply_matrices(B_i, B_j)
            B_jB_i = multiply_matrices(B_j, B_i)
            if are_matrices_equal(B_iB_j, B_jB_i):
                commuting_B_pairs.append((i + 1, j + 1))

print(commuting_B_pairs)
