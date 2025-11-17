# WKB wavefunction approximations over a series of shaped potential barriers
This library provides a toolkit to demonstrate the most primitive application of the WKB approximation on a 1D single particle wave. 
## Installation
requires matplotlib and numpy
```
pip3 install -m numpy
```

```
pip3 install -m matplotlib
```
# barrierlib.py usage
Provides 3 potential shapes:
- cube (step)
- triangle
- gaussian

## Methods
```
# Constructor method for the barrier
init(
	float64: location_on_x_axis,
	float64:64:  width,
	floatheight_of_potential
)
```

```
# Draws the barrier on the axis
draw(
	matplotlib.pyplot.axis: axis_to_draw_on
)

#returns axis
```

```
# function to pull the potential from an numpy x array, not recommended to use
function(
	np.array: x
)

#returns np.array: potential
```
## Example
```
import matplotlib.pyplot
import barrierlib as bl

fig = plt.figure()
ax = fig.add_subplot(111)

Barrier = bl.cube(
	1,   #x
	0.5,   #width
	10   #potential
)

Barrier.draw(ax)
```

# wkblib.py usage
Provides the physics behind defining a WKB approximated wavefront. Because of the triviality of analytically creating a WKB wavefunction but the relatively esoteric application in code, it's not recommended to write you're own code but instead review the code.

## Methods
```
# Constructor method for the wavefunction with its respective parameters
init(
	float64: wavefunction_constant,
	float64: wavefunction_energy,
	float64: particle_mass,
	array_of_barrier_objects: barriers_to_interact_with
)
```

```
# Plots the wavefunction on the axis
plot(
	matplotlib.pyplot.axis: axis_to_draw_on,
	matplotlib.pyplot.figure:
	figure_to_draw_on,
	boolean: save,   #optional, False by default
	boolean: animated   #optional, False by default
)
```

```
# Returns the psi at numpy array x, not recommended to use 
value(
	np.array: x
)

#returns np.array: psi
```

## Example
```
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
```

# Simulation
A simulation section is provided plotting the wavefunction in the classical analytical method over a step barrier. this section is hard-coded and can be run independently without the rest of the library, to help you get an understanding of a more sophisticated simulation, also including the reflection.

This is not using the wkb approximation used in the library and only should be edited by advanced users. Simona has added in depth comments in order to help your way around the document.

# Credits
Simona - simulation section and also providing the bulk of the code for animating the wavefunction plots over time
Joseph - barrierlib.py and wkblib.py independent of time
