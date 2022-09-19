import rubik.cube as rubik
import rubik.rotate as rotate
import math

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    if not rotate._validateCube(parms.get('cube', None)):
        result['status'] = 'error: invalid cube'
    else:
        solution = _solveBottomCross(parms.get('cube'), '')
        result['solution'] = solution
        result['status'] = 'ok'                   
    return result

def _solveBottomCross(cube, solution):
    # Base Case: check if bottom cross is solved
    if _checkBottomCross(cube):
        return solution
    
    rotations = ''
    location = 0
    
    _solveEdgeInBottom(cube, location, rotations, solution)
    
    # Used to check for correctness/incorrectness of edge pairs
    sideEdgePairs = [ (rotate.cubeEnum.F12.value, rotate.cubeEnum.R10.value, 'f', 'R')
                    , (rotate.cubeEnum.R12.value, rotate.cubeEnum.B10.value, 'r', 'B')
                    , (rotate.cubeEnum.B12.value, rotate.cubeEnum.L10.value, 'b', 'L')
                    , (rotate.cubeEnum.L12.value, rotate.cubeEnum.F10.value, 'l', 'F') ]
    
    for side, edge in enumerate(sideEdgePairs):
    #Case 4: Edge in side - bottom color on left
        if cube[edge[0]] == cube[rotate.cubeEnum.D11.value]:
            rotations += edge[3]
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            if edge[3] == 'F':
                location = rotate.cubeEnum.F01.value
            elif edge[3] == 'R':
                location = rotate.cubeEnum.R01.value
            elif edge[3] == 'B':
                location = rotate.cubeEnum.B01.value
            else:
                location = rotate.cubeEnum.L01.value
            
            # Position the edge where it needs to be in the top
            cube, location, upRotations = _positionEdgeInTop(cube, location)
            rotations += upRotations
            
            rotations += edge[3].lower()
            cube = rotate._rotate({'cube':cube,'dir':edge[3].lower()})['cube']
            
            # Flip the edge from the top to the bottom
            cube, location, downRotations = _flipEdgeToBottomFromTop(cube, location)
            rotations += downRotations
            
            return _solveBottomCross(cube, solution + rotations)
            
    #Case 5: Edge in side - bottom color on right
        elif cube[edge[1]] == cube[rotate.cubeEnum.D11.value]:
            rotations += edge[2]
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            if edge[2] == 'f':
                location = rotate.cubeEnum.F01.value
            elif edge[2] == 'r':
                location = rotate.cubeEnum.R01.value
            elif edge[2] == 'b':
                location = rotate.cubeEnum.B01.value
            else:
                location = rotate.cubeEnum.L01.value
            
            # Position the edge where it needs to be in the top
            cube, location, upRotations = _positionEdgeInTop(cube, location)
            rotations += upRotations
            
            rotations += edge[2].upper()
            cube = rotate._rotate({'cube':cube,'dir':edge[2].upper()})['cube']
            
            # Flip the edge from the top to the bottom
            cube, location, downRotations = _flipEdgeToBottomFromTop(cube, location)
            rotations += downRotations
            
            return _solveBottomCross(cube, solution + rotations)

def _checkBottomCross(cube):
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
    rotations = ''
    while cube[location] != cube[location+3]:
        rotations = rotations + 'U'
        cube = rotate._rotate({'cube':cube,'dir':'U'})['cube']
        location = location - 9 if location != rotate.cubeEnum.F01.value else rotate.cubeEnum.L01.value
        
    return cube, location, rotations

def _flipEdgeToBottomFromTop(cube, location):
    rotations = ''
    if math.floor(location/9) == 0:
        rotations = rotations + 'FF'
        cube = rotate._rotate({'cube':cube,'dir':'FF'})['cube']
    elif math.floor(location / 9) == 1:
        rotations = rotations + 'RR'
        cube = rotate._rotate({'cube':cube,'dir':'RR'})['cube']
    elif math.floor(location / 9) == 2:
        rotations = rotations + 'BB'
        cube = rotate._rotate({'cube':cube,'dir':'BB'})['cube']
    else:
        rotations = rotations + 'LL'
        cube = rotate._rotate({'cube':cube,'dir':'LL'})['cube']
        
    return cube, location, rotations

def _solveEdgeInBottom(cube, location, rotations, solution):
    # Used to check for correctness/incorrectness of edge pairs
    bottomEdgePairs = [ (rotate.cubeEnum.D01.value, rotate.cubeEnum.F21.value, 'F')
                      , (rotate.cubeEnum.D12.value, rotate.cubeEnum.R21.value, 'R')
                      , (rotate.cubeEnum.D21.value, rotate.cubeEnum.B21.value, 'B')
                      , (rotate.cubeEnum.D10.value, rotate.cubeEnum.L21.value, 'L') ]
    
    # keeps track of the colors of each side
    sideColors = [cube[rotate.cubeEnum.F11.value],cube[rotate.cubeEnum.R11.value],cube[rotate.cubeEnum.B11.value],cube[rotate.cubeEnum.L11.value]]
    
    for side, edge in enumerate(bottomEdgePairs):
    # Case 2: Edge in bottom flipped
        if cube[edge[0]] == sideColors[side] and cube[edge[1]] == cube[rotate.cubeEnum.D11.value]:
            if edge[2] == 'F':
                rotations += 'Fl'
                location = rotate.cubeEnum.L01.value
            elif edge[2] == 'R':
                rotations += 'Rf'
                location = rotate.cubeEnum.F01.value
            elif edge[2] == 'B':
                rotations += 'Br'
                location = rotate.cubeEnum.R01.value
            else:
                rotations += 'Lb'
                location = rotate.cubeEnum.B01.value
                
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            # Position the edge where it needs to be in the top
            cube, location, upRotations = _positionEdgeInTop(cube, location)
            rotations = rotations + upRotations
            
            # Reset the side that was rotated so that nothing is messed up
            rotations = rotations + rotations[1].upper()
            cube = rotate._rotate({'cube':cube,'dir':rotations[1].upper()})['cube']
            
            # Flip the edge from the top to the bottom
            cube, location, downRotations = _flipEdgeToBottomFromTop(cube, location)
            rotations = rotations + downRotations
            
            # Recursive call to complete the cube solution
            return _solveBottomCross(cube, solution + rotations)
          
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
            
            # Position the edge where it needs to be in the top
            cube, location, upRotations = _positionEdgeInTop(cube, location)
            rotations = rotations + upRotations

            # Flip the edge from the top to the bottom
            cube, location, downRotations = _flipEdgeToBottomFromTop(cube, location)
            rotations = rotations + downRotations
                
            return _solveBottomCross(cube, solution + rotations)
                