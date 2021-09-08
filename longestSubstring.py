# Given a string s, find the length of the longest substring without
# repeating characters.

def find(s):
    m = l = 0
    lib = {}

    for i, c in enumerate(s):
        if c in lib:
            l = lib[c] + 1
        else:
            lib[c] = i
        m = max(m, i - l + 1)
    return m

if __name__ == "__main__":
    s = "abcabcbb"

    print("Longest substring of %s without repeating characters is of length %d" % (s, find(s)))