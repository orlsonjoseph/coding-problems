# Given a list of numbers and a number k, return whether any two numbers fro
# the list add up to k.

def add_up_to(k, numbers):
    for a in range(len(numbers)):
        for b in range(len(numbers)):
            if a == b:
                pass
            else:
                if numbers[a] + numbers[b] == k:
                    return True

    return False

def add_up_to_optimized(k, numbers):
    numbers.sort()

    start = 0
    end = len(numbers) - 1

    while start != end:
        sum = numbers[start] + numbers[end]

        if sum == k: return True

        if sum < k: start += 1
        else: end -= 1

    return False


if __name__ == '__main__':
    add_up_to(17, [10, 15, 3, 7])

    add_up_to_optimized(17, [10, 15, 3, 7])
