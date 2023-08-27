from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> list[str]:
    '''
    Function will return the list of required packages needed to be install

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for req in requirements:
            requirements=req.replace('\n',"")
            requirements=req.replace('-e .',"")
    return requirements


setup(name='First_Project', 
      version= '0.0.1', 
      author='Nirav Dobariya', 
      author_email='niravdobariya@gmail.com', 
      packages=find_packages(), 
      install_requires=get_requirements('requirements.txt'))