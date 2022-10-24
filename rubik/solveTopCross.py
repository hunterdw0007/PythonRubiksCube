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
    
    if topEdges.count(topEdges[0]) == 4:
        return 0
    return 1
        