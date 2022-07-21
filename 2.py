# №2
for i in range(8_666_266_66, 8_666_333_33 + 1):
    divs = set()
    if str(i).count('0') == 0:
        for d in range(2, int(i ** 0.5) + 1):
            if i % d == 0:
                divs.add(d)
                divs.add(i // d)
        if len(divs) == 222:
            print(i)
