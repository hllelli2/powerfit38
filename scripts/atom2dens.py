from __future__ import absolute_import
import sys

from powerfit.structure import Structure
from powerfit.volume_helpers import structure_to_shape

def main():

    structure = Structure.fromfile(sys.argv[1])
    template = structure_to_shape(
          structure.coor, resolution=float(sys.argv[2]),
          weights=structure.atomnumber, shape='vol'
          )
    template.to_file(sys.argv[3])

if __name__ == '__main__':
    main()