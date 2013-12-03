#
# Read in generated data, display & compare it
# Needs manual file paths and grid dimension settings for now...
# 
import sys
from manta import *
from helperInclude import *

# solver params
dim = 3
res = 45
gs = vec3(res,res,res)
if (dim==2):
	gs.z=1

basename1 = "test_2045_fallingDrop_v01.py"
#basename2 = basename1 # optionally, make different
basename2 = "test_2045_fallingDrop_v02.py"

s = Solver(name='main', gridSize = gs, dim=dim)
flags    = s.create(FlagGrid)
real1    = s.create(RealGrid)
real2    = s.create(RealGrid)
realErr   = s.create(RealGrid)

#ls1      = s.create(LevelsetGrid)
#ls2      = s.create(LevelsetGrid)
#lsErr    = s.create(RealGrid)

mac1     = s.create(VecGrid)
mac2     = s.create(VecGrid)
macErr   = s.create(VecGrid)

parts1    = s.create(BasicParticleSystem) 
pDens1    = parts1.create(PdataReal) 
pTest1    = parts1.create(PdataReal) 

parts2    = s.create(BasicParticleSystem) 
pDens2    = parts2.create(PdataReal) 

flags.initDomain(boundaryWidth=0)

if 1 and (GUI):
	gui = Gui()
	gui.show()
	gui.pause()
    
# try to load uni file if it exists
def tryToLoad( grid, basename, suffix ):
	rfile = referenceFilename( basename, suffix ) 
	print("Trying to load " + rfile)
	if(os.path.isfile(rfile)):
		grid.load(rfile)
	else:
		grid.clear()
	return 1

# to be initialized later on...
realErrMax = 0
macErrMax = 0
lsErrMax = 0
partErrMax = 0

#main loop
for t in range(150):

	if(0):
		tryToLoad( real1, basename1, ("dens_%04d"  % t) )
		tryToLoad( real2, basename2, ("dens_%04d"  % t) )
		realErr.sub(real1,real2);
		realErrMax = gridMaxDiff(real1, real2)
	
		realErr.print(zSlice=15) 
		print("Max difference in step " +str(t) + " = "+ str(realErrMax) )

	if(1):
		tryToLoad( mac1, basename1, ("vel" ) ) #  % t
		tryToLoad( mac2, basename2, ("vel" ) ) #  % t
		macErr.sub(mac1,mac2);
		macErrMax = gridMaxDiffVec3(mac1, mac2)
	
		macErr.print(zSlice=15) 
		print("Max vec3 difference in step " +str(t) + " = "+ str(macErrMax) )

	# load particles
	if(0):
		tryToLoad( parts1 , basename1, ("parts_%04d"  % t) )
		tryToLoad( parts2 , basename2, ("parts_%04d"  % t) )

	#tryToLoad( pDens1 , basename1, ("pdens_%04d"  % t) )

	s.step()
    
