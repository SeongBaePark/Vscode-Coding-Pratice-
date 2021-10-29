H, M = map(int, input().split())
if H > 0 and M < 45:
    H = H -1
    M = M - 45 + 60
    print(H, M)
elif M >= 45:
    M = M -45
    print(H, M)
elif H == 0 and M < 45:
    H = H + 23
    M = M - 45 + 60
    print(H, M)
   
