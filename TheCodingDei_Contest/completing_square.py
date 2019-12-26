"""
    Solution to Completing the Square problem: https://open.kattis.com/problems/completingthesquare
    Author: Francesco Pham
    Date: 13/12/2019
"""
import math

def norm_sq(v):
    return v[0]*v[0] + v[1]*v[1]

def dist(p1, p2):
    return math.sqrt(norm_sq((p1[0]-p2[0], p1[1]-p2[1])))

def toVec(a, b):
    return (b[0]-a[0], b[1]-a[1])

def translate(p, v):
    return (p[0]+v[0], p[1]+v[1])

points = []
for _ in range(3):
    x,y = [int(x) for x in input().split()]
    points.append((x,y))


dist_ab = dist(points[0], points[1])
dist_bc = dist(points[1], points[2])
dist_ca = dist(points[2], points[0])

if dist_ab == dist_bc:
    A = points[0]
    B = points[1]
    C = points[2]
elif dist_bc == dist_ca:
    A = points[1]
    B = points[2]
    C = points[0]
elif dist_ab == dist_ca:
    A = points[1]
    B = points[0]
    C = points[2]

vec = toVec(B, A)
D = translate(C, vec)

print(D[0], D[1])