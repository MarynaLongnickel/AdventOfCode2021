from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/master/Day3/day3.txt').read().decode().split('\n')[:-1]

l = list(zip(*[[int(i) for i in x] for x in data]))

a = int(''.join(['1' if sum(x) > len(x)/2 else '0' for x in l]), 2)
b = int(''.join(['0' if sum(x) > len(x)/2 else '1' for x in l]), 2)
a*b

# -------------------------------------------------- Part 2 ------------------------------------------------------

a = 1

for n in [0, 1]:
    d = [[int(i) for i in x] for x in data]
    for i in range(12):
        if len(d) < 2:
            break
        else:
            s = n%2 if sum([x[i] for x in d]) >= len(d) / 2 else (n+1)%2
        d = [x for x in d if x[i] == s]
    a *= int(''.join(map(str, d[0])), 2)
a
