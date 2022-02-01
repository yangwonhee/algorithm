data = input()
total = 0
result = []

for i in data:
    if i.isalpha():
        result.append(i)
    else:
        total += int(i)


result.sort()
result.append(str(total))

print(''.join(result))



# for i in data:
#     if i in num:
#         total += int(i)
#         data.remove(i)

# data.sort()
# for i in data:
#     print(i, end='')

# print(total)