# WKBGP1
Group project 1 plotting wavefunction code and provided barrier shape library

Participants will use the provided library to draw barriers, and use the WKB approximation (independent in time) to plot a wavefunction tunnelling through drawn shapes.

## Shape Library Draw Functions
- cube(x,potential): Draws a cube at coordinate x with potential V.
- triangle(x,potential): Draws a triangle at coordinate x with potential V.
- gaussian(x,potential): Draws a gaussian barrier at coordinate x with potential V.
- is_inside(x,function): Takes an x and a function in terms of x returns whether it is inside the barrier.
- draw(ax): Draws a barrier on axes ax. Returns true on success.
