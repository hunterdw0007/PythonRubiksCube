import rubik.cube as rubik
import rubik.rotate as rotate

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    if not rotate._validateCube(parms.get('cube', None)):
        result['status'] = 'error: invalid cube'
    else:
        encodedCube = parms
        encodedCube['solution'] = ''
        result = _solveBottomCross(encodedCube)
        result['status'] = 'ok'                   
    return result

def _solveBottomCross(cubeDict):
    outputDict = {}
    outputDict = cubeDict
    if (outputDict.get('cube')[rotate.cubeEnum.B11.value] == \
    (   outputDict.get('cube')[rotate.cubeEnum.B01.value] 
    and outputDict.get('cube')[rotate.cubeEnum.B10.value] 
    and outputDict.get('cube')[rotate.cubeEnum.B12.value] 
    and outputDict.get('cube')[rotate.cubeEnum.B21.value] ))\
    and outputDict.get('cube')[rotate.cubeEnum.F11.value] == outputDict.get('cube')[rotate.cubeEnum.F21.value]\
    and outputDict.get('cube')[rotate.cubeEnum.R11.value] == outputDict.get('cube')[rotate.cubeEnum.R21.value]\
    and outputDict.get('cube')[rotate.cubeEnum.B11.value] == outputDict.get('cube')[rotate.cubeEnum.B21.value]\
    and outputDict.get('cube')[rotate.cubeEnum.L11.value] == outputDict.get('cube')[rotate.cubeEnum.L21.value]:
        return outputDict
    
    outputDict['solution'] = 'FlUUULFF'
    outputDict['cube'] = rotate._rotate({'cube':outputDict.get('cube'),'dir':outputDict.get('solution')})['cube']
    _solveBottomCross(outputDict)