from __future__ import absolute_import
from __future__ import print_function
import sys

import numpy as np
from numpy.fft import fftn

from powerfit import Volume
from powerfit._powerfit import fsc_curve
from six.moves import range

vol1 = Volume.from_file(sys.argv[1])
vol2 = Volume.from_file(sys.argv[2])

ft_vol1 = fftn(vol1.array)
ft_vol2 = fftn(vol2.array)

fsc = fsc_curve(ft_vol1, ft_vol2)
res = [n / vol1.dimensions[0] for n in range(fsc.size)]
inv_res = [1 / r for r in res[1:]]

print(fsc)
print()
print(res)
print()
print(inv_res)

