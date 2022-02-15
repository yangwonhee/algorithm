# 거스름돈 문제 답
n = int(input())
count = 0

array = [500, 100, 50, 10]

for i in array:
    count += n // i
    n %= i

print(count)