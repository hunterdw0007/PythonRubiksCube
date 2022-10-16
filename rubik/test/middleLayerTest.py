'''
Created on Oct 13, 2022

@author: Hunter
'''
import unittest
import rubik.solve as solve
import rubik.rotate as rotate
import rubik.verify as verify
import rubik.solveMiddleLayer as solveMiddleLayer

class Test(unittest.TestCase):

# Analysis - solveMiddleLayer._checkMiddleLayer
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: boolean
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: fully solved cube
#    test 020: solved bottom not middle
#    test 030: solved middle, scrambled elsewhere

    def test_checkMiddleLayer_010_solvedMiddleEdgesOfSolvedCubeCheck(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = True
        
        actualResult = solveMiddleLayer._checkMiddleLayer(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_checkMiddleLayer_020_solvedMiddleEdgesOfSolvedBottomCheck(self):
        cube = 'byybwbwwwbyrrrorrrboobyryyywoowowooobwwybrybrggggggggg'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = False
        
        actualResult = solveMiddleLayer._checkMiddleLayer(cube)
        
        self.assertEqual(expectResult, actualResult)

    def test_checkMiddleLayer_030_solvedMiddleEdgesOnly(self):
        cube = 'rgbbbbyybyborrrywrwgogggwrgywgoooowrgwbbyywyogorowrwyb'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = True
        
        actualResult = solveMiddleLayer._checkMiddleLayer(cube)
        
        self.assertEqual(expectResult, actualResult)

# Analysis - solveMiddleLayer._locateMiddlePieceInTop
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: integer, [0-53] corresponding to location
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: edge found in Front
#    test 020: edge found elsewhere
# 
# sad path:
#    test 910: no edge found

    def test_locateMiddlePieceInTop_010_edgeFoundInFront(self):
        cube = 'gogobbbbbogyyrrrrrbybygbgggyrrooyoooogrbyrygywwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = rotate.cubeEnum.F01.value
        
        actualResult = solveMiddleLayer._locateMiddlePieceInTop(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_locateMiddlePieceInTop_020_edgeFoundNotInFront(self):
        cube = 'bybobbbbbyrryrrrrrgogygbgggogyooyoooygyrybrgowwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = rotate.cubeEnum.R01.value
        
        actualResult = solveMiddleLayer._locateMiddlePieceInTop(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_locateMiddlePieceInTop_910_edgeNotFoundInTop(self):
        # Solved cube has no middle edges in top
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = -1
        
        actualResult = solveMiddleLayer._locateMiddlePieceInTop(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveMiddleLayer._positionMiddlePieceInTop
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#    location: integer, [0-53], arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns:
#        cube: string; len=54, [browyg], 9 occurences of each character, unique middle color
#        location: integer, 0-53 corresponding to location
#        rotations: string, len=0-3, [U]
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: edge located in front
#    test 020: edge not located in front
#    test 030: all edges solved except one, needs 3 rotations to place
        
    def test_positionMiddlePieceInTop_010_edgeLocatedInFront(self):
        cube = 'gogobbbbbogyyrrrrrbybygbgggyrrooyoooogrbyrygywwwwwwwww'
        location = rotate.cubeEnum.F01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'ogyobbbbbbybyrrrrryrrygbggggogooyoooybogygyrrwwwwwwwww'
        expectedLocation = rotate.cubeEnum.L01.value
        expectedRotations = 'U'
        
        actualCube, actualLocation, actualRotations = solveMiddleLayer._positionMiddlePieceInTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)

    def test_positionMiddlePieceInTop_020_edgeNotLocatedInFront(self):
        cube = 'bybobbbbbyrryrrrrrgogygbgggogyooyoooygyrybrgowwwwwwwww'
        location = rotate.cubeEnum.R01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = cube
        expectedLocation = rotate.cubeEnum.R01.value
        expectedRotations = ''
        
        actualCube, actualLocation, actualRotations = solveMiddleLayer._positionMiddlePieceInTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_positionMiddlePieceInTop_030_edgeNeedsThreeRotations(self):
        cube = 'yogggggggygbooyooorbbobbbbbyyorrrrrroyyryygbrwwwwwwwww'
        location = rotate.cubeEnum.F01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'yyoggggggyogooyoooygbobbbbbrbbrrrrrryyryyborgwwwwwwwww'
        expectedLocation = rotate.cubeEnum.R01.value
        expectedRotations = 'UUU'
        
        actualCube, actualLocation, actualRotations = solveMiddleLayer._positionMiddlePieceInTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)

# Analysis - solveMiddleLayer._locateMiddlePieceInMiddle
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: integer, 0-53 corresponding to location
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: edge found in Front
#    test 020: edge found elsewhere

    def test_locateMiddlePieceInMiddle_010_edgeFoundInFront(self):
        cube = 'rgbggbgggrboooyoooygoobbbbbbryrrrrrryygyyygoywwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = rotate.cubeEnum.F12.value
        
        actualResult = solveMiddleLayer._locateMiddlePieceInMiddle(cube)
        
        self.assertEqual(expectResult, actualResult)

    def test_locateMiddlePieceInMiddle_020_edgeNotFoundInFront(self):
        cube = 'gygggggggooooobooobbbobbbbbrrrrrrrrryyyyyyygywwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = rotate.cubeEnum.R12.value
        
        actualResult = solveMiddleLayer._locateMiddlePieceInMiddle(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveMiddleLayer._moveMiddlePieceToTop
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#    location: integer, [0-53], arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns:
#        cube: string; len=54, [browyg], 9 occurences of each character, unique middle color
#        location: integer, 0-53 corresponding to location
#        rotations: string, len=8
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: edge located in front
#    test 020: edge not located in front

    def test_moveMiddlePieceToTop_010_edgeLocatedInFront(self):
        cube = 'rygrrgrrrogbrgggggrbbooooooyrybbbbbboyyyyygoywwwwwwwww'
        location = rotate.cubeEnum.F12.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'yrgrryrrrobbogggggyrgooooooyyrbbbbbbrgogyybyywwwwwwwww'
        expectedLocation = rotate.cubeEnum.B01.value
        expectedRotations = 'URurufUF'
        
        actualCube, actualLocation, actualRotations = solveMiddleLayer._moveMiddlePieceToTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_moveMiddlePieceToTop_020_edgeNotLocatedInFront(self):
        cube = 'bybrrrrrrrygggbgggooryooooogyobbbbbbygyryoygywwwwwwwww'
        location = rotate.cubeEnum.R12.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'bggrrrrrryygggygggoyooooooobyybbbbbbyrybygrorwwwwwwwww'
        expectedLocation = rotate.cubeEnum.L01.value
        expectedRotations = 'UBuburUR'
        
        actualCube, actualLocation, actualRotations = solveMiddleLayer._moveMiddlePieceToTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)
        
# Analysis - solveMiddleLayer._middleAlgorithmRight
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#    location: integer, [0-53], arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns:
#        cube: string; len=54, [browyg], 9 occurences of each character, unique middle color
#        rotations: string, len=8
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: edge located in front
#    test 020: edge not located in front

    def test_middleAlgorithmRight_010_edgeLocatedInFront(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        location = rotate.cubeEnum.F01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'yobbbbbbbrggyrrrrroryggggggoygoooooobbyryyryywwwwwwwww'
        expectedRotations = 'URurufUF'
        
        actualCube, actualRotations = solveMiddleLayer._middleAlgorithmRight(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_middleAlgorithmRight_020_edgeNotLocatedInFront(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        location = rotate.cubeEnum.R01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'byobbbbbbybrrrrrrrgooygggggbgyooooooyyyryyrggwwwwwwwww'
        expectedRotations = 'UBuburUR'
        
        actualCube, actualRotations = solveMiddleLayer._middleAlgorithmRight(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
# Analysis - solveMiddleLayer._middleAlgorithmLeft
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#    location: integer, [0-53], arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns:
#        cube: string; len=54, [browyg], 9 occurences of each character, unique middle color
#        rotations: string, len=8
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: edge located in front
#    test 020: edge not located in front

    def test_middleAlgorithmLeft_010_edgeLocatedInFront(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        location = rotate.cubeEnum.F01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'brybbbbbbgyrrrrrrryorggggggggoooyoooybbyyoyyowwwwwwwww'
        expectedRotations = 'ulULUFuf'
        
        actualCube, actualRotations = solveMiddleLayer._middleAlgorithmLeft(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_middleAlgorithmLeft_020_edgeNotLocatedInFront(self):
        cube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        location = rotate.cubeEnum.L01.value
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'gyrrrrrrryorggggggggoooyooobrybbbbbbyyyyyboobwwwwwwwww'
        expectedRotations = 'ubUBULul'
        
        actualCube, actualRotations = solveMiddleLayer._middleAlgorithmLeft(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
# Analysis - solve._solve
#
# inputs:
#    parms: dict: mandatory: arrives validated
#    parms['op']: string; 'solve', mandatory, arrives validated
#    parms['cube']: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives unvalidated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: dict
#    nominal:
#        dict['rotations']: string, rotations to solve cube bottom
#        dict['status']: string, 'ok'
#    abnormal:
#        dict['status']: string, 'error: xxx', xxx is message
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: solved cube input
#    test 020: solved bottom layer and middle layer input
#    test 030: solved bottom layer, not middle layer
#    test 040: solved bottom layer, no middle pieces solved

    def test_solveMiddleLayer_010_solvedCubeInput(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = {}
        expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_solveMiddleLayer_020_solvedBottomAndMiddle(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'roobbbbbbyrrrrrrrrygyggggggobyoooooobybyyygygwwwwwwwww'
        
        expectResult = {}
        expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_solveMiddleLayer_030_solvedBottomNotMiddle(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww'
        
        expectResult = {}
        expectResult['rotations'] = 'ulULUFuf'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))