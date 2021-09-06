# Given an array of non-negative integer, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Determine if you are able to reach the last index

def jump(arr):
    goal = len(arr) - 1

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] + i >= goal:
            goal = i

    return goal == 0

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]

    print("Can we reach the end?:", jump(nums))