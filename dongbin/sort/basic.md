# 정렬 알고리즘
- 정렬(sorting)이란, 데이터를 특정한 기준에 따라 순서대로 나열하는 것.
- 일반적으로 문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용 됨.

## 선택 정렬
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복.

```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap
print(array)
```

```cpp
#include <bits/stdc++.h>

using namespace std;

int n = 10;
int target[10] = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

int main(void) {
    for(int i = 0; i < n; i++){
        int min_index = i;
        for(int j = i+1; j < n; j++){
            if(target[min_index] > target[j]){
                min_index = j;
            }
        }
        swap(target[i], target[min_index]);
    }
    for(int i = 0; i < n; i++){
        cout << target[i] << ' ';
    }
    return 0;
}
```

```java
import java.util.*;

public class Main{
    public static void main(String[] args){
        int n = 10;
        int[] arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

        for (int i = 0; i < n; i++){
            int min_index = i;
            for (int j = i+1; j < n; j++){
                if (arr[min_index] > arr[j]){
                    min_index = j;
                }
            }
            int temp = arr[j];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
        for (int i = 0; i < n; i++){
            System.out.print(arr[i]+" ");
        }
    }
}
```

## 선택 정렬의 시간 복잡도
- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 N + (N-1) + (N-2) + ... + 2
- 이는 (N^2 + N - 2) / 2로 표현할 수 있는데, 빅오 표기법에 따라 O(N^2)라고 작성함.


## 삽입 정렬
- 처리되지 않은 데이터를 하나 씩 골라 적절한 위치에 삽입.
- 선택 정렬에 비해 구현 난이도는 높은 편이지만, 일반적으로 더 효율적으로 동작함.

```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int n = 10;
int target[10] = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

int main(void){
    for (int i = 1; i < n; i++){
        for (int j = i; j > 0; j--){
            if(target[j] < target[j-1]){
                swap(target[j], target[j-1]);
            }
            else break;
        }
    }
    for (int i = 0; i < n; i++){
        cout << target[i] << ' ';
    }
    return 0;
}
```

```java
import java.util.*;
public class Main{
    public static void main(String[] args){
        int n = 10;
        int[] arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];
        for (int i = 1; i < n; i++){
            for (int j = i; j > 0; j--){
                if(arr[j] < arr[j-1]){
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                }
                else break;
            }
        }
        for(int i = 0; i < n; i++){
            System.out.print(arr[i]+" ");
        }
    }
}
```


## 삽입 정렬의 시간 복잡도
- 삽입 정렬의 시간 복잡도는 O(N^2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩.
- 삽입 정렬은 `현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작` 한다.
    - 최선의 경우 O(N)의 시간 복잡도를 가짐
    - 이미 정렬되어 있는 상태에서 다시 삽입 정렬을 수행하면?


# 퀵 정렬
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나.
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘.
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정.

## 퀵 정렬이 빠른 이유: 직관적인 이해
- 이상적인 경우, 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다.
- 너비 * 높이 = N * logN = NlogN
> 배열의 길이는 N이다. 높이는 여기서 N인 배열을 계속 2개로 분할을 하는데 이때 생긴 경우의 수들을 말하는 것 같다. 

## 퀵 정렬의 시간 복잡도
- 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다.
- 하지만 최악의 경우에는 O(N^2)의 시간 복잡도를 가짐.
    - 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행한다면?
> 배열이 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]로 설정되어 있다면, 피벗은 0이고 왼쪽에서 오른쪽으로 서치할 때의 큰 수는 1, 작은 수는 오른쪽에서 왼쪽으로 서치할 때 결국 0이 나온다. 그럼 피벗은 그대로 0 자리에 있으며 분할은 [0], [1, 2, 3, 4, 5, 6, 7, 8, 9]가 되기 때문에 배열이 절반으로 나뉘지 않는다. 그래서 이 최악의 경우에는 시간 복잡도가 O(N^2)가 나오는 것이다.

```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end:
        return                  # 원소가 1개인 경우 종료
    pivot = start
    left = start+1
    right = end
    while(left <= right):       
        while(left <= end and array[left] <= array[pivot]):      # 피벗보다 큰 데이터를 찾을 때 까지 반복
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int n = 10;
int target[10] = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

void quickSort(int* target, int start, int end){
    if(start >= end) return;
    int pivot = start;
    int left = start + 1;
    int right = end;
    while(left <= right){
        while(left <= end && target[left] <= target[pivot]) left++;
        while(right > start && target[right] > target[pivot]) right--;
        if(left > right) swap(target[pivot], target[right]);
        else swap(target[left], target[right]);
    }
    quickSort(target, start, right-1);
    quickSort(target, right+1, end);
}
int main(void){
    quickSort(target, 0, n-1);
    for(int i = 0; i<n ; i++){
        cout << target[i] << ' ';
        return 0;
    }
}
```


```java
import java.util.*;
public class Main{
    public static void quickSort(int[] arr, int start, int end){
        if(start >= end) return;
        int pivot = start;
        int left = start + 1;
        int right = end;
        while (left <= right){
            while(left <= end&& arr[left] <= arr[pivot]) left++;
            while(right > start && arr[right] >= arr[pivot]) right--;
            if (left > right){
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            }
            else{
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
        quickSort(arr, start, right-1);
        quickSort(arr, right+1, end);
    }

    public static void main(String[] args){
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8}

        quickSort(arr, 0, n-1);
    }
}
```

### 파이썬 장점을 살린 퀵 정렬 소스코드
```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))
```


# 계수 정렬
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘.
    - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K)를 보장.

```py
#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2 ,9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] +=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```

```cpp
#include <bits/sstdc++.h>
#define MAX_VALUE 9
using namespace std;

int n = 15;
int arr[15] = [7, 5, 9, 0, 3, 1, 6, 2 ,9, 1, 4, 8, 0, 5, 2];
int cnt[MAX_VALUE+1];

int main(void){
    for (int i = 0; i < n ;i++){
        cnt[arr[i]] += 1;
    }
    for (int i = 0; i <= MAX_VALUE; i++){
        for(int j = 0; j < cnt[i]; j++){
            cout << i << ' ';
        }
    }
}
```

```java
import java.util.*;

public class Main{
    public static final int MAX_VALUE = 9;

    public static void main(String[] args){
        int n = 15;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2 ,9, 1, 4, 8, 0, 5, 2};
        int[] cnt = new int[MAX_VALUE + 1];

        for(int i = 0; i < n; i++){
            cnt[arr[i]] += 1;
        }
        for(int i = 0; i <= MAX_VALUE; i++){
            for(int j = 0; j < cnt[i]; j++){
                System.out.print(i+" ");
            }
        }
    }
}
```


## 계수 정렬의 복잡도 분석
- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있음
    - 데이터가 0과 999999로 단 2개만 존재하는 경우를 생각하면 됨
    > 배열을 0부터 999999까지 생성해야 함. (배열의 길이가 1000000임)
- 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있음
    - 성적의 경우, 100점을 맞은 학생이 여러 명 일 수 있기 때문에 계수 정렬이 효과적.

