from setuptools import find_packages, setup 
from typing import List

hypon_e_dot='-e .'

def get_requrements(file_path: str)->List[str]:
    """this function will provide requirements list"""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
        if hypon_e_dot in requirements:
            requirements.remove(hypon_e_dot)
    return requirements


setup(
name="End to end ml project",
version='0.0.1',
author='Usman',
author_email='usmanashraf4360@gmail.com',
packages=find_packages(),
install_requires=get_requrements('requirements.txt')
    
)