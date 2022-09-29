'''
Created on Sep 18, 2022

@author: Hunter
'''
import unittest
import rubik.solve as solve

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
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = {}
        expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_020_solvedCrossUnsolvedCube(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'ygwybbobrryworgyrwbgbygyrgryboboobogoooryrgrbwwgwwwywg'
        
        expectResult = {}
        expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_030_flippedEdgeOnBottomF(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'grwoboywbbboyrgrrwggbygyrgrybrbogbogorwryoyyoobwwwwywg'
        
        expectResult = {}
        expectResult['rotations'] = 'FlULUUFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_040_flippedEdgeOnBottom(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'worrbgwbrgggorrgwowggbgyygroboboyboryrooyybyybwwwwrywb'
        
        expectResult = {}
        expectResult['rotations'] = 'RfUFUURR'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_050_edgeInWrongPositionBottom(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'yoyroyorbrbwrbowborbyyroyrwgyrggbrggoobgyybwgwwowwwggb'
        
        expectResult = {}
        expectResult['rotations'] = 'FFUUBB'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_060_edgeInSide(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gywyrwyrogbwrgrbgrrggyoryoywbybborboooboyyogrbgwwwwbwg'
        
        expectResult = {}
        expectResult['rotations'] = 'RUrFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_070_edgeInTopUpwards(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gbwyroyrwrbyggrrgrgywyoryoybrobborboogowyowybbggwwwbwg'
        
        expectResult = {}
        expectResult['rotations'] = 'UUUFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_080_edgeInTopSideways(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'bwwgrgoyybyrogrogrwrwyoryoyrbobbyrbgbggoyoyrowbgwwwbwg'
        
        expectResult = {}
        expectResult['rotations'] = 'FRurfUUFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_090_fullBottomCrossSolve(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'ygwybrgbbooryrbrowwoywgworbrrbrogygogwgbybowgyywowyrgb'
        
        expectResult = {}
        expectResult['rotations'] = 'ruRUUFFruRBBruRURRULL'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_910_invalidCubeString(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = ''
        
        expectResult = {}
        expectResult['status'] = 'error: invalid cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))