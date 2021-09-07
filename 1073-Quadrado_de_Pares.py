N = int(input())
for i in range(1,N+1):
    if (5 < N < 2000 and   i % 2 == 0):
        print("{}^{} = {}".format(i,2,pow(i,2)))
