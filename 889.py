# Run-length encoding is a fast and simple method of encoding strings. The basic
# idea is to represent repeated successive characters as a single count and
# character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

def encode(m):
    p = None
    c = 0
    o = []

    for x in m:
        if p == None:
            p = x
        elif p != x:
            o.append(str(c) + p)
            c = 0
            p = x
        c += 1

    # last letter
    o.append(str(c) + p)
    return o

def decode(m):
    o = []
    chunks = [m[i:i+2] for i in range(0, len(m), 1)]

    for c in chunks:
        n, l = c[0]

        o.append(int(n) * l)

    return "".join(o)

if __name__ == '__main__':
    a = "AAAABBBCCDAA"
    b = encode(a)
    c = decode(b)

    print("Original", a, "\nEncoded", b, "\nDecoded", c)
