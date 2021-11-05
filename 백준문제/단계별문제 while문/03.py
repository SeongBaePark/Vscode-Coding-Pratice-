#더하기 사이클
N = int(input())
cnt= 0
data = N
if data < 10:
    data = data*10 + data
while True:
    cnt +=1
    first = int(data % 10) 
    second = int(data / 10 + first) % 10 
    data = int((first * 10) + second)
    if data == N:
        break
print(cnt)