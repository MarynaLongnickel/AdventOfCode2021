from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/master/Day1/day1.txt').read().decode().split('\n')[:-1]
data = [int(x) for x in data]

sum([y - x for x, y in zip(data, data[1:])])

# -------------------------------------------------- Part 2 --------------------------------------------------------

t = 0

for i in range(1, len(data) - 2):
    t += sum(data[i : i + 3]) > sum(data[i - 1 : i + 2])
    
t
