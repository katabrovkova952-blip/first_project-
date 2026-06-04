mountain = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6, 8]
]

for i in range(len(mountain) - 2, -1, -1):
    for j in range(len(mountain[i])):
        mountain[i][j] += max(mountain[i + 1][j], mountain[i + 1][j + 1])

print(mountain[0][0])