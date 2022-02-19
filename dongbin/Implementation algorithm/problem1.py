import sys

n = int(sys.stdin.readline())
move = list(map(str, sys.stdin.readline().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_list = ['L', 'R', 'U', 'D']

for i in move:
    for j in range(len(move_list)):
        if i == move_list[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)