import os
import glob

def main():
    print('.')
    print(os.listdir('./mytree'))
    print_dir('.')

def print_dir(path, padding=0):
    stuff = os.listdir(path)
    for s in stuff:
        if os.path.isfile(f"{path}/{s}"):
            print(' ' * padding + '├──' + s)
        elif os.path.isdir(f"{path}/{s}"):
            print(' ' * padding + '├──' + s)
            print(f"{path}/{s}")
            print_dir(f"{path}/{s}", padding + 2)
        