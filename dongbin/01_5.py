# 순열과 조합


## 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것.
### 'abc' 'acb' 'bac' 'bca' 'cab' 'cba'

from itertools import permutations

data = ['a', 'b', 'c']

result = list(permutations(data, 3))
print(result)


## 조합: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
### 'ab' 'ac' 'bc'

from itertools import combinations
data = ['a', 'b', 'c']
result = list(combinations(data, 2))
print(result)


## 중복 순열

from itertools import product
result = list(product(data, repeat = 2))
print(result)



## 중복 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)