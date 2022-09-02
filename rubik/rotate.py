import rubik.cube as rubik
import re

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube')
    encodedDir = parms.get('dir')
    
    if not _validateCube(encodedCube):
        result['status'] = 'error: invalid cube'
    elif not _validateDir(encodedDir):
        result['status'] = 'error: invalid rotation'
    else:
        cubeRot = list(encodedCube)
        
        if encodedDir == 'F':
            offset = 0
            faceRot = _faceCW(''.join(cubeRot[0:9]))
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
            
            # Right Edges
            cubeRot[47] = encodedCube[ 9]
            cubeRot[46] = encodedCube[12]
            cubeRot[45] = encodedCube[15]
            # Left Edges
            cubeRot[44] = encodedCube[29]
            cubeRot[43] = encodedCube[32]
            cubeRot[42] = encodedCube[35]
            # Top Edges
            cubeRot[ 9] = encodedCube[42]
            cubeRot[12] = encodedCube[43]
            cubeRot[15] = encodedCube[44]
            # Bottom Edges
            cubeRot[29] = encodedCube[45]
            cubeRot[32] = encodedCube[46]
            cubeRot[35] = encodedCube[47]
            
        elif encodedDir == 'f':
            offset = 0
            faceRot = _faceCCW(''.join(cubeRot[0:9]))
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Right Edges
            cubeRot[42] = encodedCube[ 9]
            cubeRot[43] = encodedCube[12]
            cubeRot[44] = encodedCube[15]
            # Left Edges
            cubeRot[45] = encodedCube[29]
            cubeRot[46] = encodedCube[32]
            cubeRot[47] = encodedCube[35]
            # Top Edges
            cubeRot[35] = encodedCube[42]
            cubeRot[32] = encodedCube[43]
            cubeRot[29] = encodedCube[44]
            # Bottom Edges
            cubeRot[15] = encodedCube[45]
            cubeRot[12] = encodedCube[46]
            cubeRot[ 9] = encodedCube[47]
            
        result['cube'] = ''.join(cubeRot)          
        result['status'] = 'ok'                     
    return result

def _validateCube(cube):
    validColors = 'wryobg'
    centerColors = ''

    if cube == None:
        return False

    if len(cube) != 54:
        return False
    
    for color in validColors:
        if cube.count(color) != 9:
            return False
    
    for i, color in enumerate(cube):
        if validColors.count(color) != 1:
            return False
        if i % 9 == 4:
            if centerColors.count(color) != 0:
                return False
            else:
                centerColors += color
    
    return True

def _faceCW(face):
    newFace = list(face)
    
    newFace[2] = face[0]
    newFace[5] = face[1]
    newFace[8] = face[2]
    newFace[1] = face[3]
    # center stays at the same position
    newFace[7] = face[5]
    newFace[0] = face[6]
    newFace[3] = face[7]
    newFace[6] = face[8]
    
    return ''.join(newFace);

def _faceCCW(face):
    newFace = list(face)
    
    newFace[6] = face[0]
    newFace[3] = face[1]
    newFace[0] = face[2]
    newFace[7] = face[3]
    # center stays at the same position
    newFace[1] = face[5]
    newFace[8] = face[6]
    newFace[5] = face[7]
    newFace[2] = face[8]
    
    return ''.join(newFace);

def _validateDir(dir):
    validDirs = 'FfRrLlUuDdBb'
    
    for d in dir:
        if validDirs.count(d) == 0:
            return False
    return True