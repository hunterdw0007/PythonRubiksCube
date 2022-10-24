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
#    test 020: solved bottom not middle
#    test 030: solved middle, scrambled elsewhere

    def test_checkTopCross_010_solvedTopCrossOfSolvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        #checking that cube is valid
        self.assertTrue(verify._validateCube(cube))
        
        expectResult = True
        
        actualResult = solveTopCross._checkTopCross(cube)
        
        self.assertEqual(expectResult, actualResult)