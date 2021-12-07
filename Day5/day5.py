from urllib.request import urlopen

data = urlopen('https://tinyurl.com/yckkb8mx').read().decode().split('\n')[:-1]

data = [[list(map(int, c.split(','))) for c in x.split(' -> ')] for x in data]
lines = [x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]]

d = {(i, j) : 0 for i in range(1000) for j in range(1000)}

for p in data:
    x1, y1 = p[0]
    x2, y2 = p[1]
    if x1 == x2:
        l = list(zip([x1] * (abs(y1 - y2) + 1), range(min(y1, y2), max(y1, y2) + 1)))
    elif y1 == y2:
        l = list(zip(range(min(x1, x2), max(x1, x2) + 1), [y1] * (abs(x1 - x2) + 1)))
    else:
        s = 1 if x1 < x2 else -1
        t = 1 if y1 < y2 else -1
        l = [(x1 + i * s, y1 + i * t) for i in range(abs(x1 - x2) + 1)]
    for i in l:
        d[i] += 1
        
len([i for i in d.values() if i > 1])
