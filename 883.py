# Given a positive integer N, find the smallest number of steps it will take to
# reach 1.
#
# There are two kinds of permitted steps:
#
# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route:
# 100 -> 10 -> 9 -> 3 -> 2 -> 1.

def divisor(n):
    o = []
    for i in range(1, n + 1):
        if n % i == 0:
            o.append(i)

    m = len(o) // 2
    return o[m]

def steps(n):

    # Base case
    if n == 1:
        return [n]

    dv = divisor(n)
    next = steps(n - 1)

    if dv != n:
        next_p = steps(dv)
        if len(next) > len(next_p):
            next = next_p

    return [n] + next

if __name__ == '__main__':
    n = 100

    print("The steps from ", n, "to 1 is", steps(n))

    # Tests
    assert steps(100) == [100, 10, 9, 3, 2, 1]
    assert steps(50) == [50, 10, 9, 3, 2, 1]
    assert steps(64) == [64, 8, 4, 2, 1]
    assert steps(31) == [31, 30, 6, 3, 2, 1]
