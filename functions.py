import math
from math import factorial as fct


def combinations(k, n):
    return fct(n) / (fct(k) * fct(n - k))


def probability(m, n):
    return m / n


def bernulli(p, k, n):
    return combinations(k, n) * p ** k * (1 - p) ** (n - k)


def puasson(p, m, n):
    return math.e ** (-p * n) * (p * n) ** m / fct(m)



