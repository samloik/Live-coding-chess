def contains(usedList: list, coordsToCheck):
    coordInListFlag = False
    for coord in usedList:
        if str(coord) == str(coordsToCheck):
            coordInListFlag = True
    return coordInListFlag