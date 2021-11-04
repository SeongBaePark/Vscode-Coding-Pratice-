#더하기 사이클
N = int(input())
cnt= 0
data = N
if data < 10:
    data += 10
while True:
    first = int(data % 10) 
    second = int(data / 10 + first) % 10 
    data = int((first * 10) + second)
    cnt +=1
    if data == N:
        break
print(cnt)