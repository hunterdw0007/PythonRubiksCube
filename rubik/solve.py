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
    if (cube[rotate.cubeEnum.D11.value] == \
    (   cube[rotate.cubeEnum.D01.value] 
    and cube[rotate.cubeEnum.D10.value] 
    and cube[rotate.cubeEnum.D12.value] 
    and cube[rotate.cubeEnum.D21.value] ))\
    and cube[rotate.cubeEnum.F11.value] == cube[rotate.cubeEnum.F21.value]\
    and cube[rotate.cubeEnum.R11.value] == cube[rotate.cubeEnum.R21.value]\
    and cube[rotate.cubeEnum.B11.value] == cube[rotate.cubeEnum.B21.value]\
    and cube[rotate.cubeEnum.L11.value] == cube[rotate.cubeEnum.L21.value]:
        return solution
    
    # Used to check for correctness/incorrectness of edge pairs
    bottomEdgePairs = [ (rotate.cubeEnum.D01.value, rotate.cubeEnum.F21.value, 'F')
                      , (rotate.cubeEnum.D12.value, rotate.cubeEnum.R21.value, 'R')
                      , (rotate.cubeEnum.D21.value, rotate.cubeEnum.B21.value, 'B')
                      , (rotate.cubeEnum.D10.value, rotate.cubeEnum.L21.value, 'L') ]
    
    # keeps track of the colors of each side
    sideColors = [cube[rotate.cubeEnum.F11.value],cube[rotate.cubeEnum.R11.value],cube[rotate.cubeEnum.B11.value],cube[rotate.cubeEnum.L11.value]]
    
    rotations = ''
    location = 0
    
    for side, edge in enumerate(bottomEdgePairs):
    # Case 2: Edge in bottom flipped
        if cube[edge[0]] == sideColors[side] and cube[edge[1]] == cube[rotate.cubeEnum.D11.value]:
            if edge[2] == 'F':
                rotations = 'Fl'
                location = rotate.cubeEnum.L01.value
            elif edge[2] == 'R':
                rotations = 'Rf'
                location = rotate.cubeEnum.F01.value
            elif edge[2] == 'B':
                rotations = 'Br'
                location = rotate.cubeEnum.R01.value
            else:
                rotations = 'Lb'
                location = rotate.cubeEnum.B01.value
                
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            cube, location, upRotations = _positionEdgeInTop(cube, location)
            
            rotations = rotations + upRotations
            
            rotations = rotations + rotations[1].upper()
            cube = rotate._rotate({'cube':cube,'dir':rotations[1].upper()})['cube']
            
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
                
            return _solveBottomCross(cube, rotations)
            
    # Case 3: edge in bottom, wrong spot
        elif cube[edge[0]] == cube[rotate.cubeEnum.D11.value] and cube[edge[1]] != sideColors[side]:
            if edge[2] == 'F':
                rotations = 'FF'
                location = rotate.cubeEnum.F01.value
            elif edge[2] == 'R':
                rotations = 'RR'
                location = rotate.cubeEnum.R01.value
            elif edge[2] == 'B':
                rotations = 'BB'
                location = rotate.cubeEnum.B01.value
            else:
                rotations = 'LL'
                location = rotate.cubeEnum.L01.value
                
            cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
            
            cube, location, upRotations = _positionEdgeInTop(cube, location)
            
            rotations = rotations + upRotations
        
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
                
            return _solveBottomCross(cube, rotations)
                
                
def _positionEdgeInTop(cube, location):
    rotations = ''
    while cube[location] != cube[location+3]:
        rotations = rotations + 'U'
        cube = rotate._rotate({'cube':cube,'dir':'U'})['cube']
        location = location - 9 if location != rotate.cubeEnum.F01.value else rotate.cubeEnum.L01.value
        
    return cube, location, rotations
                
                