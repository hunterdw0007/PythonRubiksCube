'''
Created on Nov 7, 2022

@author: Hunter
'''
import rubik.rotate as rotate

def _checkTopLayer(cube):
    #Returns true if the top layer is solved regardless of the state of the rest of the cube
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
    #Returns true if all the top layer corners are solved based on the fact that all their "sides" match the side color
    corners = [ cube[rotate.cubeEnum.F00.value], cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.F02.value]
              , cube[rotate.cubeEnum.R00.value], cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.R02.value]
              , cube[rotate.cubeEnum.B00.value], cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.B02.value]
              , cube[rotate.cubeEnum.L00.value], cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.L02.value]]
    
    if corners[0:3].count(cube[rotate.cubeEnum.F11.value]) != 3:
        return False
    if corners[3:6].count(cube[rotate.cubeEnum.R11.value]) != 3:
        return False
    if corners[6:9].count(cube[rotate.cubeEnum.B11.value]) != 3:
        return False
    if corners[9:12].count(cube[rotate.cubeEnum.L11.value]) != 3:
        return False
    return True

def _positionTopCorners(cube, rotations):
    #Returns a cube with solved corners in the correct positions
    newCube = cube
    while not _checkTopCorners(cube):
        rotations += 'U'
        newCube = rotate._rotate({'cube':newCube,'dir':'U'}).get('cube')
        
    cube = newCube if newCube != cube else cube
    return cube, rotations
        