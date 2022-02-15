# counter 
## python collections library's counter function
## iterable 객체(like list)가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌

from collections import Counter
counter = Counter(['red','blue', 'blue','blue', 'red', 'blue', 'green', 'red', 'red'])

print(counter['blue'])
print(counter['green'])
print(counter['red'])
print(dict(counter))


# 최대 공약수와 최소 공배수
## 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd()

import math
def lcm(a, b):
    return a * b // math.gcd(a, b) ## 최소 공배수를 구하는 함수 작성 (with gcd)

a = 21
b= 14
print(math.gcd(a ,b))
print(lcm(a, b))