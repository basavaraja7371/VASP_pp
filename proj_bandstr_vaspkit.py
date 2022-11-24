#------ PROJECTED BAND STRUCTURE ------#

# Use 'vaspkit' and get PBAND_XX.dat and KLABELS files.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('text', usetex = True)    # For LaTeX
plt.style.use('default')        #Styling plot

pband = np.loadtxt('PBAND_Si.dat')      # Load the file

# Energy range or y-limits
ymax = 10
ymin = -10

# Symmetry K points. You get this in KLABELS file form vaspkit output.
X0=0.0
X1=0.86032
X2=1.56277
X3=2.05947
X4=3.05289
X5=4.10656
X6=4.45779

fig, ax = plt.subplots()

ax.set_xlim(X0,X6)
ax.set_ylim(ymin, ymax)
ax.set_ylabel("$E-E_F$ (eV)", fontsize=18)

# Symmetry k-points and their labels. Change the labels in the xticklabels below
# accordingly.
ax.set_xticks([X0, X1, X2, X3, X4, X5, X6])
ax.set_xticklabels(['$\Gamma$', 'L', 'W', 'X', '$\Gamma$', 'K', 'X'], fontsize=14)

plt.grid()
# Add the lines as per your plot. Label them appropriately
# Look for the columns (s value) in the Pband_X.dat.(Column numbers starts from 0)
# Change the s value only.
plt.scatter(pband[:,0], pband[:,1],s=pband[:,2], label='s', linewidth=2)
plt.scatter(pband[:,0], pband[:,1],s=pband[:,5], label='px', linewidth=2)
plt.scatter(pband[:,0], pband[:,1],s=pband[:,3], label='py', linewidth=2)

plt.legend(fontsize=14, bbox_to_anchor=(0.8,0.3), markerscale=9)
plt.tight_layout()

# To save the figure uncomment the line below and change the figure name.
plt.savefig('pband.png', dpi=200)
#plt.savefig('pband.eps')
plt.show()


