# goit-python-hw-07

## Task

In this homework we will make a Python package and a console script that can be called anywhere in the system from the console with the clean-folder command. For this you need to create a structure of files and folders:
```
├───clean_folder
│ ├── clean_folder
│ │ ├── clean.py
│ │ └── __init__.py
│ └── setup.py
```
In clean_folder/clean_folder/clean.py you need to put everything we did in the previous homework on folder parsing. Your main task is to write clean_folder/setup.py so that the built-in Python toolkit can install this package and the operating system can use this package as a console command.

## The Evaluation Criteria

- The package is installed on the system with the pip install -e command . (or python setup.py install, administrator rights required).
- Once installed, the package clean_folder appears in the system.
- When the package is installed in the system the script can be called anywhere from the console with the clean-folder command
- The console script handles command line arguments in exactly the same way as a Python script.
