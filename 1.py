# №1
def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

for i in range(300, 500 + 1):
    primed = set()
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            if f(d):
                primed.add(d)
            if f(i // d):
                primed.add(i // d)
    if len(primed) == 4:
        print(i, max(primed))
