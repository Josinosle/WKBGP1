import numpy as np
from matplotlib.animation import FuncAnimation

class Wavefunction:
    def __init__(self, const,energy,mass,barriers):
        self.const = const
        self.energy = energy
        self.mass = mass
        self.barriers = barriers

    def plot_energy(self,ax):
        ax.hlines(self.energy,0,ax.get_xlim()[1],'k',alpha=0.5,color='blue',linestyle="--")
        return ax

    def plot(self,ax):
        ax_min = ax.get_xlim()[0]
        ax_max = ax.get_xlim()[1]

        x = np.linspace (ax_min,ax_max,10000)
        y,trans_coeff = self.value(x)
        abs_y = (np.abs(y))**2
        ax.plot(x,abs_y,alpha=1,color='black')
        ax.text(0.02, 0.98, f'T = {trans_coeff:.4f}',
                transform=ax.transAxes, fontsize=12,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        return ax

    def plot_animation(self,ax,fig,save=False):
        dt = 0.01
        frames = 300  # change duration of simulation
        pause_frames = 30  # length of pause before restarting loop
        line, = ax.plot([], [], linewidth=1.5, label='|Ψ(x,t)|', color='blue',
                        zorder=1)  # creates empty line object that updates each time. [] means start with no data

        def animate(frame):
            t = frame * dt

            ax_min = ax.get_xlim()[0]
            ax_max = ax.get_xlim()[1]

            x = np.linspace(ax_min, ax_max, 10000)
            psi = (self.value(x))[0] * np.exp(-1j*self.energy*t)

            ax.set_ylim([0,ax.get_ylim()[1]])
            ax.hlines(self.energy, 0, ax.get_xlim()[1], 'k', alpha=0.5, color='blue', linestyle="--")
            line.set_data(x, self.energy+np.real(psi))  # updates with new data. prob density (blue envelope)
            ax.set_title(f'Wave Packet Through Potential Barrier (t= {t:.3f})',
                         fontsize=14)  # updates title to show current time

        anim = FuncAnimation(fig, animate, frames=frames + pause_frames,
                             interval=20, blit=False,
                             repeat=True)  # faster/smoother with blit=True, but doesnt update time in the title

        fig.tight_layout()
        if save:
            anim.save('wkb_animation.gif', dpi=80, writer='pillow')
        fig.show()


    def value(self, x):
        hbar = 1

        v = np.zeros_like(x)
        for b in self.barriers:
            v += b.function(x)

        p = np.emath.sqrt(2 * self.mass * (self.energy - v))

        # Integrate p dx over this segment
        s = np.zeros_like(x,dtype=complex)
        s[1:] = np.cumsum(0.5 * (p[1:] + p[:-1]) * np.diff(x))

        psi = (self.const / np.emath.sqrt(p)) * np.exp(1j * s / hbar)

        trans_coeff = np.abs(np.exp(2j/hbar * s[-1]))
        return psi,trans_coeff