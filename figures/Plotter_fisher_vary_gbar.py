"""
Fisher information for position measurement

"""
import numpy as np
import matplotlib.pyplot as plt

filenamek1 = "data/fisher_gbar1"
filenamek2 = "data/fisher_gbar5"
filenamek3 = "data/fisher_gbar10"

fisherk1 = []
fisherk2 = []
fisherk3 = []


with open(filenamek1) as f:
     for line in f:
        fisherk1.append(float(line))
with open(filenamek2) as f:
     for line in f:
        fisherk2.append(float(line))
with open(filenamek3) as f:
     for line in f:
        fisherk3.append(float(line))

times1 = np.linspace(np.pi, 3*np.pi, len(fisherk1))
times2 = np.linspace(np.pi, 3*np.pi, len(fisherk2))
times3 = np.linspace(np.pi, 3*np.pi, len(fisherk3))


for n in range(0,2):
  del fisherk1[::2]
  del fisherk2[::2]
  del fisherk3[::2]
  times1 = times1[1::2]
  times2 = times2[1::2]
  times3 = times3[1::2]

""" Latex Parameters """
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
params = {'font.size': 50,
              'axes.labelsize': 50,
              'legend.fontsize': 40,
              'xtick.labelsize': 50,
              'ytick.labelsize': 50,
              'text.latex.preamble': [r'\usepackage{physics}', r'\usepackage{amsmath}']}
plt.rcParams.update(params)

""" Create plot """
plt.figure(figsize=(13,13))

""" Axes """
ax = plt.subplot(111)
ax.tick_params(axis='both', which='major')
plt.xticks([3*np.pi/2, 7*np.pi/4, 2*np.pi, 9*np.pi/4, 5*np.pi/2], [r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$', r'$9\pi/4$', r'$5\pi/2$'])

""" Plotting """
plt.plot(times1, fisherk1, '-o', color = 'k', markeredgewidth=0.0,  label = r'$\bar{g}= 1$', markersize = 12, linewidth=2)
plt.plot(times2, fisherk2, '-^', color = 'b', markeredgewidth=0.0, label = r'$\bar{g}= 5$', markersize = 12, linewidth=2)
plt.plot(times3, fisherk3, '-v', color = 'm', markeredgewidth=0.0, label = r'$\bar{g}= 10$', markersize = 12, linewidth=2)

""" Limit data range """ 
plt.xlim([3*np.pi/2, 5*np.pi/2])

""" Labels """
plt.xlabel(r'\textbf{time} (t)')
plt.ylabel(r'\textbf{CFI} ($\bar{I}_F$)')
plt.subplots_adjust(top=0.8)
plt.legend(loc = 2, frameon = False)
ax.annotate(r'$\lambda = 1/2$', xy=(1, 1), xytext=(-33, -33), fontsize=40,
    xycoords='axes fraction', textcoords='offset points',
    bbox=dict(facecolor='white', alpha=0, boxstyle="round,pad=0.3"),
    horizontalalignment='right', verticalalignment='top')


plt.savefig("Fisher_vary_gbar.pdf",transparent=True, dpi=600,bbox_inches='tight')
plt.show()