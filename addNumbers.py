# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their
# nodes contains a single digit. Add the two numbers and return the sum
# as a linked list.

# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

class ListNode(object):
    def __init__(self, x = 0):
        self.val = x

        self.next = None

def add(x, y):
    head = current = ListNode()
    carry = sum = 0

    while x or y or carry:
        if (not x or not y) and not carry:
            current.next = x or y
            break

        sum = carry

        if x:
            sum += x.val
            x = x.next

        if y:
            sum += y.val
            y = y.next

        
        carry = sum / 10

        current.next = ListNode(sum % 10)
        current = current.next

    return head.next

if __name__ == "__main__":
    pass