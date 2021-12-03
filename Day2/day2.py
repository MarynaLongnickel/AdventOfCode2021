from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/master/Day2/day2.txt').read().decode().split('\n')[:-1]

f = 0
d = 0

for i in [x.split() for x in data]:
    if i[0] == 'forward': f += int(i[1])
    elif i[0] == 'down': d += int(i[1])
    else: d -= int(i[1])
      
# -------------------------------------------------- Part 2 ------------------------------------------------------


f = 0
d = 0
a = 0

for i in [x.split() for x in data]:
    z = int(i[1])
    if i[0] == 'forward':
        f += z
        d += a*z
    elif i[0] == 'down': a += z
    else: a -= z
