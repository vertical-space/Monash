import doctest

def factorial(n):
    '''
    Returns the product of n!, equivalent to:
    
    n*n-1*n-2*n-3...*n-(n-1)
    
    >>> factorial(1)
    1
    >>> factorial(20)
    
    '''
    assert isinstance(n,int)
    assert n > 0
    tally = 1
    while n:
        tally *= n
        n -= 1
    return tally
    
#for i in range(1,10):
#    print i, factorial(i)


def fibonacci(n):
    '''returns the nth value in the fibonacci sequence
    
    F(N) = F(N-1) + F(N-2)
    F(0) = 0, f(1) = 1
    
   
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    3
    >>> fibonacci(4)
    5
    
    '''
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

tests = [
         [0, 0],
         [1, 1],
         [2, 1],
         [3, 2],
         [5, 5],
         ]
for input, expected_result in tests:
    assert fibonacci(input) == expected_result

def base_count(seq,base):
    return seq.count(base)


def gc_content(seq):
    return 1.0*(seq.count("G")+seq.count("C"))/len(seq)*100


print base_count("ATCGCGGGATTCGTATATAGG", "A")
print gc_content("ATCGCGGGATTCGTATATAGG"), "%"

if __name__ == "__main__":
    doctest.testmod()

