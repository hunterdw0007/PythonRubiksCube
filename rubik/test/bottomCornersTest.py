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
#    test 011: position corner in top function
#    test 012: check bottom corner orientation function
#    test 020: solved bottom - unsolved cube
#    test 030: three corners solved, unsolved one above where it needs to go
#    test 031: three corners solved, unsolved one above where it needs to go, not F02 corner
#    test 040: three corders solved, unsolved on in top not where it needs to go
#    test 041: three corders solved, unsolved on in top not where it needs to go, not F02 corner
#    test 050: three corners solved, unsolved in its spot but rotated incorrectly
#    test 051: two corners solved, others swapped in bottom
#    test 060: no corners solved, unsolved all in top
#    test 070: no corners solved, unsolved all in bottom
#    test 080: completely scrambled cube, solve bottom cross and corners

    def test_bottomCorners_010_solvedBottomCornersVerify(self):
        cube = 'bgbgbgbgbrororororgbgbgbgbgororororoywywywywywywywywyw'
        
        expectResult = True
        
        actualResult = solve._checkBottomCorners(cube)
        
        self.assertEqual(expectResult, actualResult)
    
    def test_bottomCorners_011_positionCornerInTop(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        location = rotate.cubeEnum.F02.value
        
        expectedCube = 'orobbbggggggorororrorgggbbbbbbrororowywwywwywyyywwwyyy'
        expectedRotations = 'UUU'
        expectedLocation = rotate.cubeEnum.R02.value
        
        actualCube, actualLocation, actualRotations = solve._positionCornerInTop(cube, location)
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCorners_012_checkBottomCornerOrientation(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        locations = [rotate.cubeEnum.F22.value, rotate.cubeEnum.R22.value, rotate.cubeEnum.B22.value, rotate.cubeEnum.L22.value]
        
        for location in locations:
            self.assertTrue(solve._checkBottomCornerOrientation(cube, location))
        
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
        expectResult['rotations'] = 'RUruRUruRUruRUruRUru'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_031_unsolvedAbovePositionNotF(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'ggbrbybbbryworbrrygggrgbbggybyoogoooryryyrooywwwwwwwwo'
        
        expectResult = {}
        expectResult['rotations'] = 'BUbuBUbuBUbuBUbuBUbu'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_040_unsolvedNotAbovePosition(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'bygrbybbrobborybrryryggbgggrgroogooogbooyywrywwywwwwww'
        
        expectResult = {}
        expectResult['rotations'] = 'UUURUruRUruRUru'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_041_unsolvedNotAbovePositionNotF(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'rbrrbybbbgrooryrroygbggbyggrygoogoooyogrybwyywwwwwwwwb'
        
        expectResult = {}
        expectResult['rotations'] = 'UUBUbuBUbuBUbu'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_050_unsolvedInPositionRotated(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'ryborbrrgyggrgbwggobroogoooggbrbybbbyyyoyyyrowwrwwwwww'
        
        expectResult = {}
        expectResult['rotations'] = 'RUruRUru'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_051_cornersInBottomSwapped(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'bryrbobbrrbygrygrwgorggbbggyyooogooobyoryyybgwwwwwwwwr'
        
        expectResult = {}
        expectResult['rotations'] = 'RUruUUUBUbuBUbuBUbuBUbuBUbuURUruRUruRUruRUruRUru'
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_060_allCornersInTopUnsolved(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'brggbybbywbworrgrygobygbogywgwrooborrbryyyogoywrwwwowg'
        
        expectResult = {}
        #expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        #self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_070_allCornersInBottomUnsolved(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gorobgobwyyyrryrrwrgobgyogrbrygobwogyogbyroybwwgwwwbwb'
        
        expectResult = {}
        #expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        #self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_080_cubeCompletelyScrambled(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gwogwbbyrbyowroyyowwwgyogoorrwyowwrrbrbbbgroyybgggrgby'
        
        expectResult = {}
        #expectResult['rotations'] = ''
        expectResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        #self.assertEqual(expectResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))