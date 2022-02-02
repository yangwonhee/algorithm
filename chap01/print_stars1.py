# *를 n개 출력하되 w개 마다 줄 바꿈하기 (1)

print("*을 출력합니다.")
n = int(input("몇 개를 출력할까? "))
w = int(input("몇 개마다 줄 바꿈할까? "))

for i in range(n):
    print("*", end = "")
    if i % w == w-1:
        print()

print()