import rubik.cube as rubik

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    encodedCube = parms.get('cube',None)
    result['solution'] = ''
    result['status'] = 'ok'                     
    return result