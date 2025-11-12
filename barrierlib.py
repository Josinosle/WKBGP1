import matplotlib.pyplot as plt
import numpy as np


class cube:
    def __init__(self, x, width, potential):
        self.x = x
        self.w = width
        self.h = potential

    def function(self, a):
        condition = (a > self.x - self.w / 2) & (a < self.x + self.w / 2)
        return np.where(condition, self.h, 0)

    def draw(self, ax):
        square = plt.Rectangle((self.x-self.w/2,0), self.w, self.h, fill=False, edgecolor='blue', linewidth=1, linestyle='--')
        ax.add_patch(square)
        return ax

class triangle:
    def __init__(self, x, width, potential):
        self.x = x           # center of the triangle
        self.w = width       # base width
        self.h = potential      # maximum potential (peak height)

    def function(self, a):
        # Create a triangular potential centered at self.x
        left = self.x - self.w / 2
        right = self.x + self.w / 2
        v = np.zeros_like(a)

        # Linearly ramp up on the left, down on the right
        rising = (a >= left) & (a < self.x)
        falling = (a >= self.x) & (a <= right)

        v[rising] = self.h * (a[rising] - left) / (self.w / 2)
        v[falling] = self.h * (right - a[falling]) / (self.w / 2)
        return v

    def draw(self, ax):
        # Draw an outline of the triangular potential
        left = self.x - self.w / 2
        right = self.x + self.w / 2
        ax.plot([left, self.x, right], [0, self.h, 0], color='green', lw=1, linestyle='--')
        return ax

class gaussian:
    def __init__(self, x, std, potential):
        self.x = x
        self.w = std
        self.h = potential

    def function(self, a):
        v = self.h * np.exp(- (a-self.x)**2 / (2*self.w**2))
        return v

    def draw(self, ax):
        xmin,xmax = ax.get_xlim()

        x = np.linspace(xmin,xmax,100)
        ax.plot(x, self.function(x), color='red', lw=1, linestyle='--')
        return ax