'''
Created on Nov 6, 2022

@author: Hunter
'''
import unittest
import rubik.verify as verify
import rubik.solve as solve
import rubik.solveTopLayer as solveTopLayer


class TopLayerTest(unittest.TestCase):

# Analysis - solveTopLayer._checkTopLayer
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
#    test 030: scrambled cube except top
    def test_checktopLayer_010_solvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopLayer._checkTopLayer(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checktopLayer_020_scrambledCube(self):
        cube = 'rgbbbbyybyborrrywrwgogggwrgywgoooowrgwbbyywyogorowrwyb'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopLayer._checkTopLayer(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checktopLayer_030_solvedTopOnly(self):
        cube = 'wwwbwwggogggggbbooyyyoyowyybbbgbwbborrrrrrrrryywyowoog'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopLayer._checkTopLayer(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveTopLayer._checkTopCorners
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
#    test 030: scrambled cube except top corners
    def test_checkTopCorners_010_solvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopLayer._checkTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopCorners_020_scrambledCube(self):
        cube = 'rgbbbbyybyborrrywrwgogggwrgywgoooowrgwbbyywyogorowrwyb'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopLayer._checkTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checktopCorners_030_solvedTopCorners(self):
        cube = 'wywwwryrrbwbybbwygybyyybwwrgggwggbrrooooooooogbbgrgyrr'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopLayer._checkTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)

# Analysis - solveTopLayer._checkTopEdges
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
#    test 010: fully solved
#    test 020: scrambled
#    test 030: solved, rotated

    def test_checkTopEdges_010_solvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopLayer._checkTopEdges(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopEdges_020_scrambledCube(self):
        cube = 'rgbbbbyybyborrrywrwgogggwrgywgoooowrgwbbyywyogorowrwyb'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopLayer._checkTopEdges(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopEdges_030_solvedCubeRotated(self):
        cube = 'gggbbbbbbrrroooooobbbggggggooorrrrrrwwwwwwwwwyyyyyyyyy'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopLayer._checkTopEdges(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveTopLayer._locateTopCorners
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: int [-1:3]
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: no headlights
#    test 020: headlights on back
#    test 030: headlights on left
#    test 040: headlights on front
#    test 050: headlights on right

    def test_locateTopCorners_010_noHeadlights(self):
        cube = 'rrobbbbbbgbbooooooogrggggggbogrrrrrrwwwwwwwwwyyyyyyyyy'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = 0
        
        actualResult = solveTopLayer._locateTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_locateTopCorners_020_backHeadlights(self):
        cube = 'obrbbbbbbbgooooooogogggggggrrbrrrrrrwwwwwwwwwyyyyyyyyy'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = 0
        
        actualResult = solveTopLayer._locateTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_locateTopCorners_030_leftHeadlights(self):
        cube = 'rrbbbbbbbobroooooobgogggggggogrrrrrrwwwwwwwwwyyyyyyyyy'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = 1
        
        actualResult = solveTopLayer._locateTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_locateTopCorners_040_frontHeadlights(self):
        cube = 'gogbbbbbbrrbooooooobrggggggbgorrrrrrwwwwwwwwwyyyyyyyyy'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = 2
        
        actualResult = solveTopLayer._locateTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_locateTopCorners_050_rightHeadlights(self):
        cube = 'bgobbbbbbgogoooooorrbggggggobrrrrrrrwwwwwwwwwyyyyyyyyy'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = 3
        
        actualResult = solveTopLayer._locateTopCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
    
# Analysis - solveTopLayer._positionTopCorners
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
#    test 010: correctly solved corners
#    test 020: front corners swapped
#    test 030: back corners swapped
#    test 040: no headlights

    def test_positionTopCorners_010_correctlySolved(self):
        cube = 'brbbbbbbbobooooooogggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'brbbbbbbbobooooooogggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = solveTopLayer._positionTopCorners(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
    
    def test_positionTopCorners_020_frontCornersSwapped(self):
        cube = 'obrbbbbbbbgooooooogogggggggrrbrrrrrrwwwwwwwwwyyyyyyyyy'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'obobbbbbbgggoooooororggggggbrbrrrrrrwwwwwwwwwyyyyyyyyy'
        expectedRotations = 'rFrBBRfrBBRR'
        
        actualCube, actualRotations = solveTopLayer._positionTopCorners(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_positionTopCorners_030_backCornersSwapped(self):
        cube = 'rgrbbbbbbboooooooogrbggggggobgrrrrrrwwwwwwwwwyyyyyyyyy'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'grgbbbbbbrbroooooobgbggggggooorrrrrrwwwwwwwwwyyyyyyyyy'
        expectedRotations = 'UUrFrBBRfrBBRR'
        
        actualCube, actualRotations = solveTopLayer._positionTopCorners(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)