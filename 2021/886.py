# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the
# other. For example, the edit distance between “kitten” and “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
#
# Given two strings, compute the edit distance between them.

# Edit distance between a, b with m, n being the length of those strings
# respectively

# Levenshtein distance

def dist(a, m, b, n):
    # base case: empty strings
    if m == 0:
        return n

    if n == 0:
        return m

    # if the last characters of the strings match
    cost = 0 if (a[m - 1] == b[n - 1]) else 1

    return min(dist(a, m - 1, b, n) + 1, # deletion
        dist(a, m, b, n - 1) + 1, # insertion
        dist(a, m - 1, b, n - 1) + cost) # substitution

if __name__ == '__main__':
    a = "kitten"
    b = "sitting"

    print("The edit distance is", dist(a, len(a), b, len(b)))
