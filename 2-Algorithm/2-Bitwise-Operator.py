a = 10  # 1010
b = 4   # 0100

print("a & b: ", a & b)  # AND
print("a | b: ", a & b)  # OR
print("~a = ", ~a)       # NOT
print("a ^ b: ", a ^ b)  # XOR

print("a >> 1 = ", a >> 1)  # Right shift operator
print("a << 1 = ", a << 1)  # Left shift operator

# Check even or odd
def isEven(n):
    if (n | 1 > n):
        return True
    else:
        return False


if __name__ == "__main__":
    x = 100
    print("Is Even: ", isEven(x))
