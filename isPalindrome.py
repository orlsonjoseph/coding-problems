# Write a program that checks whether an integer is a palindrome. For
# example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
# Do not convert the integer into a string.

def is_palindrome(n):
    x, y = n, 0
    f = lambda: (y * 10) + x % 10
    while x > 0:
        x, y = x//10 , f()
    return y == n

if __name__ == '__main__':
    n = 8887

    assert is_palindrome(n) == False