'''
Created on Sep 26, 2022

@author: Hunter
'''
import unittest
import rubik.solve as solve
import rubik.rotate as rotate

class Test(unittest.TestCase):

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
#        dict['rotations']: string, rotations to solve cube bottom
#        dict['status']: string, 'ok'
#    abnormal:
#        dict['status']: string, 'error: xxx', xxx is message
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: solved corners - not bottom cross
#    test 015: position corner in top check
#    test 020: solved bottom - unsolved cube
#    test 030: three corners solved, unsolved one above where it needs to go
#    test 040: three corders solved, unsolved on in top not where it needs to go
#    test 050: three corners solved, unsolved in its spot but rotated incorrectly
#    test 060: no corners solved, unsolved all in top
#    test 070: no corners solved, unsolved all in bottom
#    test 080: no corners solved, unsolved randomly distributed
#    test 090: completely scrambled cube, solve bottom cross and corners
#

    def test_bottomCorners_010_solvedBottomCornersVerify(self):
        cube = 'bgbgbgbgbrororororgbgbgbgbgororororoywywywywywywywywyw'
        
        expectResult = True
        
        actualResult = solve._checkBottomCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_bottomCorners_015_positionCornerInTop(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        location = rotate.cubeEnum.F02.value
        
        expectedCube = 'orobbbggggggorororrorgggbbbbbbrororowywwywwywyyywwwyyy'
        expectedRotations = 'UUU'
        expectedLocation = rotate.cubeEnum.R02.value
        
        actualCube, actualLocation, actualRotations = solve._positionCornerInTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCorners_020_solvedBottomBaseCase(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectResult = {}
        expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
    
     
    def test_bottomCorners_030_unsolvedAbovePosition(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'rgwyobooybobobrgbbygybrbrrrgrbygrgggooogyyyyowwrwwwwww'
        
        expectResult = {}
        expectResult['rotations'] = 'RurURurURurURurURurU'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
    