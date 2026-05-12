def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def compareTo(s1, s2):
    if s1 == "" and s2 == "":
        return 0

    if s1 == "":
        return -1

    if s2 == "":
        return 1

    if s1[0] < s2[0]:
        return -1

    if s1[0] > s2[0]:
        return 1

    return compareTo(s1[1:], s2[1:])

def main():
    print(fibonacci(7))
    print(gcd(300, 60))
    print(compareTo("wall", "walk"))

if __name__ == "__main__":
    main()