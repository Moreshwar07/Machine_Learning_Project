from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    pass

#DECLARING VARIABLES FOR SETUP FUNCTION

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Moreshwar Baviskar"
DESCRIPTION = "This is a first Machine Learning Project"

REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This fucntion is going to return list
    of requirement in requirements.txt file
    
    return This function is going to return a list which contain
    name of libraries mentioned in requirements.txt file
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name= PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)