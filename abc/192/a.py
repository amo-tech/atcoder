X = int(input())

for i in range(1, 101):
    if (i + X) % 100 == 0:
        print(i)
