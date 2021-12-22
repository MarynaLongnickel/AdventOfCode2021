p1 = 2
p2 = 7

t1 = 0
t2 = 0

d = 100

i = 1
r = 1

while (t1 < 1000) and (t2 < 1000):
    if r%2:
        p1 = (p1 + (3*i + 3))%10
        if p1 == 0: p1 = 10
        t1 += p1
        if t1 >= 1000:
            print(t1, t2, 3*r, t2 * 3 * r)
            break
    else:
        p2 = (p2 + (3*i + 3))%10
        if p2 == 0: p2 = 10
        t2 += p2
        if t2 >= 1000:
            print(t1, t2, 3*r, t1 * 3 * r)
            break
    i += 3
    if i > d:
        i = i%d
    r += 1
