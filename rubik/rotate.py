import rubik.cube as rubik
import re
from enum import Enum

class Cube(Enum):
    F00 = 0
    F01 = 1
    F02 = 2
    F10 = 3
    F11 = 4
    F12 = 5
    F20 = 6
    F21 = 7
    F22 = 8
    R00 = 9
    R01 = 10
    R02 = 11
    R10 = 12
    R11 = 13
    R12 = 14
    R20 = 15
    R21 = 16
    R22 = 17
    B00 = 18
    B01 = 19
    B02 = 20
    B10 = 21
    B11 = 22
    B12 = 23
    B20 = 24
    B21 = 25
    B22 = 26
    L00 = 27
    L01 = 28
    L02 = 29
    L10 = 30
    L11 = 31
    L12 = 32
    L20 = 33
    L21 = 34
    L22 = 35
    U00 = 36
    U01 = 37
    U02 = 38
    U10 = 39
    U11 = 40
    U12 = 41
    U20 = 42
    U21 = 43
    U22 = 44
    D00 = 45
    D01 = 46
    D02 = 47
    D10 = 48
    D11 = 49
    D12 = 50
    D20 = 51
    D21 = 52
    D22 = 53

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
        
        if encodedDir == None or encodedDir == '':
            encodedDir = 'F'
        
        for rotation in encodedDir:
            
            cubeRotPrev = cubeRot[:]
            
            if rotation == 'f':
                cubeRot = _rotatef(cubeRot, cubeRotPrev)
            elif rotation == 'R':
                cubeRot = _rotateR(cubeRot, cubeRotPrev)               
            elif rotation == 'r':
                cubeRot = _rotater(cubeRot, cubeRotPrev)               
            elif rotation == 'B':
                cubeRot = _rotateB(cubeRot, cubeRotPrev)    
            elif rotation == 'b':
                cubeRot = _rotateb(cubeRot, cubeRotPrev)
            elif rotation == 'L':
                cubeRot = _rotateL(cubeRot, cubeRotPrev)
            elif rotation == 'l':
                cubeRot = _rotatel(cubeRot, cubeRotPrev)
            elif rotation == 'U':
                cubeRot = _rotateU(cubeRot, cubeRotPrev)
            elif rotation == 'u':
                cubeRot = _rotateu(cubeRot, cubeRotPrev)
            elif rotation == 'D':
                cubeRot = _rotateD(cubeRot, cubeRotPrev)
            elif rotation == 'd':
                cubeRot = _rotated(cubeRot, cubeRotPrev)
            # Performs F since that is the default for no dir
            else:
                cubeRot = _rotateF(cubeRot, cubeRotPrev)
            
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

def _validateDir(direction):
    validDirs = 'FfRrLlUuDdBb'
    
    if direction == None: 
        return True
    
    for d in direction:
        if validDirs.count(d) == 0:
            return False
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

def _rotateF(cubeRot, cubeRotPrev):
    offset = Cube.F00.value
    faceRot = _faceCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
    
    # Right Edges
    cubeRot[Cube.D02.value] = cubeRotPrev[Cube.R00.value]
    cubeRot[Cube.D01.value] = cubeRotPrev[Cube.R10.value]
    cubeRot[Cube.D00.value] = cubeRotPrev[Cube.R20.value]
    # Left Edges
    cubeRot[Cube.U22.value] = cubeRotPrev[Cube.L02.value]
    cubeRot[Cube.U21.value] = cubeRotPrev[Cube.L12.value]
    cubeRot[Cube.U20.value] = cubeRotPrev[Cube.L22.value]
    # Top Edges
    cubeRot[Cube.R00.value] = cubeRotPrev[Cube.U20.value]
    cubeRot[Cube.R10.value] = cubeRotPrev[Cube.U21.value]
    cubeRot[Cube.R20.value] = cubeRotPrev[Cube.U22.value]
    # Bottom Edges
    cubeRot[Cube.L02.value] = cubeRotPrev[Cube.D00.value]
    cubeRot[Cube.L12.value] = cubeRotPrev[Cube.D01.value]
    cubeRot[Cube.L22.value] = cubeRotPrev[Cube.D02.value]
    
    return cubeRot

