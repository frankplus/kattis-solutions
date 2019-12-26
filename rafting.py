import math
  
def dot(v,w):
    x,y = v
    X,Y = w
    return x*X + y*Y
  
def length(v):
    x,y = v
    return math.sqrt(x*x + y*y)
  
def vector(b,e):
    x,y = b
    X,Y = e
    return (X-x, Y-y)
  
def unit(v):
    x,y = v
    mag = length(v)
    return (x/mag, y/mag)
  
def distance(p0,p1):
    return length(vector(p0,p1))
  
def scale(v,sc):
    x,y = v
    return (x * sc, y * sc)
  
def add(v,w):
    x,y = v
    X,Y = w
    return (x+X, y+Y)
    
def dist_pnt_line(pnt, start, end):
    line_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    line_len = length(line_vec)
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/line_len)
    t = dot(line_unitvec, pnt_vec_scaled)    
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    nearest = add(nearest, start)
    #return (dist, nearest)
    return dist

testcases = int(input())
for _ in range(testcases):
    n_inner_points = int(input())
    innerpoints = []
    for _ in range(n_inner_points):
        input_point = input()
        point = [int(s) for s in input_point.split()]
        innerpoints.append(point)
    
    n_outer_points = int(input())
    outerpoints = []
    for _ in range(n_outer_points):
        input_point = input()
        point = [int(s) for s in input_point.split()]
        outerpoints.append(point)
    
    min_dist = dist_pnt_line(innerpoints[0], outerpoints[0], outerpoints[1])
    for point in innerpoints:
        for i in range(0,n_outer_points-1):
            dist = dist_pnt_line(point, outerpoints[i], outerpoints[i+1])
            min_dist = min(min_dist, dist)
    
    for point in outerpoints:
        for i in range(0,n_inner_points-1):
            dist = dist_pnt_line(point, innerpoints[i], innerpoints[i+1])
            min_dist = min(min_dist, dist)
    
    print(min_dist/2)