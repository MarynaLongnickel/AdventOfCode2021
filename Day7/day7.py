from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/main/Day7/day7.txt').read().decode().split('\n')[:-1]
data = sorted(map(int, data[0].split(',')))

p = list(set(data))
m = data[int(len(data) / 2)]

t = sum([abs(x - m) for x in data])

for i in range(m + 1, 1000):
    s = sum([abs(x - p[i]) for x in data])
    if s > t: break
    else: t = s
        
for i in range(m - 1, 0, -1):
    s = sum([abs(x - p[i])  for x in data])
    if s > t: break
    else: t = s
        
t

# -------------------------------------------------- Part 2 ------------------------------------------------------

t = sum([abs(x - m) * (abs(x - m) + 1) / 2 for x in data])

for i in range(m + 1, 1000):
    s = sum([abs(x - p[i]) * (abs(x - p[i]) + 1) / 2 for x in data])
    if s > t: break
    else: t = s
        
for i in range(m - 1, 0, -1):
    s = sum([abs(x - p[i]) * (abs(x - p[i]) + 1) / 2  for x in data])
    if s > t: break
    else: t = s
        
t
