from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e.'

def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open (file_path) as file_obj:
        requirments=file_obj.readline()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)





setup(
    name='mlproject',
    version='0.0.1',
    author='irfaanhasan',
    author_email='irfaan_hassan_khan005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments("requirments.txt")
)