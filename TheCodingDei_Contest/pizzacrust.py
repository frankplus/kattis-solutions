"""
    Solution to Pizza Crust problem: https://open.kattis.com/problems/pizza2
    Author: Francesco Pham
    Date: 13/12/2019
"""
R, C = [int(x) for x in input().split()]
percentage = ((R-C)**2/R**2)*100
print(percentage)