a = [29, 10, 14, 37, 14]
len_a = len(a)

print(f"Begin:\t{a}")

for i in range(0, len_a):
    for j in range(0, len_a - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            print(a)

print(f"End:\t{a}")