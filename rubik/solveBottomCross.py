import rubik.rotate as rotate

def _solveBottomCross(cube, solution):
    # Returns the rotations needed to take a given cube and produce a cube with a solved bottom cross
    # Base Case: check if bottom cross is solved
    if _checkBottomCross(cube):
        return cube, solution
        
    rotations = ''
    
    cube, location, mvRots = _movePieceFromBottom(cube)
    rotations += mvRots
    
    if location == -1:
        cube, location, mvRots = _movePieceFromSide(cube)
        rotations += mvRots
        
    if location == -1:
        cube, location, rotations = _movePieceFromTop(cube)
    
    # Position the edge where it needs to be in the top
    cube, location, upRotations = _positionEdgeInTop(cube, location)
    rotations += upRotations
    
    # Flip the edge from the top to the bottom
    cube, location, downRotations = _flipEdgeToBottomFromTop(cube, location)
    rotations += downRotations
    
    return _solveBottomCross(cube, solution + rotations)
    

def _checkBottomCross(cube):
    # Checks whether or not the bottom cross is solved
    if cube[rotate.cubeEnum.F11.value] != cube[rotate.cubeEnum.F21.value]:
        return False
    if cube[rotate.cubeEnum.R11.value] != cube[rotate.cubeEnum.R21.value]:
        return False
    if cube[rotate.cubeEnum.B11.value] != cube[rotate.cubeEnum.B21.value]:
        return False
    if cube[rotate.cubeEnum.L11.value] != cube[rotate.cubeEnum.L21.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D01.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D10.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D12.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D21.value]:
        return False
    # If it makes it here then it's all correct
    return True

def _positionEdgeInTop(cube, location):
    # Correctly positions an edge in the top row of the cube to be able to place it in the bottom cross

    rotations = ''
    while cube[location] != cube[location+3]:
        rotations = rotations + 'U'
        cube = rotate._rotate({'cube':cube,'dir':'U'})['cube']
        location = location - 9 if location != rotate.cubeEnum.F01.value else rotate.cubeEnum.L01.value
        
    return cube, location, rotations

def _flipEdgeToBottomFromTop(cube, location):
    # Flips an edge from being in the top of the cube to being in the bottom of the cube
    rotations = ''
    if location == rotate.cubeEnum.F01.value:
        rotations = rotations + 'FF'
        cube = rotate._rotate({'cube':cube,'dir':'FF'})['cube']
    elif location == rotate.cubeEnum.R01.value:
        rotations = rotations + 'RR'
        cube = rotate._rotate({'cube':cube,'dir':'RR'})['cube']
    elif location == rotate.cubeEnum.B01.value:
        rotations = rotations + 'BB'
        cube = rotate._rotate({'cube':cube,'dir':'BB'})['cube']
    else:
        rotations = rotations + 'LL'
        cube = rotate._rotate({'cube':cube,'dir':'LL'})['cube']
        
    return cube, location, rotations

def _movePieceFromBottom(cube):
    
    # Used to check for correctness/incorrectness of edge pairs
    bottomEdgePairs = [ (rotate.cubeEnum.D01.value, rotate.cubeEnum.F21.value, 'F')
                      , (rotate.cubeEnum.D12.value, rotate.cubeEnum.R21.value, 'R')
                      , (rotate.cubeEnum.D21.value, rotate.cubeEnum.B21.value, 'B')
                      , (rotate.cubeEnum.D10.value, rotate.cubeEnum.L21.value, 'L') ]
    
    # keeps track of the colors of each side
    sideColors = [cube[rotate.cubeEnum.F11.value],cube[rotate.cubeEnum.R11.value],cube[rotate.cubeEnum.B11.value],cube[rotate.cubeEnum.L11.value]]
    
    rotations = ''
    location = -1
    
    for side, edge in enumerate(bottomEdgePairs):
    # Case 2: Edge in bottom flipped
        if cube[edge[0]] == sideColors[side] and cube[edge[1]] == cube[rotate.cubeEnum.D11.value]:
            if edge[2] == 'F':
                rotations += 'FlUL'
                location = rotate.cubeEnum.B01.value
            elif edge[2] == 'R':
                rotations += 'RfUF'
                location = rotate.cubeEnum.L01.value
            elif edge[2] == 'B':
                rotations += 'BrUR'
                location = rotate.cubeEnum.F01.value
            else:
                rotations += 'LbUB'
                location = rotate.cubeEnum.R01.value
                
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            return cube, location, rotations
          
    # Case 3: edge in bottom, wrong spot
        elif cube[edge[0]] == cube[rotate.cubeEnum.D11.value] and cube[edge[1]] != sideColors[side]:
            if edge[2] == 'F':
                rotations += 'FF'
                location = rotate.cubeEnum.F01.value
            elif edge[2] == 'R':
                rotations += 'RR'
                location = rotate.cubeEnum.R01.value
            elif edge[2] == 'B':
                rotations += 'BB'
                location = rotate.cubeEnum.B01.value
            else:
                rotations += 'LL'
                location = rotate.cubeEnum.L01.value
                
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            return cube, location, rotations

    return cube, location, rotations

