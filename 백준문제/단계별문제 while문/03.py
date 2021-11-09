#더하기 사이클
N = int(input())
cnt= 0
data = N

while True:
    if data < 10:
        data = data*10 + data
        cnt +=1
    else:
        first = int(data % 10) 
        second = int(data / 10 + first) % 10 
        data = int((first * 10) + second)
        cnt +=1
    if data == N:
        break
print(cnt)