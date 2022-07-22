m1 = [''] + [oct(x)[2:] for x in range(0, 200)]
m2 = ['0' + str(x) for x in range(0, 100)] + \
     [str(x) for x in range(0, 1000)]
mas = []

for i in m1:
    for j in m2:
        m = '123#4%5'.replace('#', i).replace('%', j)
        if int(m) < 10 ** 8 and int(m) % 333 == 0:
            mas.append(int(m))

mas = sorted(mas)
for a in mas:
    print(a, a // 333)
