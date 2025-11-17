import matplotlib.pyplot as plt
import barrierlib as bl
import wkblib as wkb

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim(0,20)

Barrier1 = bl.gaussian(8,0.5,4)
Barrier2 = bl.gaussian(9,0.6,6)
Barrier1.draw(ax)
Barrier2.draw(ax)

wavefunction = wkb.Wavefunction(1,   #constant
                                3,   #energy
                                1,   #mass
                                [Barrier1,Barrier2])   #barriers

wavefunction.plot(ax,fig,save=False,animated=False)