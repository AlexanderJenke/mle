import os
import sys

if __name__ == '__main__':
    os.system(f"ln -sf -t {sys.path[-1]} $(pwd)")
