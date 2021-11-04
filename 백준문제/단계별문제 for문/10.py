# 별 찍기 -2
N = int(input())
for i in range(N):
  stars = '*' * (i + 1)
  print('{0:>{1}}'.format(stars,N))