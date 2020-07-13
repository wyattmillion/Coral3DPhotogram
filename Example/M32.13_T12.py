#This is the script to build a model from our example photoset with Metashape via the command line.

import os
#import sys
import Metashape
import glob
#dir = sys.argv[1]
#print(dir)
doc = Metashape.app.document
chunk = Metashape.app.document.addChunk()
os.chdir("/home/kenkel/Acerv3Dproj/rawPhotos/April2019Final/M32.13_T12") #change this to the location of downloaded photoset
cwd = os.getcwd() 
print(cwd)
cwd = cwd.split("/") #split the name into a list by the '/'
doc.save(cwd[-2]+'_'+cwd[-1]+'DM.psz') #names the Metashape Project file based on the last 2 portions of cwd, this can be whatever you want
chunk = doc.chunk
x=glob.glob("/home/kenkel/Acerv3Dproj/rawPhotos/"+cwd[-2]+"/"+cwd[-1]+"/*.JPG")#directs metashape to photos to be used to build the model
chunk.addPhotos(x) #change

#This section is where you can adjust metashape settings to optimize model building
chunk.matchPhotos(accuracy=Metashape.HighAccuracy) #chooses the aligning photos accuracy
chunk.alignCameras()#function to align photos
chunk.buildDepthMaps(quality=Metashape.HighQuality, filter=Metashape.MildFiltering) #builds high quality dense cloud, ability to change quality and depth filtering (best to keep it at "MILD" for the coral images)
#chunk.buildDenseCloud(point_colors = True) #uncomment this if you want to build the mesh from the Dense Cloud Data in next step
chunk.buildModel(surface=Metashape.Arbitrary, source=Metashape.DepthMapsData, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.HighFaceCount) #the build mesh step which is set to build based on the Depth Maps produced earlier.
chunk.buildUV(mapping=Metashape.GenericMapping) #part of build texture step
chunk.buildTexture(blending=Metashape.MosaicBlending, size=25000, fill_holes=True)#rest of build texture step

#names model based on cwd, again, this can be changed to whatever you like, here is where you also define the export file type
chunk.exportModel(cwd[-1]+'_'+'DM_'+"model.obj", binary=True, precision=6, texture_format=Metashape.ImageFormatJPEG, texture=True, normals=True, colors=True, cameras=True, markers=True, udim=False, strip_extensions=False, format=Metashape.ModelFormatOBJ) 
doc.save()
