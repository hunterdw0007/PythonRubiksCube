import rubik.rotate as rotate
import rubik.verify as verify
import rubik.solveBottomCross as solveBottomCross
import rubik.solveBottomCorners as solveBottomCorners

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    if not verify._validateCube(parms.get('cube', None)):
        result['status'] = 'error: invalid cube'
    else:
        cube, bottomCrossRotations = solveBottomCross._solveBottomCross(parms.get('cube'), '')
        cube, bottomCornersRotations = solveBottomCorners._solveBottomCorners(cube, '')
        result['rotations'] = bottomCrossRotations + bottomCornersRotations
        result['status'] = 'ok'                   
    return result
        
        
        
        
        
        