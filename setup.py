from setuptools import find_packages,setup
from typing import List

HYPYEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n"," ") for req in requirements]
        if HYPYEN_E_DOT  in requirements:
            requirements.remove(HYPYEN_E_DOT)

        return requirements 

setup(
    name ='DiamondPricePrediction',
    version = '0.0.1',
    authon =    'Rahul Sahani',
    authon_email = 'rahulsahani734000@gmail.com',
    install_requires =get_requirements('requirement.txt'),
    packages=find_packages()

)