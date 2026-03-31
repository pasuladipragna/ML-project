from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    '''This function reads the requirements from a file and returns them as a list of strings.
    '''
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements if req.strip()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements



setup(
    name="ml_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author="Pragna",
    description="A machine learning project",
    author_email="22x31a6668@gmail.com"
)