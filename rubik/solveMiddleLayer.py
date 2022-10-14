import rubik.rotate as rotate

def _solveMiddleLayer():
    return True

def _checkMiddleLayer(cube):
    # Checks whether or not the middle edges are solved independent of any other part of the cube being solved
    if cube[rotate.cubeEnum.F10.value] != cube[rotate.cubeEnum.F11.value]:
        return False
    if cube[rotate.cubeEnum.F12.value] != cube[rotate.cubeEnum.F11.value]:
        return False
    if cube[rotate.cubeEnum.R10.value] != cube[rotate.cubeEnum.R11.value]:
        return False
    if cube[rotate.cubeEnum.R12.value] != cube[rotate.cubeEnum.R11.value]:
        return False
    if cube[rotate.cubeEnum.B10.value] != cube[rotate.cubeEnum.B11.value]:
        return False
    if cube[rotate.cubeEnum.B12.value] != cube[rotate.cubeEnum.B11.value]:
        return False
    if cube[rotate.cubeEnum.L10.value] != cube[rotate.cubeEnum.L11.value]:
        return False
    if cube[rotate.cubeEnum.L12.value] != cube[rotate.cubeEnum.L11.value]:
        return False
    return True

def _locateMiddlePieceInTop(cube):
    
    sortedEdgeColors = [ sorted((cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.R11.value]))
                       , sorted((cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.B11.value]))
                       , sorted((cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.L11.value]))
                       , sorted((cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.F11.value])) ]
    
    topEdgeColors = [ (cube[rotate.cubeEnum.F01.value], cube[rotate.cubeEnum.U21.value])
                    , (cube[rotate.cubeEnum.R01.value], cube[rotate.cubeEnum.U12.value])
                    , (cube[rotate.cubeEnum.B01.value], cube[rotate.cubeEnum.U01.value])
                    , (cube[rotate.cubeEnum.L01.value], cube[rotate.cubeEnum.U10.value]) ]
    
    location = -1
    
    for i, topEdge in enumerate(topEdgeColors):
        if sortedEdgeColors.count(sorted(topEdge)) > 0:
            location = i * 9 + 1
            break
        
    return location

def _positionMiddlePieceInTop(cube, location):
    rotations = ''
    return cube, location, rotations