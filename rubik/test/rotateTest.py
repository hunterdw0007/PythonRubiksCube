'''
Created on Sep 1, 2022

@author: Hunter
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
#    test 060 - 160: valid cube with R,r,L,l,U,u,D,d,B,b rotations
#
# sad path:
#    test 910: missing cube with valid rotation
#    test 920: valid cube with invalid rotation
#    test 930: 


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
        inputDict['dir']  = 'F'
        
        expectResult = {}
        expectResult['cube'] = '' #TODO: figure out rotation
        expectResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))

