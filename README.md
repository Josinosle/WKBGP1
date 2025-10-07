# WKBGP1
Group project 1 plotting wavefunction code and provided barrier shape library

Participants will use the provided library to draw barriers, and use the WKB approximation (independent in time) to plot a wavefunction tunnelling through drawn shapes.

## Shape Library Objects
- cube(x,width,potential): Creates a cube at coordinate x with potential V and width W.
- triangle(x,width,potential): Creates a triangle at coordinate x with potential V and width W.
- gaussian(x,width,potential): Creates a gaussian barrier at coordinate x with potential V and width W.

# Shape Library Functions
- constructor: See above objects for their constructor parameters. Example:```Barrier1 = barrierlib.cube(x,V)```
- is_inside(x,function): Takes an x and a function in terms of x returns whether it is inside the barrier.
- draw(ax): Draws the barrier on axes ax and returns.
