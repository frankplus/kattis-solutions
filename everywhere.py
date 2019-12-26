n_testcases = int(input())

for _ in range(n_testcases):
    n_trips = int(input())
    trips = set()
    for _ in range(n_trips):
        city = input()
        if city not in trips:
            trips.add(city)
    
    print(len(trips))