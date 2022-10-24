'''
Created on Oct 24, 2022

@author: Hunter
'''
import unittest
import rubik.verify as verify
import rubik.solveTopCross as solveTopCross

class Test(unittest.TestCase):

# Analysis - solveTopCross._checkTopCross
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
        
        actualResult = solveTopCross._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopCross_020_scrambledCube(self):
        cube = 'rgbbbbyybyborrrywrwgogggwrgywgoooowrgwbbyywyogorowrwyb'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = False
        
        actualResult = solveTopCross._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)
        
    def test_checkTopCross_030_scrambledCubeExceptCross(self):
        cube = 'ybygbywbwoogooygyyrgorgbobywrgorrrgrbwwwwwrwbbyooygbrg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopCross._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)
        
# Analysis - solveTopCross._checkTopState
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
#    test 020: line on top
#    test 030: L on top
#    test 040: dot on top

def test_checkTopState_010_topCrossSolved(self):
        cube = 'grbbbbbbbrbyrrrrrrgobggggggygroooooooyoyyyyyywwwwwwwww'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = 0
        
        actualResult = solveTopCross._checkTopState(cube)
        
        self.assertEqual(expectResult, actualResult)
        