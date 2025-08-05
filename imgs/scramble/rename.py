import os
import re
from pathlib import Path

# Replace this with the path to your folder
folder = Path('/Users/oliviamaltz/Downloads/Temple Items/GLINT_kids/glint-kids-stimuli/imgs/line/inanimate_natural')

# Regex pattern to match "avocada_scr(number).png"
pattern = re.compile(r'^avocada_LD\((\d+)\)\.png$')

for file in folder.iterdir():
    if file.is_file():
        match = pattern.match(file.name)
        if match:
            number = match.group(1)
            new_name = f'avocado_LD({number}).png'
            new_path = file.with_name(new_name)
            file.rename(new_path)
            print(f'Renamed: {file.name} → {new_name}')
