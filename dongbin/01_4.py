# 람다 표현식
## 람다 표현식을 이용하면 함수를 더 간단하게 작성할 수 있다.
## 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징.

def add(a, b):
    return a+b

# 일반적인 add() 메서드 사용
print(add(3,5))
# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+b)(3,5))


################

# 람다 표현식 예시: 내장 함수에서 자주 사용되는 람다 함수
array = [('hong', 50), ('lee', 34), ('any', 24)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


################

# 람다 표현식 예시: 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2= [6,7,8,9,10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))