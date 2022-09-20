#!/usr/bin/env python3

from glob import glob
import argparse
import sys
import subprocess
import os


def main():
    """
        Run face restoration on an entire dataset of face images.
    """
    arguments = parse_command_line_arguments()
    source_directory = arguments.source_directory[0]

    #subdirectories = glob('inputs/whole_imgs/facescrub-actresses-lowkey/*', recursive = True)
    subdirectories = glob('inputs/whole_imgs/' + source_directory + '/*', recursive = True)

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
                         'results/' + source_directory + '/' + os.path.basename(folder),
                         '-v',
                         '1.3',
                         '-s',
                         '2'])


def parse_command_line_arguments() -> argparse.ArgumentParser:
    """
        Parse the arguments from the command-line.
        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        (argparse.ArgumentParser): the parser with command-line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--source_directory', nargs=1, required=True,
                        help='Directory with images of people under "input/whole_imgs".')

    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


main()
