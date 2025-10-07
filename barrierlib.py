import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class cube:
    def __init__(self, x, width, potential):
        self.x = x
        self.w = width
        self.v = potential

    def draw(self, ax):
        square = plt.Rectangle((self.x/2,0), self.w, self.v, fill=False, edgecolor='blue', linewidth=2)
        ax.add_patch(square)
        return ax

class triangle:
    def __init__(self, x, width, potential):
        self.x = x
        self.w = width
        self.v = potential

    def draw(self, ax):
        points = [
            (self.x, 0),  # bottom-left
            (self.x + self.w, 0),  # bottom-right
            (self.x + self.w / 2,  self.v)  # top
        ]

        # Create triangle
        triangle = Polygon(points, closed=True, fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(triangle)
        return ax