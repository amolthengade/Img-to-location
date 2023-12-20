# Example 1: Nested Loop for a 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Example 1:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Example 2: Nested Loop for Multiplication Table
print("\nExample 2:")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
