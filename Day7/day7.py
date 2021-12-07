from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/main/Day7/day7.txt').read().decode().split('\n')[:-1]
data = sorted(map(int, data[0].split(',')))

def s1(i): return sum([abs(x - i) for x in data])
def s2(i): return sum([abs(x - i) * (abs(x - i) + 1) / 2 for x in data])

p = list(set(data))
m = data[int(len(data) / 2)]

def f(s):
    t = s(m)
    for i in range(m + 1, 1000):
       x = s(p[i])
        if x > t: break
        else: t = x
    
    for i in range(m - 1, 0, -1):
        x = s(p[i])
        if x > t: break
        else: t = x
    
    return t

f(s1)

# -------------------------------------------------- Part 2 ------------------------------------------------------

f(s2)
