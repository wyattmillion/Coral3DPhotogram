#!/bin/sh

scripts=`ls *.py`

for script in $scripts; do

    bash metashape.sh -r $script;

done
