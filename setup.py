from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> list[str]:
    '''
    Function will returen the list of required packages needed to be install

    '''
    requiments=[]
    with open(file_path) as file_obj:
        requiments=file_obj.readlines()
        for req in requiments:
            requiments=req.replace('\n',"")
            requiments=req.replace('-e .',"")
    return requiments


setup(name='First_Project', 
      version= '0.0.1', 
      author='Nirav Dobariya', 
      author_email='niravdobariya@gmail.com', 
      packages=find_packages(), 
      install_requires=get_requirements('requirements.txt'))