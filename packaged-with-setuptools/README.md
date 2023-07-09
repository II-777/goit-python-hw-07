# goit-python-hw-07

## This python code was packaged using setup.py method

### initial directory structure:

├── packaged_with_setuptools
│    ├── clean_folder
│    │   ├── __init__.py
│    │   └── sort.py
│    ├── MANIFEST.in
│    ├── README.md
│    └── setup.py


### to create a package, from the diredctory where setup.py is located, run:
python3 -m build

### to install packaged version:
pip install .

### now the utility can be run from CLI, like so:
clean-folder testfolder/
