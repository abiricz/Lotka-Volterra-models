# Lotka-Volterra model simulation
# Author: BIRICZ A
# Date: 22-24.10.2017

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 44.5561, 0.437034 # mean and standard deviation
#s = np.random.lognormal(mu, sigma, 1000)

x = np.linspace(0.001, 300, 10000)
pdf = (np.exp(-(np.log(x- mu) )**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))

# plot
fig1 = plt.figure( num=1, figsize=(11, 5), dpi=100, facecolor='w', edgecolor='k' )
ax1 = fig1.add_subplot(111)

# subplot data
ax1.plot( x, pdf, 'b-')
#ax1.plot( t_1, y0_1, 'r--')
#ax1.plot( t_1, y1_1, 'c--')

# subplot labels
ax1.set_xlabel('t', fontsize=14 )
ax1.set_ylabel('p(t) / P(t) (blue/yellow)', fontsize=14 )
#ax2.set_xlabel('P(t)', fontsize=14 )
#ax2.set_ylabel('p(t)', fontsize=14 )

#fig1.text('fig title')
# Set common labels
#fig1.text(0.5, -0.02, 'common xlabel', ha='center', va='center', fontsize=16 )
#fig1.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical', fontsize=16)
fig1.text(0.5, 0.97, 'Lotka-Volterra I', ha='center', va='center', fontsize=16)

ax1.set_title('Changes in the population over time')
#ax2.set_title('Phase-space plot (prey-predator)')

plt.savefig('lognormal.png', dpi=200)

# customize and save