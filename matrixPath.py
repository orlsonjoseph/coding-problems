# There is an N by M matrix of zeroes. Given N and M, write a function to
# count the number of ways of starting at the top-left corner and getting
# to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are
# two ways to get to the bottom-right:

# Right, then down
# Down, then right

# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

def numberOfPaths(n, m):
    arr = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        arr[i][0] = 1

    for j in range(m):
        arr[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    return arr[n - 1][m - 1]

if __name__ == '__main__':
    n = 5
    m = 5

    print("Number of paths to last cell:", numberOfPaths(n, m))

