import math


def repeatedString(s, n):
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


s = "aba"
n = 10

print(repeatedString(s, n))
