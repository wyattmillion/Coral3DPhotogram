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
doc.save(cwd[-2]+'_'+cwd[-1]+'.psz') #names the output by the last 2 names in the cwd string, change this to what will properly name the output models
chunk = doc.chunk
x=glob.glob("/home/kenkel/Acerv3Dproj/rawPhotos/"+cwd[-2]+"/"+cwd[-1]+"/*.JPG") #.JEP will change with format your pictures are in
chunk.addPhotos(x) 
chunk.matchPhotos(accuracy=Metashape.HighAccuracy, generic_preselection=True, keypoint_limit=40000, tiepoint_limit=4000) #chooses the aligning photos accuracy
chunk.alignCameras(adaptive_fitting=True)#function to align photos
chunk.buildDepthMaps(quality=Metashape.HighQuality, filter=Metashape.MildFiltering) #builds high quality dense cloud, ability to change quality and depth filtering (best to keep it at "MILD" for the coral images)
chunk.buildDenseCloud(point_colors = True)
chunk.buildModel(surface=Metashape.Arbitrary, source=Metashape.DenseCloudData, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.HighFaceCount) #the "build mesh" step, 
chunk.buildUV(mapping=Metashape.GenericMapping) #part of build texture step
chunk.buildTexture(blending=Metashape.MosaicBlending, size=25000, fill_holes=True)#rest of build texture step
chunk.exportModel(cwd[-2]+cwd[-1]+'_'+"model.obj", binary=True, precision=6, texture_format=Metashape.ImageFormatJPEG, texture=True, normals=True, colors=True, cameras=True, markers=True, udim=False, strip_extensions=False, format=Metashape.ModelFormatOBJ) 
exportReport(/home/kenkel/Acerv3Dproj/rawPhotos/+cwd[-2]+"/"+cwd[-1])
doc.save()

