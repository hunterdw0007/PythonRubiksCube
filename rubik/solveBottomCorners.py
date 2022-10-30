import rubik.rotate as rotate
import math

def _solveBottomCorners(cube, rotations):
    # Returns the rotations needed to take a given cube and produce a cube with a solved bottom corners
    # Base Case: check if bottom corners are solved
    if _checkBottomCorners(cube):
        return cube, rotations
    
    # Case 1: piece is located in top, set the location
    location = _locateBottomCornerInTop(cube)
    
    # Case 2: piece is located in bottom, move to top
    if location == -1:
        cube, location, mvRots = _moveWrongBottomCornerToTop(cube)
        rotations += mvRots
    
    # Case 3: piece is already in the right spot
    if location == -1:
        location = _locateRotatedBottomCorner(cube)
    # Condition for Case 1 & 2 to move the piece to the right spot
    else:
        cube, location, posRots = _positionCornerInTop(cube, location)
    
        rotations = rotations + posRots
                   
        cube, location, moveRots = _moveCornerToBottomFromTop(cube, location)
        
        rotations = rotations + moveRots
    
    # Count is a failsafe for an infinite loop
    # and performing this algorithm more than 3 times would just loop back to the previous state again
    count = 0
    while not _checkBottomCornerOrientation(cube, location) and count < 3:
        cube, location, orientRots = _orientCornerInBottom(cube, location)
        rotations = rotations + orientRots
        count += 1
    
    return _solveBottomCorners(cube, rotations)  
   

def _checkBottomCorners(cube):
    # Checks whether or not the bottom corners are solved - independent of the bottom cross being solved
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D00.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D02.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D20.value]:
        return False
    if cube[rotate.cubeEnum.D11.value] != cube[rotate.cubeEnum.D22.value]:
        return False
    if cube[rotate.cubeEnum.F11.value] != cube[rotate.cubeEnum.F20.value]:
        return False
    if cube[rotate.cubeEnum.F11.value] != cube[rotate.cubeEnum.F22.value]:
        return False
    if cube[rotate.cubeEnum.R11.value] != cube[rotate.cubeEnum.R20.value]:
        return False
    if cube[rotate.cubeEnum.R11.value] != cube[rotate.cubeEnum.R22.value]:
        return False
    if cube[rotate.cubeEnum.B11.value] != cube[rotate.cubeEnum.B20.value]:
        return False
    if cube[rotate.cubeEnum.B11.value] != cube[rotate.cubeEnum.B22.value]:
        return False
    if cube[rotate.cubeEnum.L11.value] != cube[rotate.cubeEnum.L20.value]:
        return False
    if cube[rotate.cubeEnum.L11.value] != cube[rotate.cubeEnum.L22.value]:
        return False
    # If it makes it here then it's all correct
    return True

def _positionCornerInTop(cube, location):
    
    rotations = ''
    
    # Used to check for correctness/incorrectness of edge pairs
    topCornerColors = [ (cube[rotate.cubeEnum.F02.value], cube[rotate.cubeEnum.R00.value], cube[rotate.cubeEnum.U22.value])
                      , (cube[rotate.cubeEnum.R02.value], cube[rotate.cubeEnum.B00.value], cube[rotate.cubeEnum.U02.value])
                      , (cube[rotate.cubeEnum.B02.value], cube[rotate.cubeEnum.L00.value], cube[rotate.cubeEnum.U00.value])
                      , (cube[rotate.cubeEnum.L02.value], cube[rotate.cubeEnum.F00.value], cube[rotate.cubeEnum.U20.value]) ]
    
    bottomCornerColors = [ (cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.D11.value])
                         , (cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.D11.value])
                         , (cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.D11.value])
                         , (cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.D11.value]) ]
    
    while sorted(topCornerColors[int((location-2)/9)]) != sorted(bottomCornerColors[int((location-2)/9)]):
        rotations = rotations + 'U'
        cube = rotate._rotate({'cube':cube,'dir':'U'})['cube']
        # Reassign after each U rotation
        topCornerColors = [ (cube[rotate.cubeEnum.F02.value], cube[rotate.cubeEnum.R00.value], cube[rotate.cubeEnum.U22.value])
                          , (cube[rotate.cubeEnum.R02.value], cube[rotate.cubeEnum.B00.value], cube[rotate.cubeEnum.U02.value])
                          , (cube[rotate.cubeEnum.B02.value], cube[rotate.cubeEnum.L00.value], cube[rotate.cubeEnum.U00.value])
                          , (cube[rotate.cubeEnum.L02.value], cube[rotate.cubeEnum.F00.value], cube[rotate.cubeEnum.U20.value]) ]
        location = location - 9 if location != rotate.cubeEnum.F02.value else rotate.cubeEnum.L02.value
        
    return cube, location, rotations

def _moveCornerToBottomFromTop(cube, location):
# Moves a corner from the position above its correct position to its correct position
# Also does the reverse but the location value will be incorrect
    if location == rotate.cubeEnum.F02.value:
        rotations = 'RUru'
    elif location == rotate.cubeEnum.R02.value:
        rotations = 'BUbu'
    elif location == rotate.cubeEnum.B02.value:
        rotations = 'LUlu'
    elif location == rotate.cubeEnum.L02.value:
        rotations = 'FUfu'
        
    cube = rotate._rotate({'cube':cube,'dir':rotations})['cube'] 
    location += 6
    
    return cube, location, rotations
        
