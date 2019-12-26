from sys import stdin
 
n_datasets = stdin.readline()
n_m = stdin.readline().split()
n = n_m[0]
m = n_m[1]
A = stdin.readline().split()
for i in range(len(A)):
    A[i] = int(A[i])

start = 0
for i,x in enumerate(A):
    if x < m:
        start = i+1
        continue
    