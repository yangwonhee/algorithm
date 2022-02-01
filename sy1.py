
#문자열 입력
data = list(input())
total = 0
result = data
num = ['0','1','2','3','4','5','6','7','8','9']

for i in data:
    if i in num:
        total += int(i)


#정렬
result.sort()
for i in result:
    print(i,end='')
print(total)