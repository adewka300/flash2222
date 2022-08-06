# №3
def f(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

for i in range(19210100, 19225525 + 1):
    divs = set()
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            if f(d):
                divs.add(d)
            if f(i // d):
                divs.add(i // d)
    if len(divs) > 0 and len(divs) % 22 == 0:
        print(i, max(divs))
