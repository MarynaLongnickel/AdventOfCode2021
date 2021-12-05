from urllib.request import urlopen
    
data = urlopen('https://tinyurl.com/tuab7fz4').read().decode().split('\n')[:-1]
    
nums = data[0].split(',')
data = [x.split() for x in data[1:] if x]
    
boards1 = [list(data[i:i+5]) for i in range(0, len(data), 5)]
boards2 = [list(zip(*x)) for x in boards1]
    
d = {i : [len(nums), 0] for i in range(len(boards1))}

for board in [boards1, boards2]:
    for b in board:
        for row in b:
            if all(x in nums for x in row):
                m = max([nums.index(x) for x in row])
                i = board.index(b)
                if m < d[i][0]:
                    d[i] = [m, b]
    
n = min(d.values())

int(nums[n[0]])*sum(map(int, list(set([i for r in n[1] for i in r]) - set(nums[:n[0]+1]))))


# -------------------------------------------------- Part 2 ------------------------------------------------------


n = max(d.values())

int(nums[n[0]])*sum(map(int, list(set([i for r in n[1] for i in r]) - set(nums[:n[0]+1]))))
