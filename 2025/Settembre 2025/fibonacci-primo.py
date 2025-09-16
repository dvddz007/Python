def primo(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n < 3:
        return 1

    i = 0
    a = 1
    b = 1
    #   for i in range(1, n-2)
    while i < n - 2:
        c = a + b
        a = b
        b = c

        i += 1
    return c


n = -1
while n <= 0:
    n = int(input("Inserire un numero: "))

i = 1
while fibonacci(i) < n:
    '''if primo(fibonacci(i)):
        print(f"{fibonacci(i)} è primo.")
    else:
        print(f"{fibonacci(i)} non è primo.")'''
    print(f"Il numero {fibonacci(i)} {'non ' if not primo(fibonacci(i)) else ''}è primo.")
    i += 1