def _movePieceFromSide(cube):
    # Used to check for correctness/incorrectness of edge pairs
    sideEdgePairs = [ (rotate.cubeEnum.F12.value, rotate.cubeEnum.R10.value, 'f', 'R')
                    , (rotate.cubeEnum.R12.value, rotate.cubeEnum.B10.value, 'r', 'B')
                    , (rotate.cubeEnum.B12.value, rotate.cubeEnum.L10.value, 'b', 'L')
                    , (rotate.cubeEnum.L12.value, rotate.cubeEnum.F10.value, 'l', 'F') ]
    
    rotations = ''
    location = -1
    
    for edge in sideEdgePairs:
    #Case 4: Edge in side - bottom color on left
        if cube[edge[0]] == cube[rotate.cubeEnum.D11.value]:
            
            if edge[3] == 'F':
                location = rotate.cubeEnum.L01.value
            elif edge[3] == 'R':
                location = rotate.cubeEnum.F01.value
            elif edge[3] == 'B':
                location = rotate.cubeEnum.R01.value
            else:
                location = rotate.cubeEnum.B01.value
                
            rotations += edge[3] + 'U' + edge[3].lower()
            cube = rotate._rotate({'cube':cube,'dir':edge[3] + 'U' + edge[3].lower()})['cube']
            
            return cube, location, rotations
            
    #Case 5: Edge in side - bottom color on right
        elif cube[edge[1]] == cube[rotate.cubeEnum.D11.value]:
            
            if edge[2] == 'f':
                location = rotate.cubeEnum.R01.value
            elif edge[2] == 'r':
                location = rotate.cubeEnum.B01.value
            elif edge[2] == 'b':
                location = rotate.cubeEnum.L01.value
            else:
                location = rotate.cubeEnum.F01.value
                
            rotations += edge[2] + 'u' + edge[2].upper()
            cube = rotate._rotate({'cube':cube,'dir':edge[2] + 'u' + edge[2].upper()})['cube']
            
            return cube, location, rotations
    
    return cube, location, rotations

def _movePieceFromTop(cube):
    # Used to check for correctness/incorrectness of edge pairs
    topEdgePairs = [ (rotate.cubeEnum.F01.value, rotate.cubeEnum.U21.value, 'F')
                   , (rotate.cubeEnum.R01.value, rotate.cubeEnum.U12.value, 'R')
                   , (rotate.cubeEnum.B01.value, rotate.cubeEnum.U01.value, 'B')
                   , (rotate.cubeEnum.L01.value, rotate.cubeEnum.U10.value, 'L') ]
    
    rotations = ''
    location = -1
    
    for edge in topEdgePairs:
        # Color on top of the edge is the same as the bottom side's color
        if cube[edge[1]] == cube[rotate.cubeEnum.D11.value]:
            return cube, edge[0], rotations
        
        elif cube[edge[0]] == cube[rotate.cubeEnum.D11.value]:
            # "Flip" edge to the right orientation
            if edge[2] == 'F':
                rotations += 'FRurf'
                location = rotate.cubeEnum.B01.value
            elif edge[2] == 'R':
                rotations += 'RBubr'
                location = rotate.cubeEnum.L01.value
            elif edge[2] == 'B':
                rotations += 'BLulb'
                location = rotate.cubeEnum.F01.value
            else:
                rotations += 'LFufl'
                location = rotate.cubeEnum.R01.value
                
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            return cube, location, rotations
        
    return cube, location, rotations