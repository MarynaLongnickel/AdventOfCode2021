import regex as re
from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/main/Day22/day22.txt').read().decode()[:-1].split('\n')

d = [i.replace('on', '1').replace('off','0') for i in data[:20]]
d = [[int(n) for n in re.findall(r'-?\d+', i)] for i in d]

dic = {''.join([n.rjust(2, '0') for n in  map(str, [i,j,k])]): 0 for i in range(-50, 51) for j in range(-50, 51) for k in range(-50, 51)}

for r in d:
    for i in range(r[1], r[2] + 1):
        for j in range(r[3], r[4] + 1):
            for k in range(r[5], r[6] + 1):
                n = ''.join([n.rjust(2, '0') for n in  map(str, [i,j,k])])
                dic[n] = 1 if r[0] == 1 else 0
                
sum(dic.values())
