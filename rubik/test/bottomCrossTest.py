'''
Created on Sep 18, 2022

@author: Hunter
'''
import unittest
import rubik.solve as solve
import rubik.solveBottomCross as solveBottomCross

class BottomCrossTest(unittest.TestCase):

# Analysis
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
#        dict['rotations']: string, rotations to solve cube bottom cross
#        dict['status']: string, 'ok'
#    abnormal:
#        dict['status']: string, 'error: xxx', xxx is message
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: solved cube
#    test 020: solved bottom cross - unsolved cube
#    test 030: edge in bottom flipped, others solved - assume side is front
#    test 040: edge in bottom flipped, others solved any side
#    test 050: edge in botton, wrong spot
#    test 060: edge in side
#    test 070: edge in top, facing right way
#    test 080: edge in top, facing sideways
#    test 090: no edges placed initially - full solve
#
# sad path:
#    test 910: invalid cube - validateCube already tested with rotate in Iteration 1

    def test_bottomCross_010_solvedCube(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectedRotations= ''
        expectedCube = cube
        
        actualCube, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedCube, actualCube)
        
    def test_bottomCross_020_solvedCrossUnsolvedCube(self):
        cube = 'ygwybbobrryworgyrwbgbygyrgryboboobogoooryrgrbwwgwwwywg'
        
        expectedRotations= ''
        expectedCube = cube
        
        actualCube, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedCube, actualCube)
        
    def test_bottomCross_030_flippedEdgeOnBottomF(self):
        cube = 'grwoboywbbboyrgrrwggbygyrgrybrbogbogorwryoyyoobwwwwywg'
        
        expectedRotations = 'FlULUUFF'
        
        _, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_040_flippedEdgeOnBottom(self):
        cube = 'worrbgwbrgggorrgwowggbgyygroboboyboryrooyybyybwwwwrywb'
        
        expectedRotations = 'RfUFUURR'
        
        _, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_050_edgeInWrongPositionBottom(self):
        cube = 'yoyroyorbrbwrbowborbyyroyrwgyrggbrggoobgyybwgwwowwwggb'
        
        expectedRotations = 'FFUUBB'
        
        _, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_060_edgeInSide(self):
        cube = 'gywyrwyrogbwrgrbgrrggyoryoywbybborboooboyyogrbgwwwwbwg'
        
        expectedRotations = 'RUrFF'
        
        _, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_070_edgeInTopUpwards(self):
        cube = 'gbwyroyrwrbyggrrgrgywyoryoybrobborboogowyowybbggwwwbwg'
        
        expectedRotations = 'UUUFF'
        
        _, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_080_edgeInTopSideways(self):
        cube = 'bwwgrgoyybyrogrogrwrwyoryoyrbobbyrbgbggoyoyrowbgwwwbwg'
        
        expectedRotations = 'FRurfUUFF'
        
        _, actualRotations = solveBottomCross._solveBottomCross(cube, '')
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_090_fullBottomCrossSolve(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'ygwybrgbbooryrbrowwoywgworbrrbrogygogwgbybowgyywowyrgb'
        
        expectResult = {}
        expectedRotations = 'ruRUUFFruRBBruRURRULL'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertTrue(actualResult.get('rotations').startswith(expectedRotations))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_910_invalidCubeString(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = ''
        
        expectResult = {}
        expectResult['status'] = 'error: invalid cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))