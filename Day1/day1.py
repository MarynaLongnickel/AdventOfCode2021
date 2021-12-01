from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2021/master/Day1/day1.txt').read().decode().split('\n')[:-1]

sum([int(y) > int(x) for x, y in zip(data, data[1:])])
