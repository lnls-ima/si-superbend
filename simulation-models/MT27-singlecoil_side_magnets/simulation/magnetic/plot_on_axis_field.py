
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


plt.rcParams['figure.figsize'] = [12, 6]
plt.rcParams['font.size'] = 22
plt.rcParams['legend.fontsize'] = 22
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 3

filename_bc = '2018-10-10_bc_model13_X=-90_12mm_Z=-1000_1000mm.txt'
filename_sb = '2021-11-06_Superbend_Sirius_MT27_SingleCoil_SideMagnets_X=-80_80mm_Z=-800_800mm_Imc=128A.txt'

zmin = -600
zmax = 600

directory = os.path.dirname(os.path.abspath(__file__))
filename_bc = os.path.join(directory, filename_bc)
filename_sb = os.path.join(directory, filename_sb)

spec = gridspec.GridSpec(
        ncols=1, nrows=1,
        wspace=0.3, hspace=0.25,
        left=0.1, right=0.97, top=0.95, bottom=0.15)
fig = plt.figure()
ax0 = fig.add_subplot(spec[0, 0])

data_bc = np.loadtxt(filename_bc, skiprows=21*2)
data_sb = np.loadtxt(filename_sb, skiprows=18*2)

x_bc = data_bc[:, 0]
z_bc = data_bc[:, 2]
by_bc = data_bc[:, 4]
z_bc = z_bc[x_bc == 0]
by_bc = by_bc[x_bc == 0]

x_sb = data_sb[:, 0]
z_sb = data_sb[:, 2]
by_sb = data_sb[:, 4]
z_sb = z_sb[x_sb == 0]
by_sb = by_sb[x_sb == 0]

filt_bc = (z_bc >= zmin) & (z_bc <= zmax)
z_bc = z_bc[filt_bc]
by_bc = by_bc[filt_bc]

filt_sb = (z_sb >= zmin) & (z_sb <= zmax)
z_sb = z_sb[filt_sb]
by_sb = by_sb[filt_sb]

color_bc = 'tab:green'
color_sb = 'tab:blue'

label_bc = 'BC Dipole'
label_sb = 'Superbend (Single Coil)'

ax0.plot(z_bc, by_bc, color=color_bc, label=label_bc)
ax0.plot(z_sb, by_sb, color=color_sb, label=label_sb)

ax0.legend(loc='best')
ax0.grid(True, ls='--', alpha=0.5)
ax0.patch.set_edgecolor('black')
ax0.patch.set_linewidth('2')
ax0.set_xlabel('Longitudinal Position [mm]', fontweight='bold')
ax0.set_ylabel('Vertical Magnetic Field [T]', fontweight='bold')

plt.show()
