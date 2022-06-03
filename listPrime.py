def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def listprime(n):
    numbers_perline = 0
    for p in range(n):
        if isprime(p):
            numbers_perline += 1
            if numbers_perline % 10 == 0:
                print(p)
            else:
                print(p, end= " ")
    #print(p)
listprime(60)