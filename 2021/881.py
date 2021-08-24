# Incomplete

# Implement a 2D iterator class. It will be initialized with an array of arrays,
# and should implement the following methods:
#
# next(): returns the next element in the array of arrays. If there are no more
# elements, raise an exception.
#
# has_next(): returns whether or not the iterator still has elements left.
#
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
# repeatedly should output 1, 2, 3, 4, 5, 6.

class Iterator(object):
    """docstring for Iterator."""

    def __init__(self, arg):
        super(Iterator, self).__init__()
        self.arg = arg

        self.i = self.j = None

    def __is_empty(self, i, j):
        if self.arg[i]:
            if self.arg[i][j]:
                return False

        return True

    def __exists(self, i, j):
        if i < len(self.arg) and j < len(self.arg[i]):
            return True

        return False

    def next(self):
        # Object is not null
        if not self.arg:
            raise Exception

        # Initial next call
        if self.i is None:
            self.i = self.j = 0

            if self.__exists(self.i, self.j) and not self.__is_empty(self.i, self.j):
                return self.arg[self.i][self.j]
            else:
                return self.next()

        # Consecutive calls
        # Is next an option ? If not raise an exception
        if not self.has_next():
            raise Exception

        if self.__exists(self.i, self.j + 1):
            self.j += 1
        else:
            self.i += 1

            self.j = 0

        if self.__is_empty(self.i, self.j):
            return self.next()
        else:
            return self.arg[self.i][self.j]

    def has_next(self):
        if self.__exists(self.i, self.j + 1) or self.__exists(self.i + 1, 0):
            return True
        return False

if __name__ == '__main__':
    testIterator = Iterator([[1, 2], [3], [], [4, 5, 6]])

    for i in range(8):
        print(testIterator.next())
