'''
Created on Oct 24, 2022

@author: Hunter
'''

import rubik.rotate as rotate

def _checkTopCross( cube ):
    # Returns true if the top cross is solved, including edges being on the correct side
    topEdges = [ cube[rotate.cubeEnum.U11.value]
               , cube[rotate.cubeEnum.U01.value], cube[rotate.cubeEnum.U10.value]
               , cube[rotate.cubeEnum.U12.value], cube[rotate.cubeEnum.U21.value] ]
    
    if topEdges.count(topEdges[0]) != len(topEdges):
        return False
    
    # Side faces
    if cube[rotate.cubeEnum.F01.value] != cube[rotate.cubeEnum.F11.value]:
        return False
    if cube[rotate.cubeEnum.R01.value] != cube[rotate.cubeEnum.R11.value]:
        return False
    if cube[rotate.cubeEnum.R01.value] != cube[rotate.cubeEnum.R11.value]:
        return False
    if cube[rotate.cubeEnum.R01.value] != cube[rotate.cubeEnum.R11.value]:
        return False
    return True

def _checkCrossState( cube ):
    # Returns the number of rotations needed to orient the top in order to perform the algorithm
    # Special case for if the cross is already solved returns -1
    topEdges = [ cube[rotate.cubeEnum.U11.value]
               , cube[rotate.cubeEnum.U01.value], cube[rotate.cubeEnum.U10.value]
               , cube[rotate.cubeEnum.U12.value], cube[rotate.cubeEnum.U21.value] ]
    
    # Cross solved
    if topEdges.count(topEdges[0]) != len(topEdges):
        return -1
    # Case 0: horizontal line, L in position
    if topEdges[1] == topEdges[2] or topEdges[0] == topEdges[1]:
        return 0
    # Case 2: line vertical, L in bottom left
    if topEdges[0] == topEdges[3] or topEdges[1] == topEdges[3]:
        return 1
    #Case 3: L in bottom right
    if topEdges[2] == topEdges[3]:
        return 2
    # Case 4: L in top right
    if topEdges[0] == topEdges[2]:
        return 3
    # Case 5: No edges
    return 0

def _orientTopEdges( cube, rotations ):
    # Returns cube with top cross in position but edges not aligned to their color
    rotationCount = _checkCrossState(cube)
    
    if rotationCount == -1:
    # Base case when the cross is solved
        return cube, rotations
    else:
        rotations += 'U' * rotationCount + 'FRUruf'
        cube = cube = rotate._rotate({'cube':cube,'dir':'U' * rotationCount + 'FRUruf'}).get('cube')
    
    return _orientTopEdges(cube, rotations)
        
    