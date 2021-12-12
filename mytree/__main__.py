import os
import glob

dirs_to_ignore = [
    ".git"
]

def main():
    print('.')
    print_dir('.')

def print_dir(path, padding=0):
    stuff = os.listdir(path)
    stuff.sort(key=lambda s: os.path.isfile(s))
    for s in stuff:
        if os.path.isfile(f"{path}/{s}"):
            print(' ' * padding + '├──' + s)
        elif os.path.isdir(f"{path}/{s}") and not s in dirs_to_ignore:
            print(' ' * padding + '├──' + s)
            print_dir(f"{path}/{s}", padding + 3)
        