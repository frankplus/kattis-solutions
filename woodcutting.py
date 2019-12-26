n_testcases = int(input())

for _ in range(n_testcases):
    N = int(input())
    customers = []
    for _ in range(N):
        line = [int(x) for x in input().split()]
        if line and len(line) > 1:
            W = line[0]
        else:
            W = 0

        tot_wood = 0
        for i in range(0,W):
            size = int(line[i+1])
            tot_wood += size
        customers.append(tot_wood)

    customers.sort()
    
    somma = 0
    for c in customers:
        somma = 2*somma + c

    # somma = customers[0]
    # for i in range(1, len(customers)):
    #     customers[i] += customers[i-1]
    #     somma += customers[i]

    if N != 0:
        print(somma / N)
    else:
        print(0)