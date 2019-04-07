all_known_primes = set()

def primeFactors(n, max_prime_size):
    factors = []
    if n == 0:
        return factors
    if n == 1:
        return [1,1]

    while n % 2 == 0: 
        factors.append(2) 
        n = n / 2

    for prime in all_known_primes:
        if n % prime== 0: 
            factors.append(int(prime))
            other_prime = int(n / prime)
            factors.append(other_prime)
            if other_prime > 2:
                all_known_primes.add(other_prime)
            return factors

    for i in range(3,max_prime_size*2,2):
        if i in all_known_primes:
            continue
        if n % i== 0: 
            factors.append(int(i))
            other_prime = int(n/i)
            factors.append(other_prime)
            if i > 2:
                all_known_primes.add(i)
            if other_prime > 2:
                all_known_primes.add(other_prime)
            return factors

def build_seq_of_primes(inputs, max_prime_size, length_of_input):
    input_length = length_of_input
    primes_sets = []
    
    for num in inputs.split(" "):
        factors = primeFactors(int(num), max_prime_size)
        primes_sets.append(factors)

    prime_seq = []
    i = len(primes_sets)-1
    while i > 0:
        j = i-1
        current_set = primes_sets[i]
        prev_set = primes_sets[j]
        intersection_set = [value for value in current_set if value in prev_set]
        intersection_set_prime = [value for value in current_set if value not in intersection_set]
        while len(intersection_set) != 1 and j-1>0:
            j -= 1
            current_set = intersection_set
            prev_set = primes_sets[j]
            intersection_set = [value for value in current_set if value in prev_set]
            intersection_set_prime = [value for value in current_set if value not in intersection_set]
        if i == len(primes_sets)-1:
            prime_seq.append(intersection_set_prime[0])
        prime_seq.append(intersection_set[0])
        i-=1
    #0 case 

    print(prime_seq)
    return []

def remove_duplicates_and_sort(original_list):
    hashset = list(dict.fromkeys(original_list))
    hashset.sort()
    return hashset

def build_key(sorted_primes):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = dict(zip(sorted_primes, alphabets))
    return key

cases = int(input())
for case in range(1, cases + 1):
    max_prime_size, length_of_input = [int(s) for s in input().split(" ")]
    inputs = input()
    prime_inputs = build_seq_of_primes(inputs, max_prime_size, length_of_input)
    key = build_key(remove_duplicates_and_sort(prime_inputs))
    decoded_string = ""

    for prime in prime_inputs:
        decoded_string += key[prime]
    print("Case #{}: {}".format(case, decoded_string))