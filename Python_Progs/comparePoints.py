import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        coords = test[:len(test)-1].split(" ")
        O, P, Q, R = map(int,coords)
        if (O - Q) > 0:
            lat = 1 # West
        elif (O - Q) == 0:
            lat = 10
        else:
            lat = 100 # East

        if (P - R) > 0:
            lon = 2 # South
        elif (P - R) == 0:
            lon = 20
        else:
            lon = 200 # North

        x = lat + lon
        if (x == 30): d = "here"
        elif (x ==   3): d = "SW"
        elif (x ==  21): d = "W"
        elif (x == 201): d = "NE"

        elif (x ==  12): d = "S"
        elif (x ==  30): d = "here"
        elif (x == 210): d = "N"

        elif (x == 102): d = "SE"
        elif (x == 120): d = "E"
        elif (x == 300): d = "NE"

        elif (x ==   3): d = "SW"
        elif (x ==  12): d = "S"
        elif (x == 102): d = "SE"

        elif (x ==  21): d = "W"
        elif (x ==  30): d = "here"
        elif (x == 120): d = "E"

        elif (x == 201): d = "NW"
        elif (x == 210): d = "N"
        elif (x == 300): d = "NE"
        else:
            d = "here"

        print d

