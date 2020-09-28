import numpy as np
import matplotlib.pyplot as plt
from magpylib.source.magnet import Cylinder
from magpylib import Collection, displaySystem

# create magnets
s1 = Cylinder(mag=(0,0,500), dim=(6,3), pos=(0, 0, -4))
s2 = Cylinder(mag=(0,0,500), dim=(6,3), pos=(0, 0, 4))

c = Collection(s1,s2)

# calculate B-field on a grid
xs = np.linspace(-10,10,20)
zs = np.linspace(-10,10,50)
POS = np.array([(x,0,z) for z in zs for x in xs])
Bs = c.getB(POS).reshape(50,50,3)     #<--VECTORIZED

# create figure
fig = plt.figure(figsize=(9,5))
ax1 = fig.add_subplot(121, projection='3d')  # 3D-axis
ax2 = fig.add_subplot(122)                   # 2D-axis

# display system geometry on ax1
displaySystem(c, subplotAx=ax1, suppress=True)

# display field in xz-plane using matplotlib
X,Z = np.meshgrid(xs,zs)
U,V = Bs[:,:,0], Bs[:,:,2]
ax2.streamplot(X, Z, U, V, color=np.log(U**2+V**2))

plt.show()