import numpy as np

class Wavefunction:
    def __init__(self, const,energy,mass,barriers):
        self.const = const
        self.energy = energy
        self.mass = mass
        self.barriers = barriers

    def plot(self,ax,start,end):
        x = np.linspace (start,end,100)
        y = self.value(x)
        abs_y = np.abs(y)**2
        ax.plot(x,abs_y)
        return ax

    def value(self, x, sign=+1):
        hbar = 1

        v = np.zeros_like(x)
        for b in self.barriers:
            v += b.function(x)

        p = np.emath.sqrt(2 * self.mass * np.abs(self.energy - v))
        allowed = self.energy > v

        # Find turning points (E = V)
        turning_points = np.where(np.diff(allowed.astype(int)) != 0)[0]
        segments = np.split(np.arange(len(x)), turning_points + 1)

        psi = np.zeros_like(x, dtype=complex)
        s_total = 0.0  # to accumulate phase

        for seg in segments:
            xi = x[seg]
            pi = p[seg]
            allowed_seg = allowed[seg]

            # Integrate p dx over this segment
            s = np.zeros_like(xi)
            s[1:] = np.cumsum(0.5 * (pi[1:] + pi[:-1]) * np.diff(xi))
            s += s_total  # continue cumulative phase from previous segment
            s_total = s[-1]

            if allowed_seg[0]:
                psi[seg] = (self.const / np.sqrt(pi)) * np.exp(1j * sign * s / hbar) #Classical Case
            else:
                psi[seg] = (self.const / np.sqrt(pi)) * np.exp(-sign * s / hbar) #Barrier Case
                trans_coeff = np.exp(-sign * s_total / hbar)
                self.const *= trans_coeff
        return psi