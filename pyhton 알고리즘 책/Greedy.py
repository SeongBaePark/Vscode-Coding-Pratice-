""" 그리디 알고리즘
    현 상황에서 가장 좋은 것만 고르는 알고리즘 , 나중에 미칠 영향은 신경쓰지 않는다.            
"""
# ex1) 거스름돈 문제 (그리디 알고리즘 대표적인 문제)

n = 1260
count = 0

coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin
    n %= coin
print(count)