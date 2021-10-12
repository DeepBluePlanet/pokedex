import os
import sys
from PIL import Image
file = sys.argv[1]
new_file = sys.argv[2]
if os.path.isdir(new_file):
    print('file already exist')
else:
    os.makedirs(new_file)
    for item in os.listdir(file):
        img = Image.open(f'{file}{item}')
        clean_name = os.path.splitext(item)[0]
        img.save(f'{new_file}{clean_name}.png')






