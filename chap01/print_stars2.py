# *를 n개 출력하되 w개 마다 줄 바꿈하기 (2)

print("*을 출력합니다.")
n = int(input("몇 개를 출력할까? "))
w = int(input("몇 개마다 줄 바꿈할까? "))

for _ in range(n//w):
    print("*" * w)

if n%w:
    print("*" * (n%w))