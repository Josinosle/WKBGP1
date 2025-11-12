import matplotlib.pyplot as plt
import barrierlib as bl
import wkblib as wkb

fig = plt.figure()
ax = fig.add_subplot(111)

"""
Barrier1 = bl.cube(1,0.5,10)
ax = Barrier1.draw(ax)
Barrier2 = bl.triangle(1.2,0.5,9)
ax = Barrier2.draw(ax)

Barrier3 = bl.gaussian(8,0.5,11)
ax = Barrier3.draw(ax)
#ax.set_ylim(0,1)
"""

ax.set_xlim(0,20)

Barrier1 = bl.gaussian(4,0.5,4)
Barrier1.draw(ax)
Barrier2 = bl.gaussian(5,0.5,2)
Barrier2.draw(ax)
Barrier3 = bl.triangle(12,0.5,4)
Barrier3.draw(ax)
Barrier4 = bl.cube(16,0.5,3)
Barrier4.draw(ax)

wavefunction = wkb.Wavefunction(1,
                                2,
                                1,
                                (Barrier1,Barrier2,Barrier3,Barrier4))

#Static time independent prob density plot
#ax = wavefunction.plot(ax)
#ax = wavefunction.plot_energy(ax)
#plt.show()

wavefunction.plot_animation(ax,fig,save=True)