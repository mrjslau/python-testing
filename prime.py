import random as rand

def is_a_prime(num):
    """Print if a given number 'num' is a prime number or not
    >>> is_a_prime(1)
    1 is not a prime number
    >>> is_a_prime(14)
    14 is not a prime number
    2 times 7 is 14
    (2, 7)
    >>> is_a_prime(1124321)
    1124321 is not a prime number
    11 times 102211 is 1124321
    (11, 102211)
    >>> is_a_prime(5.5)
    Traceback (most recent call last):
      ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> is_a_prime(113)
    113 is a prime number
    113
    >>> is_a_prime(2)
    2 is a prime number
    2
    """
    if num > 1:
       # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num//i, "is", num)
                return (i, num//i)
        else:
            print(num, "is a prime number")
            return num
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")

if __name__=="__main__":
    import doctest
    doctest.testmod()
