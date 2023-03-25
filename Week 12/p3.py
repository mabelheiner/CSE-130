def find_primes(limit):
    # Create a list of numbers from 2 to the limit
    numbers = [n for n in range(2, limit+1)]
    primes = []
    
    while numbers:
        # Get the first number in the list and add it to the primes list
        prime = numbers.pop(0)
        primes.append(prime)
        
        # Remove all multiples of the prime from the list using only addition and subtraction
        multiples = [n for n in range(prime*2, limit+1, prime)]
        for multiple in multiples:
            while multiple in numbers:
                numbers.remove(multiple)
    
    return primes

# Example usage
limit = 99
primes = find_primes(limit)
print(primes)
