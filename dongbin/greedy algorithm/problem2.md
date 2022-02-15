# <문제> 곱하기 혹은 더하기: 문제 설명

- 각 자리가 숫자(0~9)로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' or '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
- 예를 들어, 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0+2)x9)x8)x4) = 576입니다. 또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

입력 조건: 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 s가 주어집니다.
출력 조건: 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

입력예시1: 02984
출력예시1: 576

입력예시2: 567
출력예시2: 210

```py
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
```

```c++
#include <bits/stdc++.h>
using namespace std;
string str;
int main(void){
    cin >> str;
    long long result = str[0] - '0';

    for (int i = 1; i < str.size(); i++){
        int num = str[i] - '0';
        if (num <= 1 || result <= 1) result += num;
        else result *= num;
    }
    cout << result << '\n';
}
```

```java
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
    }

    long result = str.charAt(0) - '0';
    for (int i = 1; i < str.length(); i++){
        int num = str.charAt(i) - '0';
        if (num <= 1 || result <= 1){
            result += num;
        }
        else {
            result *= num;
        }
    }
    System.out.println(result);
}
```
