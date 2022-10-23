import rubik.rotate as rotate

def _solveMiddleLayer(cube, rotations):
    # Takes in a cube with solved bottom layer and solves the middle layer
    # Returns the cube state and the string of rotations to produce it
    if _checkMiddleLayer(cube):
        return cube, rotations
    
    # Case 1: Piece is located in the top
    location = _locateMiddlePieceInTop(cube)
    
    # Case 2: Piece is located in the middle
    if location == -1:
        location = _locateMiddlePieceInMiddle(cube)
        cube, location, mvRots = _moveMiddlePieceToTop(cube, location)
        rotations += mvRots
        
    cube, location, posRots = _positionMiddlePieceInTop(cube, location)
    rotations += posRots
            
    if _chooseAlgorithmDirection(cube, location):
        cube, algRots = _middleAlgorithmRight(cube, location)
        rotations += algRots
    else:
        cube, algRots = _middleAlgorithmLeft(cube, location)
        rotations += algRots
        
    return _solveMiddleLayer(cube, rotations)

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
    # Finds the first piece in the top row that contains colors corresponding to two adjacent sides and returns its location
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
    # Moves an edge piece in the top until it lines up with its matching side
    # Returns the cube state, the new location, and the rotations to get that state
    rotations = ''
    
    while cube[location] != cube[location + 3]:
        rotations = rotations + 'U'
        cube = rotate._rotate({'cube':cube,'dir':'U'}).get('cube')
        location = location - 9 if location != rotate.cubeEnum.F01.value else rotate.cubeEnum.L01.value
        
    return cube, location, rotations

def _locateMiddlePieceInMiddle(cube):
    # Finds the first piece in the middle layer which is either in the wrong position, or "flipped" but otherwise in the right position
    # Returns the location of that piece
    expectedMiddles = [ (cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.R11.value])
                      , (cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.B11.value])
                      , (cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.L11.value])
                      , (cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.F11.value]) ]
    
    actualMiddles = [ (cube[rotate.cubeEnum.F12.value], cube[rotate.cubeEnum.R10.value])
                    , (cube[rotate.cubeEnum.R12.value], cube[rotate.cubeEnum.B10.value])
                    , (cube[rotate.cubeEnum.B12.value], cube[rotate.cubeEnum.L10.value])
                    , (cube[rotate.cubeEnum.L12.value], cube[rotate.cubeEnum.F10.value]) ]
    
    location = -1
    
    for i, middle in enumerate(actualMiddles):
        if middle != expectedMiddles[i] and middle.count(cube[rotate.cubeEnum.U11.value]) < 1:
            location = i * 9 + 5
            break
    
    return location

def _moveMiddlePieceToTop(cube, location):
    # Given the location of a piece in the middle layer which is misplaced, it moves it to the top layer
    # Returns the new cube state, location of the piece moved, and the rotations it took
    cube, rotations = _middleAlgorithmRight(cube, location - 4)
    
    if location == rotate.cubeEnum.F12.value:
        location = rotate.cubeEnum.B01.value
    elif location == rotate.cubeEnum.R12.value:
        location = rotate.cubeEnum.L01.value
    elif location == rotate.cubeEnum.B12.value:
        location = rotate.cubeEnum.F01.value
    else:
        location = rotate.cubeEnum.R01.value
        
    return cube, location, rotations

def _middleAlgorithmRight(cube, location):
    # Performs the algorithm to move a middle edge from the top to the middle, moving the piece right
    # Returns the new cube state, and the rotations of the algorithm
    rotations = ''
    
    if location == rotate.cubeEnum.F01.value:
        rotations = 'URurufUF'
    elif location == rotate.cubeEnum.R01.value:
        rotations = 'UBuburUR'
    elif location == rotate.cubeEnum.B01.value:
        rotations = 'ULulubUB'
    else:
        rotations = 'UFufulUL'
    
    cube = rotate._rotate({'cube':cube,'dir':rotations}).get('cube')
    
    return cube, rotations

def _middleAlgorithmLeft(cube, location):
    # Performs the algorithm to move a middle edge from the top to the middle, moving the piece left
    # Returns the new cube state, and the rotations of the algorithm
    rotations = ''
    
    if location == rotate.cubeEnum.F01.value:
        rotations = 'ulULUFuf'
    elif location == rotate.cubeEnum.R01.value:
        rotations = 'ufUFURur'
    elif location == rotate.cubeEnum.B01.value:
        rotations = 'urURUBub'
    else:
        rotations = 'ubUBULul'
    
    cube = rotate._rotate({'cube':cube,'dir':rotations}).get('cube')
    
    return cube, rotations

def _chooseAlgorithmDirection(cube, location):
    # Given the location of a piece needing to be moved from the top to the middle
    # Returns the direction of the algorithm needed to move it correctly
    if location == rotate.cubeEnum.F01.value:
        if cube[rotate.cubeEnum.U21.value] == cube[rotate.cubeEnum.L11.value]:
            return False
    elif location == rotate.cubeEnum.R01.value:
        if cube[rotate.cubeEnum.U12.value] == cube[rotate.cubeEnum.F11.value]:
            return False
    elif location == rotate.cubeEnum.B01.value:
        if cube[rotate.cubeEnum.U01.value] == cube[rotate.cubeEnum.R11.value]:
            return False
    else:
        if cube[rotate.cubeEnum.U10.value] == cube[rotate.cubeEnum.B11.value]:
            return False
    
    return True