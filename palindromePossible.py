# Given a string, determine whether any permutation of it is a palindrome.
#
# For example, carrace should return true, since it can be rearranged to form
# racecar, which is a palindrome. daily should return false, since there's no
# rearrangement that can form a palindrome.

def check(s):
    l = list(s)
    
    if len([x for x in l if l.count(x) < 2]) < 2:
        return True
    return False

if __name__ == '__main__':
    s = "carrace"

    print("Can the string", s, "be rearranged into a palindrome? :", check(s))
