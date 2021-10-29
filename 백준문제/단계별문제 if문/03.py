#윤년
ly = int(input())
if ly % 4 == 0:
    if ly % 100 == 0 and ly % 400 != 0:
        print(0)
    else:
        print(1)
else:
    print(0)