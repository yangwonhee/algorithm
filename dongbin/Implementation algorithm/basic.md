# 구현(implementation)

- 구현이란, 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다. (problem -> thinking -> solution)

- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다.

```py
# 동,북,서,남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
```
