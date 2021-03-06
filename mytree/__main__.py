import os
import glob

dirs_to_ignore = [
    ".git"
]

def main():
    print('.')
    print_dir('.')

def print_dir(path, padding=0, start_symbol=""):
    stuff = os.listdir(path)
    stuff.sort(key=lambda s: os.path.isfile(s))
    symbol = '├──'
    for i, s in enumerate(stuff, start=1):
        if i == len(stuff):
            symbol = '└──'
        else:
            symbol = '├──'
        if os.path.isfile(f"{path}/{s}"):
            print(start_symbol + symbol + s)
        elif os.path.isdir(f"{path}/{s}") and not s in dirs_to_ignore:
            print(start_symbol + symbol + s)
            if i == len(stuff):
                print_dir(f"{path}/{s}", padding + 1, start_symbol + "   ")
            else:
                print_dir(f"{path}/{s}", padding + 1, start_symbol + "│  ")
        