def _orientCornerInBottom(cube, location):
# Rotates a bottom corner once "clockwise" thus three applications of this algorithm will loop back to itself
    if location == rotate.cubeEnum.F22.value:
        rotations = 'RUruRUru'
    elif location == rotate.cubeEnum.R22.value:
        rotations = 'BUbuBUbu'
    elif location == rotate.cubeEnum.B22.value:
        rotations = 'LUluLUlu'
    elif location == rotate.cubeEnum.L22.value:
        rotations = 'FUfuFUfu'
    
    cube = rotate._rotate({'cube':cube,'dir':rotations})['cube']
        
    return cube, location, rotations

def _checkBottomCornerOrientation(cube, location):
# Checks a given bottom corner location to see if it is oriented such that the face pointing down is the same color as the
# Down side of the cube
# Returns True if it is facing down, and False otherwise
    if location == rotate.cubeEnum.F22.value and cube[rotate.cubeEnum.D02.value] == cube[rotate.cubeEnum.D11.value]:
            return True
    if location == rotate.cubeEnum.R22.value and cube[rotate.cubeEnum.D22.value] == cube[rotate.cubeEnum.D11.value]:
            return True
    if location == rotate.cubeEnum.B22.value and cube[rotate.cubeEnum.D20.value] == cube[rotate.cubeEnum.D11.value]:
            return True
    if location == rotate.cubeEnum.L22.value and cube[rotate.cubeEnum.D00.value] == cube[rotate.cubeEnum.D11.value]:
            return True
    return False

def _locateBottomCornerInTop(cube):
# Checks each of the four top corners to see if they contain a face with the same color as the Down side of the cube
# Returns the first one found or -1 if none are found
    topCornerColors = [ (cube[rotate.cubeEnum.F02.value], cube[rotate.cubeEnum.R00.value], cube[rotate.cubeEnum.U22.value])
                      , (cube[rotate.cubeEnum.R02.value], cube[rotate.cubeEnum.B00.value], cube[rotate.cubeEnum.U02.value])
                      , (cube[rotate.cubeEnum.B02.value], cube[rotate.cubeEnum.L00.value], cube[rotate.cubeEnum.U00.value])
                      , (cube[rotate.cubeEnum.L02.value], cube[rotate.cubeEnum.F00.value], cube[rotate.cubeEnum.U20.value]) ]
    
    # Set to -1 in case none are found
    location = -1
    
    for i, corner in enumerate(topCornerColors):
        if corner.count(cube[rotate.cubeEnum.D11.value]) > 0:
            location = i * 9 + 2
            break
            
    return location

def _locateRotatedBottomCorner(cube):
# Checks each of the four bottom corners to see if they are in the right spot but rotated the wrong way
# Returns the location of a corner if found or -1 if none are found
    expectedBottomCorners = [ (cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.D11.value])
                            , (cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.D11.value])
                            , (cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.D11.value])
                            , (cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.D11.value]) ]

    actualBottomCorners = [ (cube[rotate.cubeEnum.F22.value], cube[rotate.cubeEnum.R20.value], cube[rotate.cubeEnum.D02.value])
                          , (cube[rotate.cubeEnum.R22.value], cube[rotate.cubeEnum.B20.value], cube[rotate.cubeEnum.D22.value])
                          , (cube[rotate.cubeEnum.B22.value], cube[rotate.cubeEnum.L20.value], cube[rotate.cubeEnum.D20.value])
                          , (cube[rotate.cubeEnum.L22.value], cube[rotate.cubeEnum.F20.value], cube[rotate.cubeEnum.D00.value]) ]
    
    location = -1
    
    for i, corner in enumerate(actualBottomCorners):
        # We only care if the corner contains the right colors and is rotated incorrectly
        if sorted(corner) == sorted(expectedBottomCorners[i]) and corner[2] != expectedBottomCorners[i][2]:
            location = i * 9 + 8
            break
                
    return location
        
def _moveWrongBottomCornerToTop(cube):
# Finds the first corner that is located in the bottom which is in the wrong spot and moves it to the top to be operated on later
    expectedBottomCorners = [ (cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.D11.value])
                            , (cube[rotate.cubeEnum.R11.value], cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.D11.value])
                            , (cube[rotate.cubeEnum.B11.value], cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.D11.value])
                            , (cube[rotate.cubeEnum.L11.value], cube[rotate.cubeEnum.F11.value], cube[rotate.cubeEnum.D11.value]) ]

    actualBottomCorners = [ (cube[rotate.cubeEnum.F22.value], cube[rotate.cubeEnum.R20.value], cube[rotate.cubeEnum.D02.value])
                          , (cube[rotate.cubeEnum.R22.value], cube[rotate.cubeEnum.B20.value], cube[rotate.cubeEnum.D22.value])
                          , (cube[rotate.cubeEnum.B22.value], cube[rotate.cubeEnum.L20.value], cube[rotate.cubeEnum.D20.value])
                          , (cube[rotate.cubeEnum.L22.value], cube[rotate.cubeEnum.F20.value], cube[rotate.cubeEnum.D00.value]) ]
    
    location = -1
    rotations = ''
    
    for i, corner in enumerate(actualBottomCorners):
        if sorted(corner) != sorted(expectedBottomCorners[i]) and corner.count(cube[rotate.cubeEnum.D11.value]):
            cube, _, rotations = _moveCornerToBottomFromTop(cube, i * 9 + 2)
            location = i * 9 + 2
            break
    
    return cube, location, rotations