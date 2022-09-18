import rubik.cube as rubik
import rubik.rotate as rotate

def _solve(parms):
    """Return rotates needed to solve input cube"""
    encodedCube = parms.get('cube',None)
    result = _solveBottomCross(encodedCube)
    result['status'] = 'ok'                   
    return result

def _solveBottomCross(outputDict):
    cubeString = outputDict.get('cube')
    rotString = outputDict.get('solution')
    
    if (cubeString[rotate.cubeEnum.B11.value] == \
    (   cubeString[rotate.cubeEnum.B01.value] 
    and cubeString[rotate.cubeEnum.B10.value] 
    and cubeString[rotate.cubeEnum.B12.value] 
    and cubeString[rotate.cubeEnum.B21.value] ))\
    and cubeString[rotate.cubeEnum.F11.value] == cubeString[rotate.cubeEnum.F21.value]\
    and cubeString[rotate.cubeEnum.R11.value] == cubeString[rotate.cubeEnum.R21.value]\
    and cubeString[rotate.cubeEnum.B11.value] == cubeString[rotate.cubeEnum.B21.value]\
    and cubeString[rotate.cubeEnum.L11.value] == cubeString[rotate.cubeEnum.L21.value]:
        return outputDict