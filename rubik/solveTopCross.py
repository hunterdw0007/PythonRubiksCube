'''
Created on Oct 24, 2022

@author: Hunter
'''

import rubik.rotate as rotate

def _checkTopCross( cube ):
    # Returns true if the top cross is solved, including edges being on the correct side
    if cube[rotate.cubeEnum.U01.value] != cube[rotate.cubeEnum.U11.value]:
        return False
    if cube[rotate.cubeEnum.U10.value] != cube[rotate.cubeEnum.U11.value]:
        return False
    if cube[rotate.cubeEnum.U12.value] != cube[rotate.cubeEnum.U11.value]:
        return False
    if cube[rotate.cubeEnum.U21.value] != cube[rotate.cubeEnum.U11.value]:
        return False
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
    
    topEdges = [ cube[rotate.cubeEnum.U01.value], cube[rotate.cubeEnum.U10.value]
               , cube[rotate.cubeEnum.U12.value], cube[rotate.cubeEnum.U21.value]]
    
    # Case 1: Cross, horizontal line, L in position
    if topEdges.count(topEdges[0]) == len(topEdges) or topEdges[1] == topEdges[2] or topEdges[0] == topEdges[1]:
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