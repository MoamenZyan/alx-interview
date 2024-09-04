#!/usr/bin/python3
"""My script"""


def isWinner(x, nums):
    """Prime game"""
    mariaCount = 0
    benCount = 0

    for num in nums:
        rounds = list(range(1, num + 1))
        primes = primesInRange(1, num)

        if not primes:
            benCount += 1
            continue

        mariaTurn = True

        while(True):
            if not primes:
                if mariaTurn:
                    benCount += 1
                else:
                    mariaCount += 1
                break

            smallPrime = primes.pop(0)
            rounds.remove(smallPrime)

            rounds = [x for x in rounds if x % smallPrime != 0]

            mariaTurn = not mariaTurn

    if mariaCount > benCount:
        return "Winner: Maria"

    if mariaCount < benCount:
        return "Winner: Ben"

    return None


def isPrime(num):
    """Returns rue if num is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primesInRange(start, end):
    """Returns prime numbers."""
    primeNumbers = [n for n in range(start, end+1) if isPrime(n)]
    return primeNumbers
