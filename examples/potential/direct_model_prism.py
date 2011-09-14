"""
Create synthetic data from a right rectangular prism model.
"""
from matplotlib import pyplot as mpl
import numpy
from fatiando import potential, mesher, gridder, vis, logger

log = logger.get()
log.info(logger.header())
log.info("Example of direct modelling using right rectangular prisms")

log.info("Calculating...")
prisms = [mesher.RightRectangularPrism(-4000,-3000,-4000,-3000,0,2000,density=1000),
          mesher.RightRectangularPrism(-1000,1000,-1000,1000,0,2000,density=-1000),
          mesher.RightRectangularPrism(2000,4000,3000,4000,0,2000,density=1000)]
xp, yp, zp = gridder.regular(-5000, 5000, -5000, 5000, 100, 100, z=-100)
gz = potential.prism.gz(prisms, xp, yp, zp)

log.info("Plotting...")
mpl.axis('scaled')
mpl.title("gz produced by prism model (mGal)")
vis.pcolor(xp, yp, gz, (100,100))
mpl.colorbar()
mpl.show()