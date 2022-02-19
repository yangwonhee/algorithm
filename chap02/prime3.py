# 1000 이하의 소수를 나열하기 (알고리즘 개선 2)

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1
prime[ptr] = 2
ptr += 1

# prime = [2, 3]

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n: # n = 5일 때 i는 0만 실행됨
        counter += 2                # 카운트를 2 늘리는 이유는 바로 위의 while조건과 바로 아래의 if조건 때문.
        if n % prime[i] == 0:       # n = 5, prime[0] = 2  5 % 2 != 0 임
            break                   # 만약 while문이 여기서 강제 종료된다면 prime * prime은 카운트 되지 않음
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')