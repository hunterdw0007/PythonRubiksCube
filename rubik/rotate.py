import rubik.cube as rubik
import re

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    rotatedCube = encodedCube                  #STUB:  rotate the cube
    result['cube'] = 'orgowobgrowwwrwggwrbgrybgorywyroybyorobbbgbyywrwbgyygo'               
    result['status'] = 'ok'                     
    return result

def _validate(cube):
    if len(cube) != 54:
        return False
    if re.search(r'^[bgorwy]*$', cube) != None:
        return False
    return True