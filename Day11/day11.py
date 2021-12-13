from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/main/Day11/day11.txt').read().decode().split('\n')[:-1]

d = [list(map(int, i)) for i in data]
f = 0

for i in range(1000):
    if max([x for y in d for x in y]) == 0:
        print('step: ', i)
        break
        
    for r in range(len(d)):
        for c in range(len(d[0])):
            d[r][c] += 1

    while max([x for y in d for x in y]) > 9:
        for r2 in range(len(d)):
            for c2 in range(len(d[0])):
                if d[r2][c2] > 9:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if i == 0 and j == 0:
                                d[r2][c2] = 0
                                f += 1
                            elif (0 <= r2+i < len(d)) and (0 <= c2+j < len(d[0])) and d[r2+i][c2+j] != 0:
                                d[r2+i][c2+j] += 1
                            else:
                                continue
f
