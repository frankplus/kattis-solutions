"""
    Solution to Darts problem: https://open.kattis.com/problems/dartscores
    Author: Francesco Pham
    Date: 11/12/2019
"""
import math
n_testcases = int(input())

def norm_sq(v):
    return v[0]*v[0] + v[1]*v[1]

def dist(p1, p2):
    return math.sqrt(norm_sq((p1[0]-p2[0], p1[1]-p2[1])))

for _ in range(n_testcases):
    n = int(input())
    tot_points = 0
    for _ in range(n):
        x,y = [int(i) for i in input().split()]
        radii = [20 , 40, 60, 80, 100, 120, 140, 160, 180, 200]
        distance_to_center = dist((x,y), (0,0))
        points = 0
        for radius in radii:
            if distance_to_center <= radius:
                points = 11 - radius/20
                break
        tot_points += points
    
    print(int(tot_points))