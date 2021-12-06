from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/main/Day6/day6.txt').read().decode().split('\n')[:-1]
data = list(map(int, data[0].split(',')))


d = [data.count(i) for i in range(9)]

for i in range(256):
    d.append(0 if d[0] == 0 else d[0])
    n = d.pop(0)
    d[6] += n
    
print(sum(d))
