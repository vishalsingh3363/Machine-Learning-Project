from setuptools import setup,find_packages
from typing import List

#declaring variable for setup function
PROJECT_NAME="Housing-Predictor"
VERSION="0.0.1"
AUTHOR="Vishal Singh"
DESCRIPTION="This is my first FSDS Nov batch machine learning project"

REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list():  #this function we will read files present in requirement.txt and this will return a list with string
    """
    Description: this function is going to return list of requirement
    mention in requirements.txt file

    return This function will return a list which will contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)


