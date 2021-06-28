"""
주어진 숫자가 1이 될때 까지
어떠한 수 n, 나누는 숫자 k
n을 k로 나눌 수 없으면 나눌 수 있을 때 까지 -1
n을 k로 나눌 수 있으면 바로 나눔
둘중에 하나 선택해서 연산
n이 1이 될 때 까지의 최소 횟수를 구하시오
"""
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
while n > 1:
    n -= 1
    result += 1
print(result)    

