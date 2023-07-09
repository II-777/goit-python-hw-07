# goit-python-hw-07

## This python code was packaged using setup.py method

### directory structure:

├── clean_folder
│    ├── clean_folder
│    │   ├── __init__.py
│    │   └── sort.py
│    ├── MANIFEST.in
│    ├── README.md
│    └── setup.py


├── test
│   ├── clean_folder
│   │   ├── __init__.py
│   │   └── sort.py
│   ├── README.md
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── setup.cfg
│   └── test_pr.py

### to create a package, from the diredctory where setup.py is located, run:
python3 setup.py sdist bdist_wheel

### to install packaged version:
pip install .

### now the utility can be run from CLI, as so:
clean-folder
