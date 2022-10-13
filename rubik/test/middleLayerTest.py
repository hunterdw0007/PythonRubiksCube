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

# Analysis - solve._checkMiddleLayer
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

    def test_middleLayer_010_solvedMiddleEdgesOfSolvedCubeCheck(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = True
        
        actualResult = solveMiddleLayer._checkMiddleLayer(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_middleLayer_020_solvedMiddleEdgesOfSolvedBottomCheck(self):
        cube = 'byybwbwwwbyrrrorrrboobyryyywoowowooobwwybrybrggggggggg'
        
        #checking that cube is valid
        self.assertEqual(verify._validateCube(cube), True)
        
        expectResult = False
        
        actualResult = solveMiddleLayer._checkMiddleLayer(cube)
        
        self.assertEqual(expectResult, actualResult)
