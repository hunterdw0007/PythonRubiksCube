'''
Created on Oct 24, 2022

@author: Hunter
'''
import unittest
import hashlib
import rubik.verify as verify
import rubik.solveTopFace as solveTopFace
import rubik.solve as solve

class TopFaceTest(unittest.TestCase):

# Analysis - solveTopFace._checkTopCross
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
#    test 020: scrambled cube
#    test 030: scrambled cube except cross

    def test_checkTopCross_010_solvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopFace._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopCross_020_scrambledCube(self):
        cube = 'rgbbbbyybyborrrywrwgogggwrgywgoooowrgwbbyywyogorowrwyb'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopFace._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopCross_030_scrambledCubeExceptCross(self):
        cube = 'ybygbywbwoogooygyyrgorgbobywrgorrrgrbwwwwwrwbbyooygbrg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopFace._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveTopFace._checkCrossState
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: int; [0-3]
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: top cross completed
#    test 020: line on top - horizontal
#    test 021: line on top - vertical
#    test 030: L on top
#    test 040: dot on top

    def test_checkCrossState_010_topCrossSolved(self):
        cube = 'grbbbbbbbrbyrrrrrrgobggggggygroooooooyoyyyyyywwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = -1
        
        actualResult = solveTopFace._checkCrossState(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkCrossState_020_topLineHorizontal(self):
        cube = 'yyrbbbbbbyoorrrrrryyoggggggbggooooooyrgyyyrbbwwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = 0
        
        actualResult = solveTopFace._checkCrossState(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_checkCrossState_021_topLineVertical(self):
        cube = 'yoobbbbbbyyorrrrrrbggggggggyyrooooooryybyrbygwwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = 1
        
        actualResult = solveTopFace._checkCrossState(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkCrossState_030_topL(self):
        cube = 'brybbbbbbggyrrrrrroyrgggggggyyooooooyobbyyryowwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = 2
        
        actualResult = solveTopFace._checkCrossState(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkCrossState_040_topDot(self):
        cube = 'rygbbbbbboybrrrrrryyyggggggryboooooogrobyoygywwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = 0
        
        actualResult = solveTopFace._checkCrossState(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveTopFace._orientTopEdges
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns:
#        cube: string; len=54, [browyg], 9 occurences of each character, unique middle color
#        rotations: string, len=0-3, [U]
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: cross solved
#    test 020: horizontal line
#    test 030: L shape
#    test 040: dot on top

    def test_orientTopEdges_010_CrossOrientedCorrectly(self):
        cube = 'rbybbbbbboryrrrrrrgobggggggrgyooooooyyoyyygybwwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'rbybbbbbboryrrrrrrgobggggggrgyooooooyyoyyygybwwwwwwwww'
        expectedRotations = ''
        
        actualCube, actualRotations = solveTopFace._orientTopEdges(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_orientTopEdges_020_HorizontalLine(self):
        cube = 'gyobbbbbbboorrrrrryyyggggggbgroooooorbgyyyyrywwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'bbgbbbbbbyrrrrrrrryooggggggygooooooogybyyyyyrwwwwwwwww'
        expectedRotations = 'FRUruf'
        
        actualCube, actualRotations = solveTopFace._orientTopEdges(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_orientTopEdges_030_LShapeLine(self):
        cube = 'yygbbbbbborrrrrrrryggggggggyybooooooryboyyobywwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'rbybbbbbboryrrrrrrgobggggggrgyooooooyyoyyygybwwwwwwwww'
        expectedRotations = 'UUUFRUrufFRUruf'
        
        actualCube, actualRotations = solveTopFace._orientTopEdges(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_orientTopEdges_040_DotShape(self):
        cube = 'byybbbbbbgyyrrrrrroyrgggggggyyooooooyrbbyorgowwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'gbobbbbbbbrorrrrrryoyggggggbgroooooorygyyyyyywwwwwwwww'
        expectedRotations = 'FRUrufUUFRUrufFRUruf'
        
        actualCube, actualRotations = solveTopFace._orientTopEdges(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
# Analysis - solveTopFace._checkTopCorners
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
#    test 010: fully solved face
#    test 020: corners only
#    test 030: scrambled

    def test_checkTopCorners_010_solvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopFace._checkTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)

    def test_checkTopCorners_020_cornersOnly(self):
        cube = 'oyobbbbbbbybrrrrrrryrgggggggygooooooygybyryoywwwwwwwww'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopFace._checkTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopCorners_030_scrambledCube(self):
        cube = 'bgobbbbbbyoyrrrrrrrybggggggryoooooooyrgbyyyygwwwwwwwww'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopFace._checkTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveTopFace._orientTopFace
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: cube, rotations
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: top face solved
#    test 020: top cross - no corners
#    test 030: top fish aka one corner
#    test 040: two corners
    def test_orientTopFace_010_faceSolved(self):
        cube = 'brgbbbbbbogrrrrrrrgobggggggrboooooooyyyyyyyyywwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'brgbbbbbbogrrrrrrrgobggggggrboooooooyyyyyyyyywwwwwwwww'
        expectedRotations = ''
        
        actualCube, actualRotations = solveTopFace._orientTopFace(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_orientTopFace_020_noCorners(self):
        cube = 'ybybbbbbbboyrrrrrrogoggggggyrgoooooogybyyyryrwwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'grbbbbbbbrgorrrrrrbogggggggobrooooooyyyyyyyyywwwwwwwww'
        expectedRotations = 'URUrURUUrUUURUrURUUr'
        
        actualCube, actualRotations = solveTopFace._orientTopFace(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_orientTopFace_030_oneCorner(self):
        cube = 'ybrbbbbbbggrrrrrrryobggggggyrooooooooybyyygyywwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'bogbbbbbbobrrrrrrrgrbggggggrgoooooooyyyyyyyyywwwwwwwww'
        expectedRotations = 'URUrURUUrUURUrURUUr'
        
        actualCube, actualRotations = solveTopFace._orientTopFace(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)

    def test_orientTopFace_040_twoCorners(self):
        cube = 'ggrbbbbbbgbbrrrrrrrrbggggggyoyoooooooyyyyyoyywwwwwwwww'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'rrobbbbbbbbgrrrrrroorggggggggbooooooyyyyyyyyywwwwwwwww'
        expectedRotations = 'RUrURUUrURUrURUUrUUURUrURUUr'
        
        actualCube, actualRotations = solveTopFace._orientTopFace(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)

# Analysis - solveTopFace._checkTopFace
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
#    test 010: top face solved
#    test 020: top face not solved

    def test_checkTopFace_010_solvedCube(self):
        cube = 'rrobbbbbbbbgrrrrrroorggggggggbooooooyyyyyyyyywwwwwwwww'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopFace._checkTopFace(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopFace_020_unsolvedCube(self):
        cube = 'ggrbbbbbbgbbrrrrrrrrbggggggyoyoooooooyyyyyoyywwwwwwwww'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopFace._checkTopFace(cube)
        
        self.assertEqual(expectResult, actualResult)
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
#    test 020: solved bottom, middle
#    test 030: solve bottom, middle 2

    def test_solveTopFace_010_solvedCubeInput(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = {}
        expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        expectedHash = hashlib.sha256((inputDict.get('cube') + expectResult.get('rotations')).encode()).hexdigest()
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        self.assertTrue(expectedHash.find(actualResult.get('token')) > 0)
        
    def test_solveTopFace_020_solvedBottomMiddle(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'brorrrrrrygrgggggggyyoooooobyobbbbbbroybyyyygwwwwwwwww'
        
        expectResult = {}
        expectResult['rotations'] = 'UUFRUrufFRUrufRUrURUUrRUrURUUrUURUrURUUr'
        expectResult['status'] = 'ok'
        expectedHash = hashlib.sha256((inputDict.get('cube') + expectResult.get('rotations')).encode()).hexdigest()
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        self.assertTrue(expectedHash.find(actualResult.get('token')) > 0)
    
    def test_solveTopFace_020_solvedBottomMiddle2(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'rybggggggrgoooooooyoobbbbbbbyyrrrrrryygryygbywwwwwwwww'
        
        expectResult = {}
        expectResult['rotations'] = 'UUUFRUrufFRUrufRUrURUUrRUrURUUrUURUrURUUr'
        expectResult['status'] = 'ok'
        expectedHash = hashlib.sha256((inputDict.get('cube') + expectResult.get('rotations')).encode()).hexdigest()
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        self.assertTrue(expectedHash.find(actualResult.get('token')) > 0)