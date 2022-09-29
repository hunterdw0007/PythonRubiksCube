'''
Created on Sep 26, 2022

@author: Hunter
'''
import unittest
import rubik.solve as solve

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
#    test 020: solved bottom - unsolved cube
#    test 030: three corners solved, unsolved one above where it needs to go
#    test 040: three corders solved, unsolved on in top not where it needs to go
#    test 050: three corners solved, unsolved in its spot but rotated incorrectly
#    test 060: no corners solved, unsolved all in top
#    test 070: no corners solved, unsolved all in bottom
#    test 080: no corners solved, unsolved randomly distributed
#    test 090: completely scrambled cube, solve bottom cross and corners
#
# sad path:
#    test 910: invalid cube - validateCube already tested with rotate in Iteration 1

    def test_bottomCornersTest_010_solvedBottomCornersVerify(self):
        inputDict = {}
        inputDict['op']   = 'solve'
        inputDict['cube'] = 'gbggbggbgorooroorobgbbgbbgbrorrorrorywywywywywywywywyw'
        
        expectResult = True
        
        actualResult = solve._checkBottomCorners(inputDict.get('cube'))
        
        self.assertEqual(expectResult, actualResult)
    
    
    