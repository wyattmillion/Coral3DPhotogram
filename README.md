# Bash and Python scripts for running Agisoft Metashape on a remote HPC server 

Wyatt Million wmillion@usc.edu 

We have developed a workflow in order to build 3D models of Acropora cervicornis coral colonies through a remote HPC system. Aigsoft Metashape is most commonly used through a GUI window however the software's speed is severely limited by processing power of standard personal computers. In an effort to automate 3D model building, we have generated a series of scripts to work around the intricacies of Metashape to go from 2D photographs to 3D models with limited user effort. Metashape requires a license so our workflow works by submitting jobs one after another to build models on a single license. 

This protocol was developed to maximize effeciency using the resources available to biologists and ecologist with beginner/intermediate coding experience. The API manuals from Agisoft are not straightforward so we hope to provide more user-friendly scripts and workflow to guide researchers hoping to add photogrammetry to their toolkit. We have also included an example to go through the protocol on your own. Other protocols on how to take photos for photogrammetry and how to analyze the 3D models that you produce can be found here: link to protocols.io
