# Given a string like `UUUDULR`, need to derive the final coordinates starting from (0, 0).
import math


class Point():
    def __init__(self, X=0, Y=0):
        self.x = X
        self.y = Y

    def __add__(self, o): 
        return Point(self.x + o.x, self.y + o.y)
    
    def distancefromO_O(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    
    def __str__(self):
        return str(self.x) +', ' + str(self.y)

    
decisiondict = {
    'U': Point(0, 1),
    'D': Point(0, -1),
    'R': Point(1, 0),
    'L': Point(-1, 0)
}

def solve(string):
    point = Point()
    for s in string:
        try:
            updatepoint = decisiondict[s.upper()]
            point += updatepoint
        except:
            pass
    
    return str(point), point.distancefromO_O()


print(solve('UUDDURRRRRRUUUUUUUUUuuuuDLR'))