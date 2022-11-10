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
#    test 020: corners rotated around
#    test 030: corners unsolved
    def test_positionTopCorners_010_correctlySolved(self):
        cube = 'brbbbbbbbobooooooogggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy'
    
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectedCube = 'brbbbbbbbobooooooogggggggggrorrrrrrrwwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = solveTopLayer._positionTopCorners(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)