def _rotatef(cubeRot, cubeRotPrev):
    offset = Cube.F00.value
    faceRot = _faceCCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Right Edges
    cubeRot[Cube.U20.value] = cubeRotPrev[Cube.R00.value]
    cubeRot[Cube.U21.value] = cubeRotPrev[Cube.R10.value]
    cubeRot[Cube.U22.value] = cubeRotPrev[Cube.R20.value]
    # Left Edges
    cubeRot[Cube.D00.value] = cubeRotPrev[Cube.L02.value]
    cubeRot[Cube.D01.value] = cubeRotPrev[Cube.L12.value]
    cubeRot[Cube.D02.value] = cubeRotPrev[Cube.L22.value]
    # Top Edges
    cubeRot[Cube.L22.value] = cubeRotPrev[Cube.U20.value]
    cubeRot[Cube.L12.value] = cubeRotPrev[Cube.U21.value]
    cubeRot[Cube.L02.value] = cubeRotPrev[Cube.U22.value]
    # Bottom Edges
    cubeRot[Cube.R20.value] = cubeRotPrev[Cube.D00.value]
    cubeRot[Cube.R10.value] = cubeRotPrev[Cube.D01.value]
    cubeRot[Cube.R00.value] = cubeRotPrev[Cube.D02.value]
    
    return cubeRot

def _rotateR(cubeRot, cubeRotPrev):
    offset = Cube.R00.value
    faceRot = _faceCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.U02.value] = cubeRotPrev[Cube.F02.value]
    cubeRot[Cube.U12.value] = cubeRotPrev[Cube.F12.value]
    cubeRot[Cube.U22.value] = cubeRotPrev[Cube.F22.value]
    # Back Edges
    cubeRot[Cube.D02.value] = cubeRotPrev[Cube.B20.value]
    cubeRot[Cube.D12.value] = cubeRotPrev[Cube.B10.value]
    cubeRot[Cube.D22.value] = cubeRotPrev[Cube.B00.value]
    # Up Edges
    cubeRot[Cube.B00.value] = cubeRotPrev[Cube.U22.value]
    cubeRot[Cube.B10.value] = cubeRotPrev[Cube.U12.value]
    cubeRot[Cube.B20.value] = cubeRotPrev[Cube.U02.value]
    # Down Edges
    cubeRot[Cube.F22.value] = cubeRotPrev[Cube.D22.value]
    cubeRot[Cube.F12.value] = cubeRotPrev[Cube.D12.value]
    cubeRot[Cube.F02.value] = cubeRotPrev[Cube.D02.value]
    
    return cubeRot

def _rotater(cubeRot, cubeRotPrev):
    offset = Cube.R00.value
    faceRot = _faceCCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.D02.value] = cubeRotPrev[Cube.F02.value]
    cubeRot[Cube.D12.value] = cubeRotPrev[Cube.F12.value]
    cubeRot[Cube.D22.value] = cubeRotPrev[Cube.F22.value]
    # Back Edges
    cubeRot[Cube.U02.value] = cubeRotPrev[Cube.B20.value]
    cubeRot[Cube.U12.value] = cubeRotPrev[Cube.B10.value]
    cubeRot[Cube.U22.value] = cubeRotPrev[Cube.B00.value]
    # Up Edges
    cubeRot[Cube.F22.value] = cubeRotPrev[Cube.U22.value]
    cubeRot[Cube.F12.value] = cubeRotPrev[Cube.U12.value]
    cubeRot[Cube.F02.value] = cubeRotPrev[Cube.U02.value]
    # Down Edges
    cubeRot[Cube.B00.value] = cubeRotPrev[Cube.D22.value]
    cubeRot[Cube.B10.value] = cubeRotPrev[Cube.D12.value]
    cubeRot[Cube.B20.value] = cubeRotPrev[Cube.D02.value]
    
    return cubeRot

def _rotateB(cubeRot, cubeRotPrev):
    offset = Cube.B00.value
    faceRot = _faceCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Right Edges
    cubeRot[Cube.U00.value] = cubeRotPrev[Cube.R02.value]
    cubeRot[Cube.U01.value] = cubeRotPrev[Cube.R12.value]
    cubeRot[Cube.U02.value] = cubeRotPrev[Cube.R22.value]
    # Left Edges
    cubeRot[Cube.D20.value] = cubeRotPrev[Cube.L00.value]
    cubeRot[Cube.D21.value] = cubeRotPrev[Cube.L10.value]
    cubeRot[Cube.D22.value] = cubeRotPrev[Cube.L20.value]
    # Up Edges
    cubeRot[Cube.L20.value] = cubeRotPrev[Cube.U00.value]
    cubeRot[Cube.L10.value] = cubeRotPrev[Cube.U01.value]
    cubeRot[Cube.L00.value] = cubeRotPrev[Cube.U02.value]
    # Down Edges
    cubeRot[Cube.R22.value] = cubeRotPrev[Cube.D20.value]
    cubeRot[Cube.R12.value] = cubeRotPrev[Cube.D21.value]
    cubeRot[Cube.R02.value] = cubeRotPrev[Cube.D22.value]
    
    return cubeRot

