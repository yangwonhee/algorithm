# 기본 입출력

## 모든 프로그램은 적절한 입출력 양식을 가지고 있다.
## 프로그램 동작의 첫 번째 단계는 데이터를 입력받거나 생성하는 것.

# input()은 한 줄의 문자열을 입력 받는 함수
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용


###############

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)


#################

# 빠르게 입력 받기
## 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우!
## sys 라이브러리에 정의되어 있는 sys.stdin.readline() 사용
## 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드 함께 사용

import sys
data = sys.stdin.readline().rstrip()
print(data)

################

# 자주 사용되는 표준 출력 방법
## 파이썬에서 기본 출력은 print()
### 각 변수를 콤마를 이용해서 띄어쓰기로 구분해서 출력
## print()는 기본적으로 출력 이후에 줄 바꿈을 수행
### 줄 바꿈을 원치않는 경우 'end'를 이용

a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 8
print("the answer is", str(answer), "!")


################
################

# f-string
## python 3.6 ~ 적용됨
## 자바스크립트에서 ${}랑 비슷

answer = 8
print(f"the answer is {answer} !")
