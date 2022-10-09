import rubik.cube as rubik

def _verify(parms):
    return parms


def _validateCube(cube):
    validColors = 'wryobg'
    centerColors = ''

    if cube == None:
        return False

    if len(cube) != 54:
        return False
    
    for color in validColors:
        if cube.count(color) != 9:
            return False
    
    for i, color in enumerate(cube):
        if validColors.count(color) != 1:
            return False
        if i % 9 == 4:
            if centerColors.count(color) != 0:
                return False
            else:
                centerColors += color
    
    return True

def _validateDir(direction):
    validDirs = 'FfRrLlUuDdBb'
    
    if direction == None: 
        return True
    
    for d in direction:
        if validDirs.count(d) == 0:
            return False
    return True
