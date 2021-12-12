from urllib.request import urlopen
import cv2

data = urlopen('https://tinyurl.com/bdcs966s').read().decode().split('\n')[:-1]
d = [list(map(int, i)) for j in data for i in j.split()]

t = 0
m = [[9] + i + [9] for i in [[9] * len(d[0])] + d + [[9] * len(d[0])]]

for r in range(1, len(m) - 1):
    for c in range(1, len(m[0]) - 1):
        if m[r][c] < min([m[r][c-1], m[r-1][c], m[r][c+1], m[r+1][c]]):
            t += m[r][c] + 1

# -------------------------------------------------- Part 2 ------------------------------------------------------

d = [list(map(int, list(s))) for s in data]
a = np.where(np.array(d) < 9, 255, 0).astype(np.uint8)
_, _, stats, _ = cv2.connectedComponentsWithStats(a, connectivity=4)

n = sorted([i[-1] for i in stats[1:]])[-3:]

n[0] * n[1] * n[2]
