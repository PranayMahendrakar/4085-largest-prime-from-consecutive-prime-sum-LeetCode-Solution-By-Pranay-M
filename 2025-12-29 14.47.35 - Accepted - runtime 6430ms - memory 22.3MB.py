class Solution:
    def largestPrime(self, n: int) -> int:
        # Sieve of Eratosthenes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False
        
        # Get list of primes <= n
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        
        if not primes:
            return 0
        
        # Find all consecutive prime sums STARTING FROM 2 that are prime and <= n
        result = 0
        current_sum = 0
        
        for p in primes:
            current_sum += p
            if current_sum > n:
                break
            if is_prime[current_sum]:
                result = current_sum
        
        return result