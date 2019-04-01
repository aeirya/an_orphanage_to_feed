class Baby:
    def __init__(self, bearing):
        self.bearing = bearing
        self.timeLeft = 0
        self.nagging = True

    def __gt__(self, baby2):
        return self.bearing > baby2.bearing

    def feed(self):
        self.timeLeft = self.bearing
        self.nagging = False

    def starve(self):
        self.timeLeft -= 1
        if self.timeLeft == 0:
            self.nagging = True

def checkAsger(i , j, baby):
    # print("comaring {} and {} with bearings of {} and {}".format(i,j, baby[i].bearing, baby[j].bearing))
    return  True if abs(j-i) <= max(baby[i].bearing, baby[j].bearing) else False

def Asger(baby):
    beds = len(baby)
    for i in range( beds-1 ):
        for j in range( i+1 , beds):
            if not checkAsger(i,j, baby):
                return False
    return True

def checkAlvida(x, y):
    if y>x+1:
        return False
    return True

def Alvida(baby):
    bearings = [ child.bearing for child in baby ]
    max_bearing =  max(bearings)
    countBearing = [ 0 for _ in range(max_bearing+1) ]
    for i in bearings:
        countBearing[i] += 1
        # print(countBearing)
        if not checkAlvida(i , countBearing[i]): return False
    return True

def Arvid(baby):
    counter = []
    # for child in baby :
        # if child.bearing in 

def Alfhild(baby):
    n = len(baby)
    while(n>1):
        bigBaby, smallBaby = 0,0
        
        for i in range(n):
            if baby[i] > baby[bigBaby]:
                bigBaby = i
            elif baby[i] < baby[smallBaby]:
                smallBaby = i
        if not checkAsger(smallBaby, bigBaby, baby): return False
        del baby[smallBaby]
        del baby[bigBaby]
        # print([x.bearing for x in baby])
        n-=2
    return True

def can(baby):
    # if not Alvida(baby): return False
    if not Alfhild(baby): return False
    # if not Asger(baby): return False
    return True

def main():
    n = input() #this line does abosolutely nothing 
    baby= [ Baby(int(x)) for x in input().split() ]
    print( "YES" if can(baby) else "NO" )

main()