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
            
        if encodedDir == 'f':
            offset = 0
            faceRot = _faceCCW(cubeRot[0:9])
            
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
        
        elif encodedDir == 'R':
            offset = 9
            faceRot = _faceCW(cubeRot[9:18])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[38] = encodedCube[2]
            cubeRot[41] = encodedCube[5]
            cubeRot[44] = encodedCube[8]
            # Back Edges
            cubeRot[47] = encodedCube[24]
            cubeRot[50] = encodedCube[21]
            cubeRot[53] = encodedCube[18]
            # Up Edges
            cubeRot[18] = encodedCube[44]
            cubeRot[21] = encodedCube[41]
            cubeRot[24] = encodedCube[38]
            # Down Edges
            cubeRot[8] = encodedCube[53]
            cubeRot[5] = encodedCube[50]
            cubeRot[2] = encodedCube[47]
            
        elif encodedDir == 'r':
            offset = 9
            faceRot = _faceCCW(cubeRot[9:18])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[47] = encodedCube[2]
            cubeRot[50] = encodedCube[5]
            cubeRot[53] = encodedCube[8]
            # Back Edges
            cubeRot[38] = encodedCube[24]
            cubeRot[41] = encodedCube[21]
            cubeRot[44] = encodedCube[18]
            # Up Edges
            cubeRot[8] = encodedCube[44]
            cubeRot[5] = encodedCube[41]
            cubeRot[2] = encodedCube[38]
            # Down Edges
            cubeRot[18] = encodedCube[53]
            cubeRot[21] = encodedCube[50]
            cubeRot[24] = encodedCube[47]
            
        elif encodedDir == 'B':
            offset = 18
            faceRot = _faceCW(cubeRot[18:27])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Right Edges
            cubeRot[36] = encodedCube[11]
            cubeRot[37] = encodedCube[14]
            cubeRot[38] = encodedCube[17]
            # Left Edges
            cubeRot[51] = encodedCube[27]
            cubeRot[52] = encodedCube[30]
            cubeRot[53] = encodedCube[33]
            # Up Edges
            cubeRot[33] = encodedCube[36]
            cubeRot[30] = encodedCube[37]
            cubeRot[27] = encodedCube[38]
            # Down Edges
            cubeRot[17] = encodedCube[51]
            cubeRot[14] = encodedCube[52]
            cubeRot[11] = encodedCube[53]
            
        elif encodedDir == 'b':
            offset = 18
            faceRot = _faceCCW(cubeRot[18:27])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Right Edges
            cubeRot[53] = encodedCube[11]
            cubeRot[52] = encodedCube[14]
            cubeRot[51] = encodedCube[17]
            # Left Edges
            cubeRot[38] = encodedCube[27]
            cubeRot[37] = encodedCube[30]
            cubeRot[36] = encodedCube[33]
            # Up Edges
            cubeRot[11] = encodedCube[36]
            cubeRot[14] = encodedCube[37]
            cubeRot[17] = encodedCube[38]
            # Down Edges
            cubeRot[27] = encodedCube[51]
            cubeRot[30] = encodedCube[52]
            cubeRot[33] = encodedCube[53]
            
        elif encodedDir == 'L':
            offset = 27
            faceRot = _faceCW(cubeRot[27:36])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[45] = encodedCube[0]
            cubeRot[48] = encodedCube[3]
            cubeRot[51] = encodedCube[6]
            # Back Edges
            cubeRot[42] = encodedCube[20]
            cubeRot[39] = encodedCube[23]
            cubeRot[36] = encodedCube[26]
            # Up Edges
            cubeRot[0] = encodedCube[36]
            cubeRot[3] = encodedCube[39]
            cubeRot[6] = encodedCube[42]
            # Down Edges
            cubeRot[26] = encodedCube[45]
            cubeRot[23] = encodedCube[48]
            cubeRot[20] = encodedCube[51]
            
        elif encodedDir == 'l':
            offset = 27
            faceRot = _faceCCW(cubeRot[27:36])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[36] = encodedCube[0]
            cubeRot[39] = encodedCube[3]
            cubeRot[42] = encodedCube[6]
            # Back Edges
            cubeRot[51] = encodedCube[20]
            cubeRot[48] = encodedCube[23]
            cubeRot[45] = encodedCube[26]
            # Up Edges
            cubeRot[26] = encodedCube[36]
            cubeRot[23] = encodedCube[39]
            cubeRot[20] = encodedCube[42]
            # Down Edges
            cubeRot[0] = encodedCube[45]
            cubeRot[3] = encodedCube[48]
            cubeRot[6] = encodedCube[51]
        
        elif encodedDir == 'U':
            offset = 36
            faceRot = _faceCW(cubeRot[36:45])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[27] = encodedCube[0]
            cubeRot[28] = encodedCube[1]
            cubeRot[29] = encodedCube[2]
            # Right Edges
            cubeRot[0] = encodedCube[9]
            cubeRot[1] = encodedCube[10]
            cubeRot[2] = encodedCube[11]
            # Back Edges
            cubeRot[9] = encodedCube[18]
            cubeRot[10] = encodedCube[19]
            cubeRot[11] = encodedCube[20]
            # Left Edges
            cubeRot[18] = encodedCube[27]
            cubeRot[19] = encodedCube[28]
            cubeRot[20] = encodedCube[29]
            
        elif encodedDir == 'u':
            offset = 36
            faceRot = _faceCCW(cubeRot[36:45])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[9] = encodedCube[0]
            cubeRot[10] = encodedCube[1]
            cubeRot[11] = encodedCube[2]
            # Right Edges
            cubeRot[18] = encodedCube[9]
            cubeRot[19] = encodedCube[10]
            cubeRot[20] = encodedCube[11]
            # Back Edges
            cubeRot[27] = encodedCube[18]
            cubeRot[28] = encodedCube[19]
            cubeRot[29] = encodedCube[20]
            # Left Edges
            cubeRot[0] = encodedCube[27]
            cubeRot[1] = encodedCube[28]
            cubeRot[2] = encodedCube[29]
            
        elif encodedDir == 'D':
            offset = 45
            faceRot = _faceCW(cubeRot[45:54])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[15] = encodedCube[6]
            cubeRot[16] = encodedCube[7]
            cubeRot[17] = encodedCube[8]
            # Right Edges
            cubeRot[24] = encodedCube[15]
            cubeRot[25] = encodedCube[16]
            cubeRot[26] = encodedCube[17]
            # Back Edges
            cubeRot[33] = encodedCube[24]
            cubeRot[34] = encodedCube[25]
            cubeRot[35] = encodedCube[26]
            # Left Edges
            cubeRot[6] = encodedCube[33]
            cubeRot[7] = encodedCube[34]
            cubeRot[8] = encodedCube[35]
            
        elif encodedDir == 'd':
            offset = 45
            faceRot = _faceCCW(cubeRot[45:54])
            
            for i, ch in enumerate(faceRot):
                cubeRot[i + offset] = ch
                
            # Front Edges
            cubeRot[33] = encodedCube[6]
            cubeRot[34] = encodedCube[7]
            cubeRot[35] = encodedCube[8]
            # Right Edges
            cubeRot[6] = encodedCube[15]
            cubeRot[7] = encodedCube[16]
            cubeRot[8] = encodedCube[17]
            # Back Edges
            cubeRot[15] = encodedCube[24]
            cubeRot[16] = encodedCube[25]
            cubeRot[17] = encodedCube[26]
            # Left Edges
            cubeRot[24] = encodedCube[33]
            cubeRot[25] = encodedCube[34]
            cubeRot[26] = encodedCube[35]
            
        # Performs F since that is the default for no dir
        else:
            offset = 0
            faceRot = _faceCW(cubeRot[0:9])
            
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
    newFace = face[:]
    
    newFace[2] = face[0]
    newFace[5] = face[1]
    newFace[8] = face[2]
    newFace[1] = face[3]
    # center stays at the same position
    newFace[7] = face[5]
    newFace[0] = face[6]
    newFace[3] = face[7]
    newFace[6] = face[8]
    
    return newFace

def _faceCCW(face):
    newFace = face[:]
    
    newFace[6] = face[0]
    newFace[3] = face[1]
    newFace[0] = face[2]
    newFace[7] = face[3]
    # center stays at the same position
    newFace[1] = face[5]
    newFace[8] = face[6]
    newFace[5] = face[7]
    newFace[2] = face[8]
    
    return newFace

def _validateDir(dir):
    validDirs = 'FfRrLlUuDdBb'
    
    if dir == None: 
        return True
    
    for d in dir:
        if validDirs.count(d) == 0:
            return False
    return True