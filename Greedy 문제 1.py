"""
큰 수의 법칙
시간 제한 1초 메모리 제한 128MB 기출 : 2019 국가 교육기관 코딩 테스트
배열의 크기 n 숫자가 더해지는 횟수 m 큰수 반복 k번
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
frist = data[n - 1]
second = data[n - 2]

result= 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += frist
        m -= 1
    if m == 0:
        break
    result += second
    m-=1

print("최종 값은 %d 입니다." % (result))