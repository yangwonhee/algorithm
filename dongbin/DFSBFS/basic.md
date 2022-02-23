# 그래프 탐색 알고리즘: DFS/BFS

- 탐색(search)이란, 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다.
- 대표적인 그래프 탐색 알고리즘으로 DFS, BFS가 있다.
- 코테에서 매우 자주 출제.

## 스택 자료구조

- 먼저 들어 온 데이터가 나중에 나가는 형식의 자료구조. (FILO)
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.

```py
# 삽입(5,2,3,7) 삭제() 삽입(2,4) 삭제()
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(2)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```

## 큐 자료구조

- 먼저 들어 온 데이터가 먼저 나가는 형식의 자료구조 (FIFO)
- 큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화 할 수 있음

```py
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순
print(queue) # 나중에 들어온 원소부터 출력

```

## 재귀 함수

- 재귀 함수(recursive function)란 자기 자신을 다시 호출하는 함수를 의미.
- 단순한 형태의 재귀함수 예제
  > '재귀함수를 호출합니다'라는 문자열을 무한히 출력.
  > 어느 정도 출력하다가 최대 재귀 깊이 초과 메세지가 출력.

```py
def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()

recursive_function()
```

## 재귀 함수의 종료 조건

- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시.
- 종료 조건을 제대로 명시하지 않을 시 함수가 무한 호출 됨.
  > 종료 조건을 포함한 재귀 함수 예제

```py
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
```

## 팩토리얼 구현 예제

- n! = 1 x 2 x 3 x ... x (n-1) x n
- 수학적으로 0!, 1!의 값은 1이다.

```py
def fac_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fac_recursive(n):
    if n <= 1:
        return 1
    return n * fac_recursive(n-1)
```

## 최대공약수 계산 (유클리드 호제법) 예제

- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다.
- 유클리드 호제법

  > 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하면,
  > 이때 A와 B의 최대공약수는 B,R 의 최대공약수와 같다.

- 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있다.

```py
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
print(gcd(192, 162))

>>> 6
```

# 재귀 함수 사용의 유의 사항

- 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
  단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 함.
- 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
- 상황에 따라 재귀함수와 반복문을 적절히 사용해야 함.
- 재귀함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있기 때문.
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
- 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신 재귀함수를 이용하는 경우가 많음.
