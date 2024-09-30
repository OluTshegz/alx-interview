#!/usr/bin/python3
"""
Prime Game - Determines the winner of a prime game
Maria and Ben take turns selecting primes and
their multiples from a list.
The player that cannot make a move loses the game.
"""


def is_prime(n):
    """
    Determines if a number is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime.
    # Check divisibility up to square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # If divisible by any number, it's not prime.
    return True  # If no divisors, it's a prime number.


def prime_count(n):
    """
    Returns the number of prime numbers less than or equal to n using
    the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The number up to which primes are counted.

    Returns:
        int: The number of primes less than or equal to n.
    """
    if n < 2:  # No primes for numbers less than 2
        return 0

    sieve = [True] * (n + 1)  # Initialize sieve array to True
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers.

    # Implement Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):  # Check up to the square root of n
        if sieve[i]:  # If i is a prime
            # Mark multiples of i as non-prime
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False

    # Count the number of primes in the sieve array
    return sum(sieve)


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing
        the upper limit of numbers for each round.

    Returns:
        str or None: The name of the player with
        the most wins ("Maria" or "Ben"),
        or None if there is no winner or invalid input.
    """
    if x <= 0 or not nums:  # Check for invalid input.
        return None  # No valid game can be played.

    # Ensure all values in nums are valid positive integers
    if any(not isinstance(n, int) or n <= 0 for n in nums):
        return None  # Invalid game input, return None.

    maria_wins = 0  # Counter for Maria's wins.
    ben_wins = 0  # Counter for Ben's wins.

    # Find the largest number in nums to optimize prime calculation.
    max_n = max(nums)
    # Precompute prime counts for all numbers up to max_n.
    prime_counts = [prime_count(i) for i in range(max_n + 1)]

    for n in nums:  # Iterate through each round.
        primes = prime_counts[n]  # Get the prime count for the current n.

        # If prime count is odd, Maria wins; if even, Ben wins.
        if primes % 2 == 1:
            maria_wins += 1  # Maria wins this round.
        else:
            ben_wins += 1  # Ben wins this round.

    # Determine the overall winner based on
    # the number of rounds each player won.
    if maria_wins > ben_wins:
        return "Maria"  # Maria wins more rounds.
    elif ben_wins > maria_wins:
        return "Ben"  # Ben wins more rounds.
    else:
        return None  # If tied, return None.


# Test cases
# if __name__ == "__main__":
    # Expected Output: Ben
    # print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
