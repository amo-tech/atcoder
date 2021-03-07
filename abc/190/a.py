A, B, C = map(int, input().split())
if C == 0:
    if A-B > 0:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if B-A > 0:
        print('Aoki')
    else:
        print('Takahashi')
