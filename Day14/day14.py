from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/main/Day14/day14.txt').read().decode().split('\n')[:-1]

s = data[0]
d = {i[:2] : i[-1] for i in data[2:]}

c = {k: s.count(k) for k in d.keys()}

for i in range(40):
    c2 = c.copy()
    for k, v in c.items():
        if c[k] > 0 :
            c2[k] -= v
            c2[k[0] + d[k]] += v
            c2[d[k] + k[1]] += v
    c = c2

l = {x: 0 for x in set(''.join(c.keys()))}

for k, v in c.items():
    l[k[0]] += v/2
    l[k[1]] += v/2

int(max(l.values()) - min(l.values()))
