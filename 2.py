# №2
c = 0
for i in range(400_001, 10 ** 7):
    divs = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            divs.add(j)
            divs.add(i // j)
            if len(divs) > 2:
                break
    if len(divs) == 2:
        if max(divs) % min(divs) == 0:
            print(min(divs), max(divs))
            c += 1
            if c == 5:
                break
