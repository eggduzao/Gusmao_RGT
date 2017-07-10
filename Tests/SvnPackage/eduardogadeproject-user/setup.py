import os
import sys
from setuptools import setup, find_packages

#################################################
# Setup
#################################################

version = "0.0.1"
setup(name="myPackage",
      version=version,
      description=("My Package"),
      author='Myself',
      author_email='me@myhome.mim',
      license='GPL',
      packages=find_packages(),
      entry_points = {
          'console_scripts': [
              'myPackageSS2 = myPackage.tool1.mainTool1:main'
          ]
      }
      )


