def fisbass(n):
    if not isinstance(n,int):
        raise TypeError()
    if n%15 == 0:
        return "fizzbuzz"
    if n%3 == 0:
        return "fizz"
    if n%5 == 0:
        return "buzz"
    return str(n)