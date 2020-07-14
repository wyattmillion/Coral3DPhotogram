#!/bin/bash
# creates individual metashape scripts for 
# submitting each job to the job schedule
# this version works on AWS EC2 with SGE
# usage: batch.sh script list jobname

LOC=$1

if [ "$#" -ne 1 ]
	then
	echo ""
	echo "Usage: Meta_expand.sh filepath/FragDirs.txt"
	echo "Where"
	echo "	filepath:   absolute path to location of FragDirs.txt"
	echo "	FragDirs.txt is a list of absolute file paths for "
	echo "	individual coral fragments within a site directory"
	echo "For example. 'Meta_expand.sh /home/kenkel/Acerv3Dproj/rawPhotos/JulySurvey/WesternSandbo/FragDirs.txt'"
	echo ""
	exit
fi

filelines=`cat $LOC`

#echo $LOC

for line in $filelines; do
#    echo $line;
#    echo test;
    IFS='/' read -ra NAME <<< "$line";
    name1="${NAME[6]}";
    while read script; do
        echo ${script//DIR/$line};
    done < metashapeBase.py > ${name1}.py. #change to the name of the base script that you would like to use as a template
done
