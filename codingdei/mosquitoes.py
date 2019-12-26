"""
    Solution to Pesky Mosquitoes problem: https://open.kattis.com/problems/mosquitoes
    Author: Francesco Pham
    Date: 13/12/2019
"""
import math

def norm_sq(v):
	return v[0]*v[0] + v[1]*v[1]

def dist(p1, p2):
	return math.sqrt(norm_sq((p1[0]-p2[0], p1[1]-p2[1])))

def center_of_circle(p1, p2, radius):
	mid_x = (p1[0] + p2[0]) / 2
	mid_y = (p1[1] + p2[1]) / 2
	mid = (mid_x, mid_y)
	len_p1_to_mid = dist(p1, mid)

	if radius < len_p1_to_mid:
		return None

	len_mid_to_center = math.sqrt(radius**2 - len_p1_to_mid**2)
	angle = math.atan2(p1[0] - p2[0], p2[1] - p1[1])
	center_x = mid_x + len_mid_to_center * math.cos(angle)
	center_y = mid_y + len_mid_to_center * math.sin(angle)
	return (center_x, center_y)


n_testcases = int(input())
for _ in range(n_testcases):
	input() # remove blank line
	line = input().split()
	m = int(line[0])
	d = float(line[1])
	radius = d/2

	mosquitoes = []
	for _ in range(m):
		mosquitoes.append([float(x) for x in input().split()])
	
	best_trap = 0
	for i in range(len(mosquitoes)):
		for j in range(len(mosquitoes)):
			center = center_of_circle(mosquitoes[i], mosquitoes[j], radius)
			if center == None:
				continue
			trapped_mosquitoes = 0
			for mosquitoe in mosquitoes:
				distance = dist(center, mosquitoe)
				if distance <= radius:
					trapped_mosquitoes += 1

			best_trap = max(best_trap, trapped_mosquitoes)
	
	print(best_trap)