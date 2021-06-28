"""
숫자 카드 게임
룰 n과 m 행렬중에서 각 행중에서 가장 낮은 숫자를 뽑게 만들고 최종적으로 가장 행마다 뽑은 가장 낮은 카드를 비교하여 가장 큰 카드를 찾으시오
"""
n, m = map(int, input().split())

result  = 0

"""
방법 1 min과 max 이용

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
"""

" 방법 2 이중 반복문"

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)