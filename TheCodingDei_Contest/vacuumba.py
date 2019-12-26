"""
    Solution to Vacuumba problem: https://open.kattis.com/problems/vacuumba
    Author: Francesco Pham
    Date: 13/12/2019
"""
from math import sin, cos, radians

class Segment:
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance

n_testcases = int(input())
for _ in range(n_testcases):
    n_segments = int(input())

    segments = []
    for _ in range(n_segments):
        angle, distance = [float(x) for x in input().split()]
        segments.append(Segment(angle, distance))
    
    position = [0.0,0.0]
    angle = 0.0

    for segment in segments:
        angle += segment.angle
        delta_x = -segment.distance * sin(radians(angle))
        delta_y = segment.distance * cos(radians(angle))

        position[0] += delta_x
        position[1] += delta_y
    
    print(position[0], position[1])
