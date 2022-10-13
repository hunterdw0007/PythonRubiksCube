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

# Analysis - solve._locateMiddlePieceInTop
#
# inputs:
#    cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives validated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: integer, 0-54 corresponding to location
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
        
        
        
            