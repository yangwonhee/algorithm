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
- 
