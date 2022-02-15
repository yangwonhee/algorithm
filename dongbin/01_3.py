# global keyword
## global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()
    
print(a)