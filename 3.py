# №3
for i in range(300_000, 500_000 + 1):
    divs = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if str(j) == str(j)[::-1]:
                divs.add(j)
            if str(i // j) == str(i // j)[::-1]:
                divs.add(i // j)
    if len(divs) >= 30:
        print(min(divs) + max(divs))
