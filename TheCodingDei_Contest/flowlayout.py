"""
    Solution to Flow Layout problem: https://open.kattis.com/problems/flowlayout
    Author: Francesco Pham
    Date: 13/12/2019
"""
max_width = int(input())
while max_width != 0:

    rectangles = []
    rectangle = [int(x) for x in input().split()]
    while rectangle[0] != -1 and rectangle[1] != -1:
        rectangles.append(rectangle)
        rectangle = [int(x) for x in input().split()]

    width = 0 
    height = 0
    curr_width = 0 # width in current row
    prev_height = 0
    for w_rect, h_rect in rectangles:
        if curr_width + w_rect > max_width:
            # put rectangle in new row
            curr_width = 0
            prev_height = height

        curr_width += w_rect
        width = max(width, curr_width)
        height = max(height, prev_height + h_rect)

    print(width, 'x', height)

    max_width = int(input())