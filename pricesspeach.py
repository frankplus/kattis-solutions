N,Y = [int(x) for x in input().split()]
myset = set()
for _ in range(Y):
    obstacle = int(input())
    myset.add(obstacle)

for i in range(N):
    if i not in myset:
        print(i)

print("Mario got", len(myset),"of the dangerous obstacles.")