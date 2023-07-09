from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Python code packaged with setuptools',
    url='https://github.com/II-777/goit-python-hw-07',
    author='II-777',
    author_email='777dev0@protonmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pathlib',
        'datetime',
    ],
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.sort:main',
        ],
    }
)
