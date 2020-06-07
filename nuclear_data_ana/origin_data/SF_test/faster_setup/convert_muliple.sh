#!/bin/bash

# for i in /home/lpc/Documents/scripts/input/FasterFiles/*.fast; do
    # name=$(basename $i .fast)
    # time ./ConvertFasterToRoot $i $name.root
# done

#for i in G:\\SF_test\\faster_setup\\*.setup; do
for i in *.setup; do
    name=$(basename $i .setup)
    echo $name >> result.txt
    awk 'FNR>=367&&FNR<=368' ${i} >> result.txt
done