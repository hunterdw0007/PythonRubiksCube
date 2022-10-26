import rubik.verify as verify
import hashlib
import random
import rubik.solveBottomCross as solveBottomCross
import rubik.solveBottomCorners as solveBottomCorners
import rubik.solveMiddleLayer as solveMiddleLayer

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    if not verify._validateCube(parms.get('cube', None)):
        result['status'] = 'error: invalid cube'
    else:
        cube, bottomCrossRotations = solveBottomCross._solveBottomCross(parms.get('cube'), '')
        cube, bottomCornersRotations = solveBottomCorners._solveBottomCorners(cube, '')
        cube, middleLayerRotations = solveMiddleLayer._solveMiddleLayer(cube, '')
        result['rotations'] = bottomCrossRotations + bottomCornersRotations + middleLayerRotations
        result['status'] = 'ok'   
        result['token'] = _generateToken(parms.get('cube'), result.get('rotations'))
    return result
        
def _generateToken(inputCube, outputRotations):
    tokenHash = hashlib.sha256((inputCube + outputRotations).encode()).hexdigest()
    start = random.randint(0, hash.len()-8)
    return tokenHash[start : start + 8]
        
        
        
        