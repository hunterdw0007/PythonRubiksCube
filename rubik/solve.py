import rubik.cube as rubik
import rubik.rotate as rotate

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    if not rotate._validateCube(parms.get('cube', None)):
        result['status'] = 'error: invalid cube'
    else:
        solution = _solveBottomCross(parms.get('cube'), '')
        result['solution'] = solution
        result['status'] = 'ok'                   
    return result

def _solveBottomCross(cube, solution):

    if (cube[rotate.cubeEnum.B11.value] == \
    (   cube[rotate.cubeEnum.B01.value] 
    and cube[rotate.cubeEnum.B10.value] 
    and cube[rotate.cubeEnum.B12.value] 
    and cube[rotate.cubeEnum.B21.value] ))\
    and cube[rotate.cubeEnum.F11.value] == cube[rotate.cubeEnum.F21.value]\
    and cube[rotate.cubeEnum.R11.value] == cube[rotate.cubeEnum.R21.value]\
    and cube[rotate.cubeEnum.B11.value] == cube[rotate.cubeEnum.B21.value]\
    and cube[rotate.cubeEnum.L11.value] == cube[rotate.cubeEnum.L21.value]:
        return solution
    
    solution = 'FlUUULFF'
    cube = rotate._rotate({'cube':cube,'dir':solution})['cube']
    return _solveBottomCross(cube, solution)