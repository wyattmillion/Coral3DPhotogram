import os
#import sys
import Metashape
import glob
#dir = sys.argv[1]
#print(dir)
doc = Metashape.app.document
chunk = Metashape.app.document.addChunk()
os.chdir("DIR")
cwd = os.getcwd() #print current working directory and save as 'cwd'
print(cwd)
cwd = cwd.split("/") #split the name into a list by the '/'
doc.save(cwd[-2]+'_'+cwd[-1]+'DM.psz') #names the output by the last 2 names in the cwd string
chunk = doc.chunk
x=glob.glob("/home/kenkel/Acerv3Dproj/rawPhotos/"+cwd[-2]+"/"+cwd[-1]+"/*.jpg")
chunk.addPhotos(x) #change
chunk.matchPhotos(accuracy=Metashape.HighAccuracy) #chooses the aligning photos accuracy
chunk.alignCameras()#function to align photos
chunk.buildDepthMaps(quality=Metashape.UltraQuality, filter=Metashape.MildFiltering) #builds high quality dense cloud, ability to change quality and depth filtering (best to keep it at "MILD" for the coral images)
#chunk.buildDenseCloud(point_colors = True)
chunk.buildModel(surface=Metashape.Arbitrary, source=Metashape.DepthMapsData, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.HighFaceCount) #the "build mesh" step,
chunk.buildUV(mapping=Metashape.GenericMapping) #part of build texture step
chunk.buildTexture(blending=Metashape.MosaicBlending, size=25000, fill_holes=True)#rest of build texture step
chunk.exportModel(cwd[-2]+cwd[-1]+'_'+'DM_'+"model.obj", binary=True, precision=6, texture_format=Metashape.ImageFormatJPEG, texture=True, normals=True, colors=True, cameras=True, markers=True, udim=False, strip_extensions=False, format=Metashape.ModelFormatOBJ)
#chunk.exportReport("/home/kenkel/Acerv3Dproj/rawPhotos"/cwd[-2]"/"cwd[-1], cwd[-1]+"report.txt")
doc.save()
