# src/main.py

import sys
from cropper import create_cropped_versions

def main(image_path):
    create_cropped_versions(image_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])