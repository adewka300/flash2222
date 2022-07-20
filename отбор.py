# №1
m1 = [''] + [oct(x)[2:] for x in range(0, 200)]
m2 = [str(x * 2) for x in range(0, 200)]
mas = []

for i in m1:
    for j in m2:
        m = '123#4%5'.replace('#', i).replace('%', j)
        if int(m) < 10 ** 8 and int(m) % 121 == 0:
            mas.append(int(m))

mas = sorted(mas)
for a in mas:
    print(a, a // 121)
          
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
