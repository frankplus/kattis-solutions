line = input()
while line != "END":
    n = float(line)
    res = []
    for i in range(10):
        x = n*3
        res.append(int(x))
        x -= int(x)

    print(res)
    
    member = "MEMBER"
    for x in res:
        if x == 1:
            member = "NON-MEMBER"

    print(member)

    line = input()