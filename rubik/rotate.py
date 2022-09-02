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
        rotatedCube = encodedCube                  #STUB:  rotate the cube
        result['cube'] = 'orgowobgrowwwrwggwrbgrybgorywyroybyorobbbgbyywrwbgyygo'               
        result['status'] = 'ok'                     
    return result

def _validateCube(cube):
    validColors = 'wryobg'
    centerColors = ''

    if len(cube) != 54 or cube == None:
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