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
        
        for rotation in encodedDir:
            
            cubeRotPrev = cubeRot[:]
            
            if rotation == 'f':
                offset = 0
                faceRot = _faceCCW(cubeRot[0:9])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Right Edges
                cubeRot[42] = cubeRotPrev[ 9]
                cubeRot[43] = cubeRotPrev[12]
                cubeRot[44] = cubeRotPrev[15]
                # Left Edges
                cubeRot[45] = cubeRotPrev[29]
                cubeRot[46] = cubeRotPrev[32]
                cubeRot[47] = cubeRotPrev[35]
                # Top Edges
                cubeRot[35] = cubeRotPrev[42]
                cubeRot[32] = cubeRotPrev[43]
                cubeRot[29] = cubeRotPrev[44]
                # Bottom Edges
                cubeRot[15] = cubeRotPrev[45]
                cubeRot[12] = cubeRotPrev[46]
                cubeRot[ 9] = cubeRotPrev[47]
            
            elif rotation == 'R':
                offset = 9
                faceRot = _faceCW(cubeRot[9:18])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[38] = cubeRotPrev[2]
                cubeRot[41] = cubeRotPrev[5]
                cubeRot[44] = cubeRotPrev[8]
                # Back Edges
                cubeRot[47] = cubeRotPrev[24]
                cubeRot[50] = cubeRotPrev[21]
                cubeRot[53] = cubeRotPrev[18]
                # Up Edges
                cubeRot[18] = cubeRotPrev[44]
                cubeRot[21] = cubeRotPrev[41]
                cubeRot[24] = cubeRotPrev[38]
                # Down Edges
                cubeRot[8] = cubeRotPrev[53]
                cubeRot[5] = cubeRotPrev[50]
                cubeRot[2] = cubeRotPrev[47]
                
            elif rotation == 'r':
                offset = 9
                faceRot = _faceCCW(cubeRot[9:18])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[47] = cubeRotPrev[2]
                cubeRot[50] = cubeRotPrev[5]
                cubeRot[53] = cubeRotPrev[8]
                # Back Edges
                cubeRot[38] = cubeRotPrev[24]
                cubeRot[41] = cubeRotPrev[21]
                cubeRot[44] = cubeRotPrev[18]
                # Up Edges
                cubeRot[8] = cubeRotPrev[44]
                cubeRot[5] = cubeRotPrev[41]
                cubeRot[2] = cubeRotPrev[38]
                # Down Edges
                cubeRot[18] = cubeRotPrev[53]
                cubeRot[21] = cubeRotPrev[50]
                cubeRot[24] = cubeRotPrev[47]
                
            elif rotation == 'B':
                offset = 18
                faceRot = _faceCW(cubeRot[18:27])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Right Edges
                cubeRot[36] = cubeRotPrev[11]
                cubeRot[37] = cubeRotPrev[14]
                cubeRot[38] = cubeRotPrev[17]
                # Left Edges
                cubeRot[51] = cubeRotPrev[27]
                cubeRot[52] = cubeRotPrev[30]
                cubeRot[53] = cubeRotPrev[33]
                # Up Edges
                cubeRot[33] = cubeRotPrev[36]
                cubeRot[30] = cubeRotPrev[37]
                cubeRot[27] = cubeRotPrev[38]
                # Down Edges
                cubeRot[17] = cubeRotPrev[51]
                cubeRot[14] = cubeRotPrev[52]
                cubeRot[11] = cubeRotPrev[53]
                
            elif rotation == 'b':
                offset = 18
                faceRot = _faceCCW(cubeRot[18:27])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Right Edges
                cubeRot[53] = cubeRotPrev[11]
                cubeRot[52] = cubeRotPrev[14]
                cubeRot[51] = cubeRotPrev[17]
                # Left Edges
                cubeRot[38] = cubeRotPrev[27]
                cubeRot[37] = cubeRotPrev[30]
                cubeRot[36] = cubeRotPrev[33]
                # Up Edges
                cubeRot[11] = cubeRotPrev[36]
                cubeRot[14] = cubeRotPrev[37]
                cubeRot[17] = cubeRotPrev[38]
                # Down Edges
                cubeRot[27] = cubeRotPrev[51]
                cubeRot[30] = cubeRotPrev[52]
                cubeRot[33] = cubeRotPrev[53]
                
            elif rotation == 'L':
                offset = 27
                faceRot = _faceCW(cubeRot[27:36])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[45] = cubeRotPrev[0]
                cubeRot[48] = cubeRotPrev[3]
                cubeRot[51] = cubeRotPrev[6]
                # Back Edges
                cubeRot[42] = cubeRotPrev[20]
                cubeRot[39] = cubeRotPrev[23]
                cubeRot[36] = cubeRotPrev[26]
                # Up Edges
                cubeRot[0] = cubeRotPrev[36]
                cubeRot[3] = cubeRotPrev[39]
                cubeRot[6] = cubeRotPrev[42]
                # Down Edges
                cubeRot[26] = cubeRotPrev[45]
                cubeRot[23] = cubeRotPrev[48]
                cubeRot[20] = cubeRotPrev[51]
                
            elif rotation == 'l':
                offset = 27
                faceRot = _faceCCW(cubeRot[27:36])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[36] = cubeRotPrev[0]
                cubeRot[39] = cubeRotPrev[3]
                cubeRot[42] = cubeRotPrev[6]
                # Back Edges
                cubeRot[51] = cubeRotPrev[20]
                cubeRot[48] = cubeRotPrev[23]
                cubeRot[45] = cubeRotPrev[26]
                # Up Edges
                cubeRot[26] = cubeRotPrev[36]
                cubeRot[23] = cubeRotPrev[39]
                cubeRot[20] = cubeRotPrev[42]
                # Down Edges
                cubeRot[0] = cubeRotPrev[45]
                cubeRot[3] = cubeRotPrev[48]
                cubeRot[6] = cubeRotPrev[51]
            
            elif rotation == 'U':
                offset = 36
                faceRot = _faceCW(cubeRot[36:45])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[27] = cubeRotPrev[0]
                cubeRot[28] = cubeRotPrev[1]
                cubeRot[29] = cubeRotPrev[2]
                # Right Edges
                cubeRot[0] = cubeRotPrev[9]
                cubeRot[1] = cubeRotPrev[10]
                cubeRot[2] = cubeRotPrev[11]
                # Back Edges
                cubeRot[9] = cubeRotPrev[18]
                cubeRot[10] = cubeRotPrev[19]
                cubeRot[11] = cubeRotPrev[20]
                # Left Edges
                cubeRot[18] = cubeRotPrev[27]
                cubeRot[19] = cubeRotPrev[28]
                cubeRot[20] = cubeRotPrev[29]
                
            elif rotation == 'u':
                offset = 36
                faceRot = _faceCCW(cubeRot[36:45])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[9] = cubeRotPrev[0]
                cubeRot[10] = cubeRotPrev[1]
                cubeRot[11] = cubeRotPrev[2]
                # Right Edges
                cubeRot[18] = cubeRotPrev[9]
                cubeRot[19] = cubeRotPrev[10]
                cubeRot[20] = cubeRotPrev[11]
                # Back Edges
                cubeRot[27] = cubeRotPrev[18]
                cubeRot[28] = cubeRotPrev[19]
                cubeRot[29] = cubeRotPrev[20]
                # Left Edges
                cubeRot[0] = cubeRotPrev[27]
                cubeRot[1] = cubeRotPrev[28]
                cubeRot[2] = cubeRotPrev[29]
                
            elif rotation == 'D':
                offset = 45
                faceRot = _faceCW(cubeRot[45:54])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[15] = cubeRotPrev[6]
                cubeRot[16] = cubeRotPrev[7]
                cubeRot[17] = cubeRotPrev[8]
                # Right Edges
                cubeRot[24] = cubeRotPrev[15]
                cubeRot[25] = cubeRotPrev[16]
                cubeRot[26] = cubeRotPrev[17]
                # Back Edges
                cubeRot[33] = cubeRotPrev[24]
                cubeRot[34] = cubeRotPrev[25]
                cubeRot[35] = cubeRotPrev[26]
                # Left Edges
                cubeRot[6] = cubeRotPrev[33]
                cubeRot[7] = cubeRotPrev[34]
                cubeRot[8] = cubeRotPrev[35]
                
            elif rotation == 'd':
                offset = 45
                faceRot = _faceCCW(cubeRot[45:54])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                    
                # Front Edges
                cubeRot[33] = cubeRotPrev[6]
                cubeRot[34] = cubeRotPrev[7]
                cubeRot[35] = cubeRotPrev[8]
                # Right Edges
                cubeRot[6] = cubeRotPrev[15]
                cubeRot[7] = cubeRotPrev[16]
                cubeRot[8] = cubeRotPrev[17]
                # Back Edges
                cubeRot[15] = cubeRotPrev[24]
                cubeRot[16] = cubeRotPrev[25]
                cubeRot[17] = cubeRotPrev[26]
                # Left Edges
                cubeRot[24] = cubeRotPrev[33]
                cubeRot[25] = cubeRotPrev[34]
                cubeRot[26] = cubeRotPrev[35]
                
            # Performs F since that is the default for no dir
            else:
                offset = 0
                faceRot = _faceCW(cubeRot[0:9])
                
                for i, ch in enumerate(faceRot):
                    cubeRot[i + offset] = ch
                
                # Right Edges
                cubeRot[47] = cubeRotPrev[ 9]
                cubeRot[46] = cubeRotPrev[12]
                cubeRot[45] = cubeRotPrev[15]
                # Left Edges
                cubeRot[44] = cubeRotPrev[29]
                cubeRot[43] = cubeRotPrev[32]
                cubeRot[42] = cubeRotPrev[35]
                # Top Edges
                cubeRot[ 9] = cubeRotPrev[42]
                cubeRot[12] = cubeRotPrev[43]
                cubeRot[15] = cubeRotPrev[44]
                # Bottom Edges
                cubeRot[29] = cubeRotPrev[45]
                cubeRot[32] = cubeRotPrev[46]
                cubeRot[35] = cubeRotPrev[47]
            
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