#------ BAND STRUCTURE ------#

# Use vaspkit for DFT band structure. Get BAND.dat and KLABELS file.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('text', usetex = True)        # for LaTeX
plt.style.use('default')                    # plot style.

# Loading the file
band = np.loadtxt('BAND.dat')

# The Energy interval(eV), i.e., y-range.
ymax =  5
ymin = -5

# The symmetry k-points. The values in KLABELS file.
X0=0.0
X1=0.86032
X2=1.56277
X3=2.05947
X4=3.05289
X5=4.10656
X6=4.45779

fig, ax = plt.subplots()

# Setting x and y limits.
# Set y-limits above in 'ymin' and 'ymax'
# For x-limit it is preffered to set from 'X0' to the 'XN'. N is the last symmetry point.
ax.set_xlim(X0, X6)
ax.set_ylim(ymin, ymax)
ax.set_ylabel("$E-E_F$ (eV)", fontsize=14)

ax.set_xticks([X0, X1, X2, X3, X4, X5, X6])

# Give labels to the symmetry k-points. Again look in KLABELS file.
ax.set_xticklabels(['$\Gamma$', 'L', 'W', 'X', '$\Gamma$', 'K', 'X'], fontsize=14)

ax.grid()

ax.plot(band[:,0], band[:,1],linewidth=2, color='darkgreen' )

plt.tight_layout()

# Saving fig as png or eps.
plt.savefig('bandstructure.png', dpi=200)
# plt.savefig('bandstructure.eps')

plt.show()


