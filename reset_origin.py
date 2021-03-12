from pymol import cmd, cgo
import numpy as np

def shift_to_center(selection):
    # center a molecule
    com = cmd.centerofmass(selection, -1.0)
    shift = np.array2string(np.negative(np.array(com)), separator=', ')
    cmd.translate(shift, selection, camera = 0)
    print('Shifting {} to {}'.format(selection, shift))

def orient_origin(selection):
    shift_to_center(selection)
    cmd.orient(selection)
    cv = list(cmd.get_view(quiet=1))
    #cmd.origin(selection, position=origin1)
    cmd.transform_selection(selection,  cv[0:3]+[0.0]+ cv[3:6]+[0.0]+
                            cv[6:9]+[0.0]+ cv[12:15]+[1.0], transpose=1)
    cmd.reset()

cmd.extend("orient_origin", orient_origin)
