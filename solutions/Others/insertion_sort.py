a = [29, 10, 14, 37, 14]
len_a = len(a)

print(f"Begin:\t{a}")

for i in range(0, len_a):
    j = i
    while j > 0 and a[i] < a[j - 1]:
        j -= 1
    
    tmp = a[i]
    for k in range(i, j, -1):
        a[k] = a[k - 1]
    a[j] = tmp
    print(a)

print(a)
