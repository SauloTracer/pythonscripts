def isPrime(n):
    if n == 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        d = 5
        while d*d <= n:
            if n % d == 0 or n % (d+2) == 0:
                return False
                break
            d+=6
        else:
            return True
