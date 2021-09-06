# Given an array of integers nums containing n + 1 integers
# where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this
# repeated number.

# You must solve the problem without modifying the array
# nums and uses only constant extra space.

def find(arr):
    tortoise = hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]

        if tortoise == hare:
            break
    
    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return hare

if __name__ == "__main__":
    # arr = [3, 1, 3, 4, 2]
    arr = [1, 4, 3, 2, 2]

    print("In", arr, find(arr), "is a duplicate")
