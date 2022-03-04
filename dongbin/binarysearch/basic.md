# 이진 탐색 알고리즘
- 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
- 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    - 이진탐색은 시작점, 끝점, 중간점을 이용하여 탐색범위를 설정.

## 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 logN에 비례.
- 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개가량의 데이터만 남음.
    - 2단계까지는 8개, 3단계까지는 4개가 남음
- 이진탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장.

```py
# 재귀적 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

```py
# 반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```


```cpp
#include <bits/stdc++.h>
using namespace std;

int binarySearch(vector<int>& arr, int target, int start, int end){
    while(start <= end){
        int mid = (start + end) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] > target) end = mid - 1;
        else start = mid + 1;
    }
    return -1;
}

int n, target;
vector<int> arr;

int main(void){
    cin >> n >> target;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        arr.push_back(x);
    }
    int result = binarySearch(arr, target, 0, n-1);
    if(result == -1){
        cout << "원소가 존재하지 않습니다." << '\n';
    }
    else{
        cout << result+ 1 << '\n';
    }
    return 0;
}
```

```java
public class Main{
    public static int binarySearch(int[] arr, int target, int start, int end){
        while(start <= end){
            int mid = (start + end) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] > target) end = mid - 1;
            else start = mid + 1;
        }
        return -1;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int target = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int result = binarySearch(arr, target, 0, n-1);
        if (result == -1){
            System.out.println("원소가 존재하지 않습니다.");
        }
        else {
            System.out.println(result + 1);
        }
    }
}
```

## 파이썬 이진 탐색 라이브러리
- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

```py
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
>>> 2
>>> 4
```

```py
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

>>> 2
>>> 6
```