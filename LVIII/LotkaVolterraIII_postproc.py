# Lotka-Volterra model simulation
# Author: BIRICZ A
# Date: 22-24.10.2017

import numpy as np
import matplotlib.pyplot as plt

# ytemp = np.empty( (Neqs), dtype = float )
#read data from file, store
f1 = open('LVIII_p20_P13b001.dat', 'r')
t, y0, y1 = np.loadtxt(f1, delimiter=' ', usecols=(0, 1, 2), unpack=True)

#f2 = open('LVIII_p5_P5.dat', 'r')
#t_1, y0_1, y1_1 = np.loadtxt(f2, delimiter=' ', usecols=(0, 1, 2), unpack=True)

#f3 = open('LVII_p13_P20.dat', 'r')
#t_2, y0_2, y1_2 = np.loadtxt(f3, delimiter=' ', usecols=(0, 1, 2), unpack=True)

# plot
fig1 = plt.figure( num=1, figsize=(11, 5), dpi=100, facecolor='w', edgecolor='k' )
ax1 = fig1.add_subplot(121)
ax2 = fig1.add_subplot(122)

# subplot data
ax1.plot( t, y0, 'b-')
ax1.plot( t, y1, 'k-')
#ax1.plot( t_1, y0_1, 'r--')
#ax1.plot( t_1, y1_1, 'c--')
ax2.plot( y1, y0, 'k-')
#ax2.plot( y1_1, y0_1, 'r--')
#ax2.plot( y1_2, y0_2, 'b-')

# subplot labels
ax1.set_xlabel('t', fontsize=14 )
ax1.set_ylabel('p(t) / P(t)', fontsize=14 )
ax2.set_xlabel('P(t)', fontsize=14 )
ax2.set_ylabel('p(t)', fontsize=14 )

#fig1.text('fig title')
# Set common labels
#fig1.text(0.5, -0.02, 'common xlabel', ha='center', va='center', fontsize=16 )
#fig1.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical', fontsize=16)
fig1.text(0.5, 0.97, 'Lotka-Volterra III', ha='center', va='center', fontsize=16)

ax1.set_title('Changes in the population over time')
ax2.set_title('Phase-space plot (prey-predator)')

plt.savefig('LVIIIb001.png', dpi=200)

# customize and save