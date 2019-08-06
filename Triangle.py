#Triangle Class

class Triangle:
    """Represents a triangle.

    attributes: side1, side2, side3.
    """
    #Inside class Triangle
    def __init__(self, sideA = 3, sideB = 4, sideC = 5):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    #Getters & Setters for sides A, B, and C
    def getA(self):
        #get side A
        return self.sideA

    def setA(self, new_a):
        #set side A
        self.sideA = int(new_a)

    def getB(self):
        #get side B
        return self.sideB

    def setB(self, new_b):
        #set side B
        self.sideB = int(new_b)

    def getC(self):
        #get side C
        return self.sideC

    def setC(self, new_c):
        #set side C
        self.sideC = int(new_c)

    def isEquilateral(self):
        '''Returns True if all 3 sides are equal.
        '''
        return self.sideA == self.sideB and self.sideA == self.sideC

    def isIsosceles(self):
        '''Returns True if at least 2 sides are the same. 
        (2+ equal sides returns True; Equilateral are also Isoceles.)
        '''
        return self.sideA == self.sideB or self.sideA == self.sideC or self.sideB == self.sideC

    def isScalene(self):
        '''Returns True if no two sides are equal.
        '''
        return self.sideA != self.sideB and self.sideA != self.sideC and  self.sideB != self.sideC

    def isRight(self):
        '''Checks if the value of any of the three sides squared 
        are equal to the sum of the squares of the other two sides, 
        then returns True.
        '''
        hypotenuse = 0
        side1 = 0
        side2 = 0

        if self.sideA > self.sideB and self.sideA > self.sideC:
            hypotenuse = self.sideA
            side1 = self.sideB
            side2 = self.sideC
        elif self.sideB > self.sideA and self.sideB > self.sideC:
            hypotenuse = self.sideB
            side1 = self.sideA
            side2 = self.sideC
        elif self.sideC > self.sideA and self.sideC > self.sideB:
            hypotenuse = self.sideC
            side1 = self.sideA
            side2 = self.sideB
        else:
            return False
        return hypotenuse**2 == (side1**2 + side2**2)