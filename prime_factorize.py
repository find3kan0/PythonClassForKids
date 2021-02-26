primes = set()
non_primes = set()

def is_prime(n):
  '''Given a number n, find if it is a prime number'''
  if n in primes:
    return True
  if n in non_primes:
    return False
  i = 2
  while(i <= n/2):
    if n%i ==0:
      non_primes.add(n)
      return False
    i = i+1
  primes.add(n)
  return True

def next_prime(n):
  '''Given a number n, find the next nearest prime number'''
  while True:
    n += 1
    if(is_prime(n)):
      return n

def find_prime_factors(n):
  '''Given a number n, return a list that contains all the prime factors of n'''
  result = []
  i = 2
  while(n!=0 and n!=1):
    if n%i == 0:
      n = n/i
      result.append(i)
    else:
      i = next_prime(i) 
  return result

if __name__ == "__main__":
  for i in range(1000):
    print("{} = {}".format(i, " * ".join(str(x) for x in find_prime_factors(i))))