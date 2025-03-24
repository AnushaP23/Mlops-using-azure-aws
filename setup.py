#to create the mlproject as a package and deploy it in pypi gives access to anyone
from setuptools import find_packages, setup #to find all packages
from typing import List
HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)-> List[str]:
    #this will return a list of requirements
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace('/n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        



#info about of the entire project
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Anusha',
    author_email='anusha.hullathi@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)

#for setup.py to find out how many packages are there and all we create src folder to convert into package init file is created


