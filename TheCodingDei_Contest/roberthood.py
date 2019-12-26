"""
    Solution to Robert Hood problem: https://open.kattis.com/problems/roberthood
    Author: Francesco Pham
    Date: 13/12/2019
"""
import math

def norm_sq(v):
    return v[0]*v[0] + v[1]*v[1]

def dist(p1, p2):
    return math.sqrt(norm_sq((p1[0]-p2[0], p1[1]-p2[1])))

def andrew_hull(P):
    if len(P) < 2: return P
    P = sorted(P)
    L = []
    U = []
    for pt in P:
        while len(L) > 1 and turn(L[-2], L[-1], pt) <= 0: L.pop()
        L.append(pt)

    for pt in reversed(P):
        while len(U) > 1 and turn(U[-2], U[-1], pt) <= 0: U.pop()
        U.append(pt)
    return L[:-1] + U[:-1]


def turn(pt1, pt2, pt3):
    '''Given three points, returns
    0 if they are collinear (no turn),
    a positive number if they form a left (counter-clockwise) turn,
    a negative number if they form a right (clockwise) turn.'''
    # No trigonometry required!
    # See https://en.wikipedia.org/wiki/Graham_scan
    (x1, y1), (x2, y2), (x3, y3) = pt1, pt2, pt3
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def area(P):
    '''Returns the area of a polygon specified by a list P of vertices
    given in some order (either clockwise or counter-clockwise).
    Works for both convex and concave polygons.
    See also https://en.wikipedia.org/wiki/Shoelace_formula'''
    result = 0.0
    for i in range(len(P)-1):
        (x1, y1) = P[i]
        (x2, y2) = P[i+1]
        result += (x1*y2 - x2*y1)
    return abs(result) / 2.0

C = int(input())
shots = []
for _ in range(C):
    x, y = [int(x) for x in input().split()]
    shots.append((x,y))

hull = andrew_hull(shots)

max_dist = 0
for i in range(len(hull)):
    for j in range(i+1, len(hull)):
        distance = dist(hull[i], hull[j])
        max_dist = max(max_dist, distance)

print(max_dist)