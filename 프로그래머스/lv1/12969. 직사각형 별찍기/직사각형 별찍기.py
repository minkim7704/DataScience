a, b = map(int, input().strip().split(' '))

for row in range(b):
    for col in range(a):
        print("*", end= "")
    print()