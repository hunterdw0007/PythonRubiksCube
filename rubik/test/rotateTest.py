'''
Created on Sep 1, 2022

@author: Hunter Westerlund
'''
import unittest
import rubik.rotate as rotate


class RotateTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    
# Analysis
#
# inputs:
#    parms: dict: mandatory: arrives validated
#    parms['op']: string; 'rotate', mandatory, arrives validated
#    parms['cube']: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives unvalidated
#    parms['dir']: string; len .GE. 0, [FfRrLlUuDdBb]; optional, defaulting to F if missing; arrives unvalidated
#
# outputs:
#    side-effects: no state changes; no external effects
#    returns: dict
#    nominal:
#        dict['cube']: string, valid cube
#        dict['status']: string, 'ok'
#    abnormal:
#        dict['status']: string, 'error: xxx', xxx is message
#
#    confidence level: boundary value analysis
#
# happy path:
#    test 010: valid cube with F rotation
#    test 020: valid cube with f rotation
#    test 030: valid cube with missing rotation
#    test 040: valid cube with '' rotation
#    test 050: valid cube with no 'dir' key-value pair
#    test 060 - 150: valid cube with R,r,L,l,U,u,D,d,B,b rotations one each
#    test 160: valid cube with multiple rotations
#
# sad path:
#    test 910: missing cube with valid rotation
#    test 920: valid cube with invalid rotation
#    test 930: invalid cube with valid rotation

    def test_rotate_010_shouldRotateValidCubeF(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'F'
        
        expectResult = {}
        expectResult['cube'] = 'orgowobgrowwwrwggwrbgrybgorywyroybyorobbbgbyywrwbgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))

    def test_rotate_020_shouldRotateValidCubef(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'f'
        
        expectResult = {}
        expectResult['cube'] = 'rgbowogroowwyrwygwrbgrybgorywgrowbyorobbbgwrwyybbgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_030_validCubeMissingDir(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = None
        
        expectResult = {}
        expectResult['cube'] = 'orgowobgrowwwrwggwrbgrybgorywyroybyorobbbgbyywrwbgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_040_validCubeEmptyDir(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = ''
        
        expectResult = {}
        expectResult['cube'] = 'orgowobgrowwwrwggwrbgrybgorywyroybyorobbbgbyywrwbgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_050_validCubeNoDirKey(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        
        expectResult = {}
        expectResult['cube'] = 'orgowobgrowwwrwggwrbgrybgorywyroybyorobbbgbyywrwbgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_060_shouldRotateValidCubeR(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'R'
        
        expectResult = {}
        expectResult['cube'] = 'goorwyooowrwgrwwwwgbggybborywyroybybrorbbgowbyygbgrygr'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_070_shouldRotateValidCuber(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'r'
        
        expectResult = {}
        expectResult['cube'] = 'gobrwgoogwwwwrgwrwobgyyboorywyroybybrogbbrowryyrbggygb'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
    
    def test_rotate_080_shouldRotateValidCubeB(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'B'
        
        expectResult = {}
        expectResult['cube'] = 'gorrwgoobwworrgwgygrroybrbgbwyooyrybwwwbbgowgyyobgyyrb'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
    
    def test_rotate_090_shouldRotateValidCubeb(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'b'
        
        expectResult = {}
        expectResult['cube'] = 'gorrwgoobwwrrrowgbgbrbyorrgywygoyoybbrybbgowgyyobgywww'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
    
    def test_rotate_100_shouldRotateValidCubeL(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'L'
        
        expectResult = {}
        expectResult['cube'] = 'rorbwgoobwwwrrwwgwrbyrybgoybryyowbyyrobbbggwggyorgyogo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_110_shouldRotateValidCubel(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'l'
        
        expectResult = {}
        expectResult['cube'] = 'yorbwgyobwwwrrwwgwrborybgoryybwoyyrbgobrbgowgryobgyggo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
    
    def test_rotate_120_shouldRotateValidCubeU(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'U'
        
        expectResult = {}
        expectResult['cube'] = 'wwwrwgoobrbgrrwwgwywyrybgorgorroybybobrwboggbyyobgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))    
    
    def test_rotate_130_shouldRotateValidCubeu(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'u'
        
        expectResult = {}
        expectResult['cube'] = 'ywyrwgoobgorrrwwgwwwwrybgorrbgroybybbggobwrboyyobgyygo'
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
                    
    def test_rotate_910_missingCube(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['dir']  = 'F'
        
        expectResult = {}
        expectResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_920_validCubeInvalidRotation(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        inputDict['dir']  = 'Q'
        
        expectResult = {}
        expectResult['status'] = 'error: invalid rotation'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_rotate_930_invalidCube(self):
        inputDict = {}
        inputDict['op']   = 'rotate'
        inputDict['cube'] = ''
        inputDict['dir']  = 'F'
        
        expectResult = {}
        expectResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
# Analysis: Validate Cube Function
#
#    inputs:
#        cube: string; len=54, [browyg], 9 occurences of each character, unique middle color; mandatory; arrives unvalidated
#
#    outputs:
#        side-effects: no state changes; no external effects
#        returns:
#            nominal: True
#            abnormal: False
#        confidence level: BVA
#
#    happy path:
#        test 010: valid cube in solved state
#        test 020: valid cube in scrambled state
#    
#    sad path:
#        test 910: empty cube string
#        test 920: string length not equal to 54
#        test 930: invalid color in string
#        test 940: count of any color not equal to nine
#        test 950: centers are not all different
#        
    def test_validateCube_010_validCubeSolved(self):
        input = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectedResult = True
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateCube_020_validCubeScrambled(self):
        input = 'gorrwgoobwwwrrwwgwrbgrybgorywyroybybrobbbgowgyyobgyygo'
        
        expectedResult = True
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateCube_910_emptyCubeString(self):
        input = ''
        
        expectedResult = False
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateCube_920_stringLengthNot54(self):
        input = 'wryobg'
        
        expectedResult = False
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateCube_930_invalidColor(self):
        input = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbppppppppp'
        
        expectedResult = False
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateCube_940_countNotNine(self):
        input = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooogggggggggggggggggg'
        
        expectedResult = False
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateCube_950_centersNotDifferent(self):
        input = 'wwwwrwwwwwrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        
        expectedResult = False
        
        actualResult = rotate._validateCube(input)
        
        self.assertEqual(expectedResult, actualResult)
        
# Analysis: Rotate Face CW Function
#
#    inputs:
#        face: list[string]; len=9, [browyg]; mandatory; arrives validated
#
#    outputs:
#        side-effects: no state changes; no external effects
#        returns:
#            nominal: list[string]; len=9, [browyg]
#        confidence level: BVA
#
#    happy path:
#        test 010: solved face rotated CW
#        test 020: scrambled face rotated CW
#

    def test_faceCW_010_rotatedClockwiseSolved(self):
        input = list('wwwwwwwww')
        
        expectedResult = list('wwwwwwwww')
        
        actualResult = rotate._faceCW(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_faceCW_020_rotatedClockwiseScrambled(self):
        input = list('gorrwgoob')
        
        expectedResult = list('orgowobgr')
        
        actualResult = rotate._faceCW(input)
        
        self.assertEqual(expectedResult, actualResult)
        
# Analysis: Rotate Face CCW Function
#
#    inputs:
#        face: string; len=9, [browyg]; mandatory; arrives validated
#
#    outputs:
#        side-effects: no state changes; no external effects
#        returns:
#            nominal: string; len=9, [browyg]
#        confidence level: BVA
#
#    happy path:
#        test 010: solved face rotated CW
#        test 020: scrambled face rotated CW
#

    def test_faceCCW_010_rotatedCounterclockwiseSolved(self):
        input = list('wwwwwwwww')
        
        expectedResult = list('wwwwwwwww')
        
        actualResult = rotate._faceCCW(input)
        
        self.assertEqual(expectedResult, actualResult)

    def test_faceCCW_020_rotatedCounterclockwiseScrambled(self):
        input = list('gorrwgoob')
        
        expectedResult = list('rgbowogro')
        
        actualResult = rotate._faceCCW(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    
# Analysis: Validate Direction Function
#
#    inputs:
#        dir: string; len .GE. 0, [FfRrLlUuDdBb]; mandatory; arrives unvalidated
#
#    outputs:
#        side-effects: no state changes; no external effects
#        returns:
#            nominal: True
#            abnormal: False
#        confidence level: BVA
#
#    happy path:
#        test 010: empty string
#        test 020: string of valid rotations
#
#    sad path:
#        test 910: invalid rotation char

    def test_validateDir_010_EmptyString(self):
        input = ''
        
        expectedResult = True
        
        actualResult = rotate._validateDir(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateDir_020_ValidString(self):
        input='FfRrLlUuDdBb'
        
        expectedResult = True
        
        actualResult = rotate._validateDir(input)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validateDir_910_invalidChar(self):
        input='GHgh'
        
        expectedResult = False
        
        actualResult = rotate._validateDir(input)
        
        self.assertEqual(expectedResult, actualResult)
