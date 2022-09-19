'''
Created on Sep 18, 2022

@author: Hunter
'''
import unittest
import rubik.solve as solve

class BottomCrossTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

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
#        dict['solution']: string, rotations to solve cube bottom cross
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
#
# sad path:
#    test 910: invalid cube - validateCube already tested with rotate in Iteration 1

    def test_bottomCross_010_solvedCube(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = {}
        expectResult['solution'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_020_solvedCrossUnsolvedCube(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'ygwybbobrryworgyrwbgbygyrgryboboobogoooryrgrbwwgwwwywg'
        
        expectResult = {}
        expectResult['solution'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_030_flippedEdgeOnBottomF(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'grwoboywbbboyrgrrwggbygyrgrybrbogbogorwryoyyoobwwwwywg'
        
        expectResult = {}
        expectResult['solution'] = 'FlUUULFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_040_flippedEdgeOnBottom(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'worrbgwbrgggorrgwowggbgyygroboboyboryrooyybyybwwwwrywb'
        
        expectResult = {}
        expectResult['solution'] = 'RfUUUFRR'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_050_edgeInWrongPosition(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'yoyroyorbrbwrbowborbyyroyrwgyrggbrggoobgyybwgwwowwwggb'
        
        expectResult = {}
        expectResult['solution'] = 'FFUUBB'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_060_edgeInSide(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gywyrwyrogbwrgrbgrrggyoryoywbybborboooboyyogrbgwwwwbwg'
        
        expectResult = {}
        expectResult['solution'] = 'RUrFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_070_edgeInTopUpwards(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gbwyroyrwrbyggrrgrgywyoryoybrobborboogowyowybbggwwwbwg'
        
        expectResult = {}
        expectResult['solution'] = 'UUUFF'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_910_invalidCubeString(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = ''
        
        expectResult = {}
        expectResult['status'] = 'error: invalid cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))