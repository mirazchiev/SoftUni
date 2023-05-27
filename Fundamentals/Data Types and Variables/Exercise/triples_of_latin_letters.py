n = int(input())

for i in range(97, n + 97):
    i = chr(i)
    for j in range(97, n + 97):
        j = chr(j)
        for k in range(97, n + 97):
            k = chr(k)
            print(i+j+k)
