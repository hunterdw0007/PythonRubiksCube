'''
Created on Nov 7, 2022

@author: Hunter
'''
import rubik.rotate as rotate

def _checkTopLayer(cube):
    # Returns true if the top layer is solved regardless of the state of the rest of the cube
    topPieces = [ cube[rotate.cubeEnum.U00.value], cube[rotate.cubeEnum.U01.value], cube[rotate.cubeEnum.U02.value]
                , cube[rotate.cubeEnum.U10.value], cube[rotate.cubeEnum.U11.value], cube[rotate.cubeEnum.U12.value]
                , cube[rotate.cubeEnum.U20.value], cube[rotate.cubeEnum.U21.value], cube[rotate.cubeEnum.U22.value] ]
    
    edgePieces = [ cube[rotate.cubeEnum.F00.value], cube[rotate.cubeEnum.F01.value], cube[rotate.cubeEnum.F02.value]
                 , cube[rotate.cubeEnum.R00.value], cube[rotate.cubeEnum.R01.value], cube[rotate.cubeEnum.R02.value]
                 , cube[rotate.cubeEnum.B00.value], cube[rotate.cubeEnum.B01.value], cube[rotate.cubeEnum.B02.value]
                 , cube[rotate.cubeEnum.L00.value], cube[rotate.cubeEnum.L01.value], cube[rotate.cubeEnum.L02.value]]

    if topPieces.count(topPieces[4]) != len(topPieces):
        return False
    if edgePieces[0:3].count(cube[rotate.cubeEnum.F11.value]) != 3:
        return False
    if edgePieces[3:6].count(cube[rotate.cubeEnum.R11.value]) != 3:
        return False
    if edgePieces[6:9].count(cube[rotate.cubeEnum.B11.value]) != 3:
        return False
    if edgePieces[9:12].count(cube[rotate.cubeEnum.L11.value]) != 3:
        return False
    return True

def _checkTopCorners(cube):
    # Returns true if all the top layer corners are solved based on the fact that all their "sides" match
    if cube[rotate.cubeEnum.F00.value] != cube[rotate.cubeEnum.F02.value]:
        return False
    if cube[rotate.cubeEnum.R00.value] != cube[rotate.cubeEnum.R02.value]:
        return False
    if cube[rotate.cubeEnum.B00.value] != cube[rotate.cubeEnum.B02.value]:
        return False
    if cube[rotate.cubeEnum.L00.value] != cube[rotate.cubeEnum.L02.value]:
        return False
    return True

def _checkTopEdges(cube):
    # Returns true if all the top layer edges are solved based on the fact that their sides match
    edgePieces = [ cube[rotate.cubeEnum.F00.value], cube[rotate.cubeEnum.F01.value], cube[rotate.cubeEnum.F02.value]
                 , cube[rotate.cubeEnum.R00.value], cube[rotate.cubeEnum.R01.value], cube[rotate.cubeEnum.R02.value]
                 , cube[rotate.cubeEnum.B00.value], cube[rotate.cubeEnum.B01.value], cube[rotate.cubeEnum.B02.value]
                 , cube[rotate.cubeEnum.L00.value], cube[rotate.cubeEnum.L01.value], cube[rotate.cubeEnum.L02.value]]
     
    if edgePieces[0:3].count(edgePieces[0]) != 3:
        return False
    if edgePieces[3:6].count(edgePieces[3]) != 3:
        return False
    if edgePieces[6:9].count(edgePieces[6]) != 3:
        return False
    if edgePieces[9:12].count(edgePieces[9]) != 3:
        return False
    return True

def _locateTopCorners(cube):
    # Returns an integer representing the number of turns required to position the "headlights" at the back of the cube
    # If there are no headlights 0 is returned
    if cube[rotate.cubeEnum.L00.value] == cube[rotate.cubeEnum.L02.value]:
        return 1
    if cube[rotate.cubeEnum.F00.value] == cube[rotate.cubeEnum.F02.value]:
        return 2
    if cube[rotate.cubeEnum.R00.value] == cube[rotate.cubeEnum.R02.value]:
        return 3
    return 0

def _positionTopCorners(cube, rotations):
    # Returns a cube with solved corners in the correct positions
    if _checkTopCorners(cube):
        return cube, rotations
    
    rotationCount = _locateTopCorners(cube)
    
    rotations += 'U' * rotationCount + 'rFrBBRfrBBRR'
    cube = rotate._rotate({'cube':cube,'dir':'U' * rotationCount + 'rFrBBRfrBBRR'}).get('cube')
        
    return cube, rotations