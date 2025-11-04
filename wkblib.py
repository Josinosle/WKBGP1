import numpy as np

class Wavefunction:
    def __init__(self, const,energy,mass,barriers):
        self.const = const
        self.energy = energy
        self.mass = mass
        self.barriers = barriers

    def plot(self,ax,start,end):
        x = np.linspace (start,end,10000)
        y,trans_coeff = self.value(x)
        abs_y = np.abs(y)**2
        ax.plot(x,abs_y)
        ax.text(0.02, 0.98, f'T = {trans_coeff:.4f}',
                transform=ax.transAxes, fontsize=12,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        return ax

    def value(self, x):
        #hbar = 1.054571817e-34
        hbar = 1

        v = np.zeros_like(x)
        for b in self.barriers:
            v += b.function(x)

        p = np.emath.sqrt(2 * self.mass * (self.energy - v))

        psi = np.zeros_like(x, dtype=complex)

        # Integrate p dx over this segment
        s = np.zeros_like(x,dtype=complex)
        s[1:] = np.cumsum(0.5 * (p[1:] + p[:-1]) * np.diff(x))

        psi = (self.const / np.emath.sqrt(p)) * np.exp(1j * s / hbar)

        print(s)
        print(s[-1])
        trans_coeff = np.abs(np.exp(2j/hbar * s[-1]))
        return psi,trans_coeff