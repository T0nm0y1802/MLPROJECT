from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_pat:str)->List[str]:
    requrements=[]
    with open(file_pat) as file_obj:
        requrements=file_obj.readlines()
        requrements=[req.replace("\n","") for req in requrements]

        if HYPHEN_E_DOT in requrements:
            requrements.remove(HYPHEN_E_DOT)
    return requrements

setup(
        name='MLproject',
        version='0.0.1',
        author="Tanmay",
        author_email='tanmaymathur1802@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements('requirements.txt') 
)
 