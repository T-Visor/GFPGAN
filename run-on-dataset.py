#!/usr/bin/env python3

from glob import glob
import sys
import subprocess
import os

subdirectories = glob('inputs/whole_imgs/facescrub-actresses-lowkey/*', recursive = True)

print('---FOLDERS FOUND---')
for folder in subdirectories:
    print(folder)
print('-------------------\n')

for folder in subdirectories:
    print('Processing folder:', folder)
    subprocess.call(['python3',
                     'inference_gfpgan.py',
                     '-i',
                     folder,
                     '-o',
                     'results/' + os.path.basename(folder),
                     '-v',
                     '1.3',
                     '-s',
                     '2'])

# python3 inference_gfpgan.py -i inputs/whole_imgs/facescrub-actresses-lowkey/Adrianne_León/ -o results/Adrianne_Leon -v 1.3 -s 2 
