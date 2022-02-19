import sys
n = sys.stdin.readline()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

go = [(-2,-1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
cnt = 0
for goes in go:
    nrow = row + goes[0]
    ncol = col + goes[1]
    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        cnt += 1

print(cnt)