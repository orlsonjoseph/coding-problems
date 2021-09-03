# Given an N by N matrix, rotate it by 90 degrees clockwise.

def rotate(m):
    n = len(m)

    # Rows into columns
    for i in range(n):
        for j in range(i, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    # Move columns
    for i in range(n):
        for j in range(n // 2):
            m[i][j], m[i][n - j - 1] = m[i][n - j - 1], m[i][j]

    return m

if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    m = rotate(m)

    n = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
        ]

    assert n == m
