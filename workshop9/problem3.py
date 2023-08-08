# problem3, 18/05/21, Cordelia Jiang
from math import hypot


# use a^2 + b^2 = c^2 (pythagoras) to calculate diagonal distance between coordinates
def diagonalLineDistanceCalc(__reference1, __reference2, _reference3):
    if __reference2[1] < _reference3[1]:
        b = (_reference3[1] - __reference1[1]) * 0.5  # grid lines are 0.5 km apart
    else:
        b = (__reference1[1] - _reference3[1]) * 0.5
    if __reference1[0] < _reference3[0]:
        a = (_reference3[0] - __reference1[0]) * 0.5
    else:
        a = (__reference1[0] - _reference3[0]) * 0.5
    c = hypot(a, b)  # returns a float value having Euclidean norm, sqrt(x*x + y*y)
    return c


# straight line calculation
def straightLineDistanceCalc(__reference1, __reference2):
    # check whether the two references are on same line
    if __reference1[0] != __reference2[0]:
        if __reference1[0] < __reference2[0]:
            # to see how far they are apart from each other
            distance = (__reference2[0] - __reference1[0]) * 0.5  # grid lines are 0.5 km apart
        else:
            distance = (__reference1[0] - __reference2[0]) * 0.5
    else:
        if __reference1[1] < __reference2[1]:
            distance = (__reference2[1] - __reference1[1]) * 0.5
        else:
            distance = (__reference1[1] - __reference2[1]) * 0.5
    return distance


# to determine between two options: straight line, or diagonal line calculation
def distanceCheck(_reference1, _reference2):
    x = []
    y = []
    # check if they're on same line, then that's a straight line
    if _reference1[0] == _reference2[0] or _reference1[1] == _reference2[1]:
        distance = straightLineDistanceCalc(_reference1, _reference2)
        return distance

    # check if not on same line, then that's a diagonal line
    if _reference1[0] < _reference2[0]:
        x = _reference2[0]
    elif _reference1[0] > _reference2[0]:
        x = _reference1[0]
    if _reference1[1] < _reference2[1]:
        y = _reference2[1]
    elif _reference1[1] > _reference2[1]:
        y = _reference1[1]
    reference3 = [x, y]
    distance = diagonalLineDistanceCalc(_reference1, _reference2, reference3)
    return distance


# check whether each coordinate's first character is uppercase letter from A to Z
# check whether each uppercase letter is followed by a int number
# print out bad reference and terminate program if the inputted reference is False
def referenceCheck(_referenceList):
    if not _referenceList[0].isalpha() or not _referenceList[0].isupper():
        return False
    elif not _referenceList[1].isdecimal():
        return False
    else:
        return True


# getting references into the correct format
def referenceMap(_referenceList):
    x = ord(_referenceList[0])  # need to turn letters into numbers before mapping
    y = int(_referenceList[1:])
    return [x, y]


distance = 0.0
referenceList = input("Enter trip map references: ").split()
# can't calculate distance if only have one coordinate, hence -1
for i in range(len(referenceList) - 1):
    if not referenceCheck(referenceList[i]):
        print("Bad reference: " + referenceList[i])
        exit(1)  # terminate program with errors
    else:
        reference1 = referenceMap(referenceList[i])
        reference2 = referenceMap(referenceList[i + 1])
        distance += distanceCheck(reference1, reference2)
        distance = round(distance + 0.015, 1)  # distance will always round up on first decimal place

print("Total distance = " + str(distance) + " km")
