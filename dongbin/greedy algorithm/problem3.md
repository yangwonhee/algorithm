# <문제> 모험가 길드 : 문제 설명

- 한 마을에 모험가가 n명 있습니다. 모험가 길드에서는 n명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
- 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
- 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. n명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.

- 예를 들어 n = 5, 각 모험가들의 공포도는 2 3 1 2 2 이다.
- 이 경우 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면 총 2개의 그룹을 만들 수 있다.
- 또한 몇 명의 모험가는 마을에 그대로 남아있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.

입력예시:
5
2 3 1 2 2

출력예시:
2

# 내 생각

- 리스트를 만들고 n번 반복하며 공포도를 입력받아서 리스트에 append한다.
- 공포도를 입력받은 리스트를 sort()를 통해 오름차순 정렬을 한다.
- 그룹 개수의 최댓값을 출력하는 문제이므로, 그룹개수가 커지려면 그룹내의 사람 수는 적어야 한다.
- 그러므로 공포도가 낮은 사람들부터 그룹을 만든 후, 공포도가 높은 사람들 끼리 그룹을 결성하는데, 이 때, 인원이 부족하면 앞에 공포도가 높은 그룹에서 차출하여 인원에 맞게 구성을 한다. (인데, 이걸 어떻게 구현할지 생각 중,,)
  ~~- 만약에 2 3 1 2 2 3 1 이라면, 정렬하면 1 1 2 2 2 3 3 이고, [1] [1] [2, 2] [2, 3, 3] 이건 딱 떨어지네..~~
  ~~- 그럼 만약 2 3 1 2 2 4 라면! 정렬하면 1 2 2 2 3 4 니까, [1] [2, 2] [2, 3, 4]-> 4이기 때문에 한명이 더 필요. 이걸 1에서 충원.인데 만약 1이 없다면?~~
  ~~- 만약 2 3 2 2 4 라면.. 정렬하면 2 2 2 3 4니까, [2,2] [2, 3, 4] 이건 .. 안되니까, 그룹을 하나로 결성 or 문제에서 `또한 몇 명의 모험가는 마을에 그대로 남아있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.` 라고 했으므로 그냥 한 그룹만 가는 것과 같겠다.. [2,2]로 가거나, [2, 2, 2, 3, 4]로 가거나..~~

- 위에처럼 아주.. 깊고 어렵게 생각을 했는데 문제 아이디어 보고 아... 했음 ..

# 문제 해결 아이디어

- 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인합니다.
- 앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면 이를 그룹으로 설정하면 됨.

- 이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가 수만 포함하여 그룹을 결성하게 된다.

```py
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
```