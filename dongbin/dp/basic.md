# 다이나믹 프로그래밍
- 다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법.
- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함.
- 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운 & 보텀업)으로 구성 됨.
  
- 다이나믹 프로그래밍 == 동적 계획법
- 일반적인 프로그래밍 분야에서 동적 이란?
    - 자료구조에서 동적 할당(dynamic allocation)은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'
    

- 다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용 가능
1. 최적 부분 구조 (optimal substructure)
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
2. 중복되는 부분 문제 (overlapping subproblem)
    - 동일한 작은 문제를 반복적으로 해결해야 함.

```py
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(4))
```


```cpp
#include <bits/stdc++.h>
using namespace std;
int fibo(int x){
    if (x == 1 || x == 2){
        return 1;
    }
    return fibo(x-1) + fibo(x- 2);
}
int main(){
    cout << fibo(4) << '\n';
    return 0;
}
```

```java
import java.util.*;

public clas Main{
    public static int fibo(int x){
        if (x == 1 || x == 2){
            return 1;
        }
        return fibo(x - 1) + fibo(x - 2);
    }
    public static void main(String[] args){
        System.out.println(fibo(4));
    }
}
```

## 피보나치 수열의 시간 복잡도 분석
- 단순 재귀함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 된다.
- 작은 값이 여러 번 호출 되며 계산이 중복된다.
- 피보나치 수열의 시간 복잡도는 다음과 같다.
  - 빅오 표기법 : O(2^n)
- 빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억가량의 연산을 수행해야 함.
- 그렇다면 f(100)을 계산하기 위해서는 얼마나 많은 연산을 수행해야 할까?


## 피보나치 수열의 효율적인 해법: 다이나믹 프로그래밍
- 다이나믹 프로그래밍의 사용 *조건*을 만족하는지 확인합니다.
	1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있음.
	2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결.
- 피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족함.



## 메모이제이션 (Memoization)
- 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나.
- 한 번 계산한 결과를 메모리 공간에 메모하는 기법
	- 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴.
	- 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 함.


## top down VS bottom up
- 탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고도 한다.
- 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다.
    - 결과 저장용 리스트는 DP table이라고 부름
- 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념.
    - 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아님.
    - 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음


## 피보나치 수열: 탑다운 다이나믹 프로그래밍 소스코드
> 재귀함수

```py
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
```

## 피보나치 수열: 보텀업 다이나믹 프로그래밍 소스코드
> 반복문

```py
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
```

```cpp
#include <bits/stdc++.h>
using namespace std;
long long d[100];
int main(){
    d[1] = 1;
    d[2] = 1;
    int n = 50;
    // cpp 에서 99번째는 overflow 발생
    for (int i = 3; i <= n; i++){
        d[i] = d[i-1] + d[i-2];
    }
    cout << d[n] << '\n';
    return 0;
}
```

```java
import java.util.*;
public class Main{
    public static long[] d = new long[100];
    public static void main(String[] args){
        d[1] = 1;
        d[2] = 1;
        int n= 50;
        for(int i = 3; i <= n; i++){
            d[i] = d[i-1] + d[i-2];
        }
        System.out.println(d[n]);
    }
}
```


## 피보나치 수열: 메모이제이션 동작 분석
- 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(N)이다.
```py
d = [0] * 100
def fibo(x):
    print('f('+ str(x)+ ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]
fibo(6)

>>> f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) 
```