def _rotateb(cubeRot, cubeRotPrev):
    offset = Cube.B00.value
    faceRot = _faceCCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Right Edges
    cubeRot[Cube.D22.value] = cubeRotPrev[Cube.R02.value]
    cubeRot[Cube.D21.value] = cubeRotPrev[Cube.R12.value]
    cubeRot[Cube.D20.value] = cubeRotPrev[Cube.R22.value]
    # Left Edges
    cubeRot[Cube.U02.value] = cubeRotPrev[Cube.L00.value]
    cubeRot[Cube.U01.value] = cubeRotPrev[Cube.L10.value]
    cubeRot[Cube.U00.value] = cubeRotPrev[Cube.L20.value]
    # Up Edges
    cubeRot[Cube.R02.value] = cubeRotPrev[Cube.U00.value]
    cubeRot[Cube.R12.value] = cubeRotPrev[Cube.U01.value]
    cubeRot[Cube.R22.value] = cubeRotPrev[Cube.U02.value]
    # Down Edges
    cubeRot[Cube.L00.value] = cubeRotPrev[Cube.D20.value]
    cubeRot[Cube.L10.value] = cubeRotPrev[Cube.D21.value]
    cubeRot[Cube.L20.value] = cubeRotPrev[Cube.D22.value]
    
    return cubeRot

def _rotateL(cubeRot, cubeRotPrev):
    offset = Cube.L00.value
    faceRot = _faceCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.D00.value] = cubeRotPrev[Cube.F00.value]
    cubeRot[Cube.D10.value] = cubeRotPrev[Cube.F10.value]
    cubeRot[Cube.D20.value] = cubeRotPrev[Cube.F20.value]
    # Back Edges
    cubeRot[Cube.U20.value] = cubeRotPrev[Cube.B02.value]
    cubeRot[Cube.U10.value] = cubeRotPrev[Cube.B12.value]
    cubeRot[Cube.U00.value] = cubeRotPrev[Cube.B22.value]
    # Up Edges
    cubeRot[Cube.F00.value] = cubeRotPrev[Cube.U00.value]
    cubeRot[Cube.F10.value] = cubeRotPrev[Cube.U10.value]
    cubeRot[Cube.F20.value] = cubeRotPrev[Cube.U20.value]
    # Down Edges
    cubeRot[Cube.B22.value] = cubeRotPrev[Cube.D00.value]
    cubeRot[Cube.B12.value] = cubeRotPrev[Cube.D10.value]
    cubeRot[Cube.B02.value] = cubeRotPrev[Cube.D20.value]
    
    return cubeRot

def _rotatel(cubeRot, cubeRotPrev):
    offset = Cube.L00.value
    faceRot = _faceCCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.U00.value] = cubeRotPrev[Cube.F00.value]
    cubeRot[Cube.U10.value] = cubeRotPrev[Cube.F10.value]
    cubeRot[Cube.U20.value] = cubeRotPrev[Cube.F20.value]
    # Back Edges
    cubeRot[Cube.D20.value] = cubeRotPrev[Cube.B02.value]
    cubeRot[Cube.D10.value] = cubeRotPrev[Cube.B12.value]
    cubeRot[Cube.D00.value] = cubeRotPrev[Cube.B22.value]
    # Up Edges
    cubeRot[Cube.B22.value] = cubeRotPrev[Cube.U00.value]
    cubeRot[Cube.B12.value] = cubeRotPrev[Cube.U10.value]
    cubeRot[Cube.B02.value] = cubeRotPrev[Cube.U20.value]
    # Down Edges
    cubeRot[Cube.F00.value] = cubeRotPrev[Cube.D00.value]
    cubeRot[Cube.F10.value] = cubeRotPrev[Cube.D10.value]
    cubeRot[Cube.F20.value] = cubeRotPrev[Cube.D20.value]  
      
    return cubeRot

def _rotateU(cubeRot, cubeRotPrev):
    offset = Cube.U00.value
    faceRot = _faceCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.L00.value] = cubeRotPrev[Cube.F00.value]
    cubeRot[Cube.L01.value] = cubeRotPrev[Cube.F01.value]
    cubeRot[Cube.L02.value] = cubeRotPrev[Cube.F02.value]
    # Right Edges
    cubeRot[Cube.F00.value] = cubeRotPrev[Cube.R00.value]
    cubeRot[Cube.F01.value] = cubeRotPrev[Cube.R01.value]
    cubeRot[Cube.F02.value] = cubeRotPrev[Cube.R02.value]
    # Back Edges
    cubeRot[Cube.R00.value] = cubeRotPrev[Cube.B00.value]
    cubeRot[Cube.R01.value] = cubeRotPrev[Cube.B01.value]
    cubeRot[Cube.R02.value] = cubeRotPrev[Cube.B02.value]
    # Left Edges
    cubeRot[Cube.B00.value] = cubeRotPrev[Cube.L00.value]
    cubeRot[Cube.B01.value] = cubeRotPrev[Cube.L01.value]
    cubeRot[Cube.B02.value] = cubeRotPrev[Cube.L02.value]
    
    return cubeRot

