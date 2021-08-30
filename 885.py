# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and the
# Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

# Bubble sort ? (not sure because of linear time requirement)
v = {'R' : 0, 'G' : 1, 'B' : 2}

def bubble(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if v[arr[j]] > v[arr[j+1]]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == '__main__':
    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

    print("The sorted output is", bubble(arr))