def _rotateu(cubeRot, cubeRotPrev):
    offset = Cube.U00.value
    faceRot = _faceCCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.R00.value] = cubeRotPrev[Cube.F00.value]
    cubeRot[Cube.R01.value] = cubeRotPrev[Cube.F01.value]
    cubeRot[Cube.R02.value] = cubeRotPrev[Cube.F02.value]
    # Right Edges
    cubeRot[Cube.B00.value] = cubeRotPrev[Cube.R00.value]
    cubeRot[Cube.B01.value] = cubeRotPrev[Cube.R01.value]
    cubeRot[Cube.B02.value] = cubeRotPrev[Cube.R02.value]
    # Back Edges
    cubeRot[Cube.L00.value] = cubeRotPrev[Cube.B00.value]
    cubeRot[Cube.L01.value] = cubeRotPrev[Cube.B01.value]
    cubeRot[Cube.L02.value] = cubeRotPrev[Cube.B02.value]
    # Left Edges
    cubeRot[Cube.F00.value] = cubeRotPrev[Cube.L00.value]
    cubeRot[Cube.F01.value] = cubeRotPrev[Cube.L01.value]
    cubeRot[Cube.F02.value] = cubeRotPrev[Cube.L02.value]    
    
    return cubeRot

def _rotateD(cubeRot, cubeRotPrev):
    offset = Cube.D00.value
    faceRot = _faceCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.R20.value] = cubeRotPrev[Cube.F20.value]
    cubeRot[Cube.R21.value] = cubeRotPrev[Cube.F21.value]
    cubeRot[Cube.R22.value] = cubeRotPrev[Cube.F22.value]
    # Right Edges
    cubeRot[Cube.B20.value] = cubeRotPrev[Cube.R20.value]
    cubeRot[Cube.B21.value] = cubeRotPrev[Cube.R21.value]
    cubeRot[Cube.B22.value] = cubeRotPrev[Cube.R22.value]
    # Back Edges
    cubeRot[Cube.L20.value] = cubeRotPrev[Cube.B20.value]
    cubeRot[Cube.L21.value] = cubeRotPrev[Cube.B21.value]
    cubeRot[Cube.L22.value] = cubeRotPrev[Cube.B22.value]
    # Left Edges
    cubeRot[Cube.F20.value] = cubeRotPrev[Cube.L20.value]
    cubeRot[Cube.F21.value] = cubeRotPrev[Cube.L21.value]
    cubeRot[Cube.F22.value] = cubeRotPrev[Cube.L22.value]
    
    return cubeRot

def _rotated(cubeRot, cubeRotPrev):
    offset = Cube.D00.value
    faceRot = _faceCCW(cubeRot[offset + 0:offset + 9])
    
    for i, ch in enumerate(faceRot):
        cubeRot[i + offset] = ch
        
    # Front Edges
    cubeRot[Cube.L20.value] = cubeRotPrev[Cube.F20.value]
    cubeRot[Cube.L21.value] = cubeRotPrev[Cube.F21.value]
    cubeRot[Cube.L22.value] = cubeRotPrev[Cube.F22.value]
    # Right Edges
    cubeRot[Cube.F20.value] = cubeRotPrev[Cube.R20.value]
    cubeRot[Cube.F21.value] = cubeRotPrev[Cube.R21.value]
    cubeRot[Cube.F22.value] = cubeRotPrev[Cube.R22.value]
    # Back Edges
    cubeRot[Cube.R20.value] = cubeRotPrev[Cube.B20.value]
    cubeRot[Cube.R21.value] = cubeRotPrev[Cube.B21.value]
    cubeRot[Cube.R22.value] = cubeRotPrev[Cube.B22.value]
    # Left Edges
    cubeRot[Cube.B20.value] = cubeRotPrev[Cube.L20.value]
    cubeRot[Cube.B21.value] = cubeRotPrev[Cube.L21.value]
    cubeRot[Cube.B22.value] = cubeRotPrev[Cube.L22.value]
    
    return cubeRot